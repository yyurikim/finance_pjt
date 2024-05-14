<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const exrate_url = `${store.API_URL}/exrates`
const selectedDeal = ref()







</script>


<template>
  <div>
    <h1>환율 계산기 만드는중</h1>
  </div>
  <div>
    <label for="fromCurrency">From:</label>
    <select v-model="fromCurrency">
      <option v-for="country in countries" :key="country.code" :value="country.code">
        {{ country.name }}
      </option>
    </select>
  </div>
  <div>
    <label for="toCurrency">To:</label>
    <select v-model="toCurrency">
      <option v-for="country in countries" :key="country.code" :value="country.code">
        {{ country.name }}
      </option>
    </select>
  </div>
  <div>
    <label for="amount">Amount:</label>
    <input type="number" v-model="amount" />
  </div>
  <button @click="calculateExchangeRate">Calculate</button>
  <div v-if="result !== null">
    <h2>Result: {{ result }}</h2>
  </div>
</template>


<style scoped>

</style>