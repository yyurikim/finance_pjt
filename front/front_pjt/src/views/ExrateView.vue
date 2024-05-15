<template>
  <h1>Exchange Rates</h1>
  <br>
  <div>
    <h2>현재 환율 정보 ({{ search_date }} 기준)</h2>
    <ul>
      <div v-for="rate in rates" :key="rate.id">
        <li v-if="rate.cur_unit !== 'KRW' && rate.cur_unit !== 'IDR(100)' && rate.cur_unit !== 'JPY(100)'">
          {{ rate.cur_nm }}: {{ rate.deal_bas_r }}
        </li>
        <li v-else-if="rate.cur_unit == 'IDR(100)' || rate.cur_unit == 'JPY(100)'">
          {{ rate.cur_nm }}: {{ rate.deal_bas_r }} (100)
        </li>
      </div>
    </ul>
  </div>
    <hr>
    <h2>환율 계산기</h2>
    <select v-model="selectedCurrency">
      <option disabled value="">Please select one</option>
      <option v-for="rate in rates" :key="rate.id" :value="rate.cur_unit">
        {{ rate.cur_nm }}
      </option>
    </select>
    <input type="number" v-model.number="amountKRW" placeholder="Enter amount in KRW">
    <button @click="calculateExchange">Calculate</button>
    <div v-if="displayExchangeAmount">
    {{ amountKRW }} KRW is {{ displayExchangeAmount }} in {{ selectedCurrency }}
  </div></template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';


const rates = ref([]);
const search_date = ref('');
const selectedCurrency = ref(''); 
const amountKRW = ref(0);
const exchangeAmount = ref(null);

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

const calculateExchange = () => {
  const selectedRate = rates.value.find(rate => rate.cur_unit === selectedCurrency.value);
  
  if (selectedRate && amountKRW.value) {
    // deal_bas_r이 문자열인 경우 숫자로 변환
    const rateValue = parseFloat(selectedRate.deal_bas_r);
    exchangeAmount.value = amountKRW.value / rateValue;
  } else {
    // 선택한 환율이 없거나 입력 금액이 없는 경우
    exchangeAmount.value = null;  // 명시적으로 null 설정
  }
};

const displayExchangeAmount = computed(() => {
  return exchangeAmount.value ? exchangeAmount.value.toFixed(2) : null;
});


onMounted(fetchRates);
</script>
