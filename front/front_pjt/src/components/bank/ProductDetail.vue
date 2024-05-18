<template>
<div class="container">
    <div class="text-container">
        <h2>
            <span>{{ selectedTerm }}</span>개월 동안 
            <input :value="localUserAmount" @input="updateUserAmount($event.target.value)" type="number" placeholder="금액을 입력해주세요" class="input-amount" /> 
            원을 예치하면,
        </h2>
        <h2>최대 만기 금액은 <span class="highlight">{{ formatCurrency(maxMaturityAmount) }}</span>원 이에요 😎</h2>
    </div>
    <div class="product-container">
        <div v-for="(product, index) in selectedProducts" :key="index" class="product-card">
            <h3>{{ product.fin_prdt_nm }}</h3>
            <p>금리: 최대 {{ product.intr_rate }}%</p>
            <br>
            <h4 class="maturity-amount">{{ formatCurrency(calculateMaturityAmount(product.intr_rate)) }}원</h4>
        </div>
    </div>
</div>
</template>

<script setup lang="ts">
import { defineProps, ref, computed, watch, defineEmits } from 'vue';

interface Product {
  fin_prdt_nm: string;
  intr_rate: number;
}

const props = defineProps<{
  selectedProducts: Product[],
  selectedTerm: number | string,
  userAmount: number
}>();

const emit = defineEmits(['update:userAmount']);

const localUserAmount = ref(props.userAmount);

watch(() => props.userAmount, (newVal) => {
  localUserAmount.value = newVal;
});

const updateUserAmount = (value: string) => {
  const numericValue = Number(value);
  if (!isNaN(numericValue)) {
    localUserAmount.value = numericValue;
    emit('update:userAmount', numericValue);
  }
};

const calculateMaturityAmount = (interestRate: number): number => {
  return localUserAmount.value * (1 + interestRate / 100);
};

const maxMaturityAmount = computed(() => {
  if (props.selectedProducts.length === 0 || !localUserAmount.value || isNaN(localUserAmount.value)) {
    return 0;
  }
  const maturityAmounts = props.selectedProducts.map(product => calculateMaturityAmount(product.intr_rate));
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
.input-amount {
width: 150px;
text-align: center;
border: none;
border-bottom: 1px solid #ccc;
outline: none;
font-size: 1.2em;
margin: 0 10px;
}

.product-container {
display: flex;
gap: 20px; /* 카드 사이의 간격 */
}
.maturity-amount {
  margin-top: auto;
  text-align: center;
}

.product-card {
  border: 1px solid #ddd;
  padding: 20px;
  background-color: white; 
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  width: 200px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.text-container{
    margin-bottom:40px;
}

.container{
    padding: 50px;
}

.highlight{
    color:#3b9676;
}
</style>
