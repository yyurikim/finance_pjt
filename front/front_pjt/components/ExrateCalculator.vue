<template>
  <div>
    <h2>환율 계산기</h2>
    <p>기준일자 : {{ search_date }}</p>
    <div>
      <label for="from-currency">From:</label>
      <select id="from-currency" v-model="fromCurrency">
        <option disabled value="">Select Currency</option>
        <option v-for="rate in rates" :key="rate.id" :value="rate.cur_unit">
          {{ rate.cur_nm }}
        </option>
      </select>
      <input type="number" v-model.number="amountFrom" placeholder="Enter amount">
      <button @click="convertCurrency">Convert</button>
    </div>
    <div>
      <label for="to-currency">To:</label>
      <select id="to-currency" v-model="toCurrency">
        <option disabled value="">Select Currency</option>
        <option v-for="rate in rates" :key="rate.id" :value="rate.cur_unit">
          {{ rate.cur_nm }}
        </option>
      </select>
      <span v-if="displayExchangeAmount">
        {{ displayExchangeAmount }}
      </span>
    </div>
    <div v-if="isDateMismatch">
      <p>가장 최근 영업일의 환율 정보입니다.</p>
    </div>
  </div>
    

</template>

<script setup>
import { ref, onMounted, computed, watch } from 'vue';
import axios from 'axios';


const rates = ref([]);
const search_date = ref('');
const fromCurrency = ref(''); 
const toCurrency = ref('');
const amountFrom = ref(0);
const exchangeAmount = ref(null);
const isDateMismatch = ref(false);

const fetchRates = async () => {
  try {
    const response = await axios.get('http://localhost:8000/exrates/');
    rates.value = response.data.exchange_rates;
    search_date.value = response.data.search_date;
    console.log(response.data);
  } catch (error) {
    console.error("There was an error!", error);
  }
};

watch(fromCurrency, (newValue) => {
  if (newValue !== 'KRW') {
    toCurrency.value = 'KRW';
  }
});

// toCurrency가 변경될 때 fromCurrency를 KRW로 설정
watch(toCurrency, (newValue) => {
  if (newValue !== 'KRW') {
    fromCurrency.value = 'KRW';
  }
});

const convertCurrency = () => {
  const today = new Date().toISOString().split('T')[0];
  if (search_date.value!== today) {
    isDateMismatch.value = true;
  } else {
    isDateMismatch.value = false;
  }

  const rateFrom = rates.value.find(rate => rate.cur_unit === fromCurrency.value)?.deal_bas_r || 1;
  const rateTo = rates.value.find(rate => rate.cur_unit === toCurrency.value)?.deal_bas_r || 1;
  if (rateFrom && rateTo && amountFrom.value) {
    exchangeAmount.value = (amountFrom.value / rateTo) * rateFrom;

    if (fromCurrency.value === 'JPY(100)' || fromCurrency.value === 'IDR(100)') {
      exchangeAmount.value /= 100;
    }
    if (toCurrency.value === 'JPY(100)' || toCurrency.value === 'IDR(100)') {
      exchangeAmount.value *= 100;
    }
  } else {
    // 선택한 환율이 없거나 입력 금액이 없는 경우
    exchangeAmount.value = null;  // 명시적으로 null 설정
  }
};

const displayExchangeAmount = computed(() => {
  if (exchangeAmount.value != null) {
    const formattedAmount = Number(exchangeAmount.value.toFixed(2)).toLocaleString('en-US', {
      style: 'decimal',
      maximumFractionDigits: 2
    });
    return formattedAmount;
  }
  return null;
});

onMounted(fetchRates);
</script>