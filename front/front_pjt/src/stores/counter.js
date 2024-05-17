import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const API_URL = 'http://127.0.0.1:8000'

  return {API_URL}
})
