<template>
  <div v-if="data" class="container">
        <div class="tabs">
      <button v-for="term in [6, 12, 24, 36]" :key="term" @click="setTerm(term)" :class="{'active-tab': selectedTerm === term}">
        {{ term }}개월
      </button>
    </div>
    <div class="row">
      <div class="column">
        <h2>예금 추천상품</h2>
        <ul>
          <li v-for="(product, index) in data[`${selectedTerm}개월`].deposits.slice(0, 5)" :key="index" @click="openDialog(product)">
            <h4>{{ product.fin_prdt_nm }}</h4>
            <p>{{ product.kor_co_nm }}</p>
            <p>만기 예상 금액 : <strong>{{  formatCurrency(product.expectedMaturity) }}</strong>원</p>
          </li>
        </ul>
      </div>
      <div class="column">
        <h2>적금 추천상품</h2>
        <ul>
          <li v-for="(product, index) in data[`${selectedTerm}개월`].savings.slice(0, 5)" :key="index" @click="openDialog(product)">
            <h4>{{ product.fin_prdt_nm }}</h4>
            <p>{{ product.kor_co_nm }}</p>
            <p>만기 예상 금액 : <strong>{{  formatCurrency(product.expectedMaturity) }}</strong>원</p>
          </li>
        </ul>
      </div>
    </div>
    <div class="row">
      <div class="column full">
        <h2>고객님의 소비 성향({{ usertype }})에 맞는 상품을 추천했어요</h2>
        <br>
        <p>1. {{ savingType }}</p>
        <p>2. {{ meaningoutType }}</p>
        <p>3. {{ portfolioType }}</p>
      </div>
    </div>
    <!-- 상품 상세 정보 다이얼로그 -->
    <div v-if="dialog" class="modal">
      <div class="modal-content">
        <span class="close" @click="dialog = false">&times;</span>
        <h3>{{ dialogProduct.fin_prdt_nm }}</h3>
        <p><strong>은행명:</strong> {{ dialogProduct.kor_co_nm }}</p>
        <p><strong>우대조건:</strong> {{ dialogProduct.spcl_cnd }}</p>
        <p><strong>기타 유의사항:</strong> {{ dialogProduct.etc_note }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import { useCounterStore } from '@/stores/counter';
import axios from 'axios';

const store = useCounterStore();
const URL = `${store.API_URL}/banks/recommendation_by_survey/`;
const data = ref(null);
const userGoal = ref(null);
const savings = ref([]);
const deposits = ref([]);
const dialogProduct = ref({});
const dialog = ref(false);


const error = ref(null);
const usertype = ref(null);
const savingType = ref('');
const meaningoutType = ref('');
const portfolioType = ref('');
const selectedTerm = ref(6); 
const depositAmount = ref(0)
const savingAmount = ref(0)


const setTerm = (term) => {
  selectedTerm.value = term;
};

const openDialog = (product) => {
  dialogProduct.value = product;
  dialog.value = true;
};

const getRecommendation = async () => {
  try {
    const response = await axios.get(URL, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    });
    data.value = response.data;
    savings.value = response.data.savings || [];
    deposits.value = response.data.deposits || [];
    usertype.value = response.data.user_type;
    savingType.value = (usertype.value === 'EIG' || usertype.value === 'EIV' || usertype.value === 'FIG' || usertype.value === 'FIV') ? '자유로운 소비를 추구하는 고객님의 성향에 맞는 자유적립식 상품을 추천했어요.' : '계획적인 소비를 추구하는 고객님의 성향에 맞는 정액적립식 상품을 추천했어요.';
    meaningoutType.value = (usertype.value === 'EIG' || usertype.value === 'FIG' || usertype.value === 'ERG' || usertype.value === 'FRG') ? '합리적인 소비에 맞는 합리적 재테크를 위해 높은 이율의 상품을 추천했어요.' : '재테크와 함께 우리 사회도 챙길 수 있는 상품을 추천했어요.';
    portfolioType.value = (usertype.value === 'EIG' || usertype.value === 'EIV' || usertype.value === 'ERG' || usertype.value === 'ERV') ? '이미 꼼꼼하게 돈 관리를 하고 있는 고객님, 적금 비율을 높여 보는 것도 추천해요!' : '재테크에 대해 하나씩 배우고 있는 고객님, 예금 중심으로 시작해 적금 비율을 조금씩 높여 가는 것을 추천해요!';

  } catch (err) {
    console.error('Error fetching data:', err);
    if (err.response) {
      error.value = `Error: ${err.response.status} - ${err.response.statusText}`;
    } else if (err.request) {
      error.value = 'No response received from server';
    } else {
      error.value = `Request error: ${err.message}`;
    }
  }
}

const getUsergoal = async () => {
  try {
    const response = await axios.get(`${store.API_URL}/api/v1/accounts/user-goal-view/`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    userGoal.value = response.data;
    savingAmount.value = response.data.saving_amount
    depositAmount.value = response.data.deposit_amount
  } catch(err) {
    console.error(error)
  }
}


const calculateSimpleInterestMaturity = (principal, annualRate, months) => {

  const monthlyRate = annualRate / 100 / 12;

  return principal + (principal * monthlyRate * months) * (1-0.154);
};

const calculateSavingMaturity = (monthlySaving, annualRate, months) => {
  const monthlyRate = annualRate / 100 / 12;
  let total = 0;
  for (let i = 0; i < months; i++) {
    total += monthlySaving;
    total += total * monthlyRate * (1-0.154); 
  }
  return total;
};

const enrichProductsWithExpectedReturns = () => {
  if (!data.value) return;
  data.value[selectedTerm.value + '개월'].deposits.forEach(product => {
    const interestRate = product.options.find(option => option.save_trm === selectedTerm.value.toString()).intr_rate;
    product.expectedMaturity = calculateSimpleInterestMaturity(depositAmount.value, interestRate, selectedTerm.value);
  });
  data.value[selectedTerm.value + '개월'].savings.forEach(product => {
    const interestRate = product.options.find(option => option.save_trm === selectedTerm.value.toString()).intr_rate;
    product.expectedMaturity = calculateSavingMaturity(savingAmount.value, interestRate, selectedTerm.value);
  });
};

const formatCurrency = (value) => {
  return Number(value).toLocaleString(undefined, { minimumFractionDigits: 0, maximumFractionDigits: 0 });
};


watch(selectedTerm, () => {
  getRecommendation().then(() => {
    enrichProductsWithExpectedReturns();
  });
}, { immediate: true });
onMounted(() => {
  getRecommendation().then(() => {
    getUsergoal().then(() => {
      enrichProductsWithExpectedReturns(); 
    });
  });
});
</script>


<style scoped>
.container {
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);

}
.tabs button {
  padding: 10px 20px;
  margin: 5px;
  border: none;
  background-color: #f1f1f1;
  cursor: pointer;
}
.tabs button.active-tab {
  background-color: rgb(83, 204, 168);
  color: white;
}
.row {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}
.column {
  flex: 1;
  padding: 10px;
}
.column.full {
  flex: 100%;
}
ul {
  list-style: none;
  padding: 0;
}
li {
  padding: 10px;
  width : 300px;
  background-color: white;
  border: 1px solid #ddd;
  margin-top: 5px;
  cursor: pointer;
  /* box-shadow: 0 4px 8px rgba(0,0,0,0.1); */

}
.modal {
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0,0,0,0.4);
}
.modal-content {
  background-color: #fefefe;
  margin: 15% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
}
.close {
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}
.close:hover,
.close:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
}
</style>



