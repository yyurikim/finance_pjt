<template>
    <v-app>
      <v-container>
        <v-row>
          <v-col cols="12">
            <h2>환율 계산기</h2>
            <p>기준일자: {{ search_date }}</p>
          </v-col>
        </v-row>
      <v-row align="center">
        <v-col cols="12" md="6">
          <v-combobox
            id="from-currency"
            label="From"
            v-model="fromCurrency"
            :items="currencies"
            item-text="cur_nm"
            item-value="cur_unit"
            outlined
          ></v-combobox>
        </v-col>
        <v-col cols="12" md="6">
          <v-text-field
            v-model.number="amountFrom"
            label="금액 입력"
            type="number"
            placeholder="Enter amount"
            outlined
            dense
          ></v-text-field>
        </v-col>
      </v-row>
        <v-col>
            <v-btn color="primary" @click="convertCurrency" :disabled="!fromCurrency || !toCurrency">Convert</v-btn>
          </v-col>
      <!-- <input type="number" v-model.number="amountFrom" placeholder="Enter amount">
      <button @click="convertCurrency">Convert</button>
    </div> -->
    <v-row align="center">
        <v-col cols="12" md="6">
          <v-combobox
            id="from-currency"
            label="To"
            v-model="toCurrency"
            :items="currencies"
            item-text="cur_nm"
            item-value="cur_unit"
            outlined
          ></v-combobox>
        </v-col>
        <v-col cols="12" md="6">
          <v-text-field
            v-model="displayExchangeAmount"
            label="결과"
            readonly
            outlined
            dense
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row v-if="isDateMismatch">
        <v-col>
          <v-alert type="warning" dense>
            가장 최근 영업일의 환율 정보입니다.
          </v-alert>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
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
const currencies = ref([]);

const fetchRates = async () => {
  try {
    const response = await axios.get('http://localhost:8000/exrates/');
    rates.value = response.data.exchange_rates;
    search_date.value = response.data.search_date;
    currencies.value = response.data.exchange_rates.map(rate => rate.cur_nm);
    console.log(response.data);
  } catch (error) {
    console.error("There was an error!", error);
  }
};

watch(fromCurrency, (newValue) => {
  if (newValue !== '한국 원') {
    toCurrency.value = '한국 원';
  }
});

// toCurrency가 변경될 때 fromCurrency를 KRW로 설정
watch(toCurrency, (newValue) => {
  if (newValue !== '한국 원') {
    fromCurrency.value = '한국 원';
  }
});

const convertCurrency = () => {
  const today = new Date().toISOString().split('T')[0];
  if (search_date.value!== today) {
    isDateMismatch.value = true;
  } else {
    isDateMismatch.value = false;
  }

  const rateFrom = rates.value.find(rate => rate.cur_nm === fromCurrency.value)?.deal_bas_r || 1;
  const rateTo = rates.value.find(rate => rate.cur_nm === toCurrency.value)?.deal_bas_r || 1;
  if (rateFrom && rateTo && amountFrom.value) {
    exchangeAmount.value = (amountFrom.value / rateTo) * rateFrom;

    if (fromCurrency.value === '일본 옌' || fromCurrency.value === '인도네시아 루피아') {
      exchangeAmount.value /= 100;
    }
    if (toCurrency.value === '일본 옌' || toCurrency.value === '인도네시아 루피아') {
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