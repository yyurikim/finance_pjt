<template>
  <div class="container">
    <div class="text-container">
      <h2>
        <span>{{ selectedTerm }}</span>개월 동안 
        <input v-model.number="localUserAmount" type="number" placeholder="금액을 입력해주세요" class="input-amount" /> 
        원을 예치하면,
      </h2>
      <h2>최대 만기 금액은 <span class="highlight">{{ formatCurrency(maxMaturityAmount) }}</span>원 이에요 😎</h2>
    </div>
    <div class="product-container">
      <div v-for="(product, index) in selectedProducts" :key="index" class="product-card">
        <h3>{{ product.fin_prdt_nm }}</h3>
        <p>금리: 최대 {{ product.intr_rate }}%</p>
        <p>금리 유형: {{ product.intr_rate_type_nm }}</p> <!-- 금리 유형 출력 -->
        <br>
        <h4 class="maturity-amount">{{ formatCurrency(calculateMaturityAmount(product.intr_rate, product.intr_rate_type_nm)) }}원</h4>
      </div>
      <div style="color: grey;">
        <p>*해당 금액은 일반과제 15.4%를 적용한 결과입니다.</p>
        <p>*실제 상품 적용 시 달라질 수 있으니 가까운 영업점을 통해 상담 받으시기 바랍니다.</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { defineProps, ref, computed, watch, defineEmits } from 'vue';

interface Product {
  fin_prdt_nm: string;
  intr_rate: number;
  intr_rate_type_nm: string; // 금리 유형 추가
}

const props = defineProps<{
  selectedProducts: Product[],
  selectedTerm: number | string,
  userAmount: number,
  isDeposit: boolean // 예금(true)인지 적금(false)인지 구분
}>();

const emit = defineEmits(['update:userAmount']);

const localUserAmount = ref(props.userAmount);

// watch를 통해 userAmount 변경 시 localUserAmount 업데이트
watch(() => props.userAmount, (newVal) => {
  localUserAmount.value = newVal;
});

watch(localUserAmount, (newVal) => {
  emit('update:userAmount', newVal);
});

// 만기 금액 (일반과세 적용)
const calculateMaturityAmount = (interestRate: number, rateType: string): number => {
  console.log('isDeposit:', props.isDeposit);
  const termInMonths = Number(props.selectedTerm);
  if (isNaN(termInMonths) || isNaN(interestRate) || isNaN(localUserAmount.value)) {
    return 0;
  }
  const termInYears = termInMonths / 12;
  const taxRate = 0.154; // 이자소득세 15.4%
  let maturityAmount = 0;
  let interestEarned = 0;

  if (props.isDeposit) {
    // 예금 계산
    if (rateType === '단리') {
      interestEarned = localUserAmount.value * (interestRate / 100) * termInYears;
      maturityAmount = localUserAmount.value + interestEarned * (1 - taxRate);
    } else if (rateType === '복리') {
      maturityAmount = localUserAmount.value * Math.pow((1 + interestRate / 100 / 12), termInMonths);
      interestEarned = maturityAmount - localUserAmount.value;
      maturityAmount -= interestEarned * taxRate;
    }
  } else {
    // 적금 계산
    if (rateType === '단리') {
      for (let i = 1; i <= termInMonths; i++) {
        const monthlyDeposit = localUserAmount.value;
        const monthlyInterest = monthlyDeposit * (interestRate / 100) * ((termInMonths - i + 1) / 12);
        interestEarned += monthlyInterest * (1 - taxRate);
      }
      maturityAmount = localUserAmount.value * termInMonths + interestEarned;
    } else if (rateType === '복리') {
      for (let i = 1; i <= termInMonths; i++) {
        const monthlyDeposit = localUserAmount.value;
        maturityAmount += monthlyDeposit * Math.pow((1 + interestRate / 100 / 12), (termInMonths - i + 1));
      }
      interestEarned = maturityAmount - (localUserAmount.value * termInMonths);
      maturityAmount -= interestEarned * taxRate;
    }
  }

  return Math.round(maturityAmount); // 소수점 이하 절삭
};

// 최대 만기 금액
const maxMaturityAmount = computed(() => {
  if (props.selectedProducts.length === 0 || !localUserAmount.value || isNaN(localUserAmount.value)) {
    return 0;
  }
  const maturityAmounts = props.selectedProducts.map(product => calculateMaturityAmount(product.intr_rate, product.intr_rate_type_nm));
  return Math.max(...maturityAmounts);
});

const formatCurrency = (value: number): string => {
  const formatter = new Intl.NumberFormat('ko-KR', {
    minimumFractionDigits: 0,
    maximumFractionDigits: 0
  });
  return formatter.format(value);
};
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.text-container {
  text-align: center;
  margin-bottom: 20px;
}

.input-amount {
  width: 200px;
  padding: 10px;
  margin: 0 10px;
}

.product-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
}

.product-card {
  border: 1px solid #ddd;
  padding: 20px;
  border-radius: 8px;
  width: 240px;
  text-align: center;
}

.highlight {
  font-weight: bold;
  color: #ff6347;
}

.maturity-amount {
  font-weight: bold;
  color: #2e8b57;
}
</style>
