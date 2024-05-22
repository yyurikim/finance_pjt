<template>
  <div v-if="userJoined && userLiked" class="container">
    <div class="card">
      <h3>내가 가입한 상품</h3>
      <br>
      <div class="list">
        <div 
          class="list-item" 
          v-for="product in userJoined.savings" 
          :key="product.id">
          <div class="list-item-content">
            <div class="list-item-title">{{ product.fin_prdt_nm }}</div>
            <div class="list-item-subtitle">{{ product.kor_co_nm }}</div>
          </div>
        </div>
        <div 
          class="list-item" 
          v-for="product in userJoined.deposits" 
          :key="product.id">
          <div class="list-item-content">
            <div class="list-item-title">{{ product.fin_prdt_nm }}</div>
            <div class="list-item-subtitle">{{ product.kor_co_nm }}</div>
          </div>
        </div>
      </div>
    </div>

    <div class="card">
      <h3>내가 관심있는 상품</h3>
      <br>
      <div class="list">
        <div 
          class="list-item" 
          v-for="product in userLiked.savings" 
          :key="product.id">
          <div class="list-item-content">
            <div class="list-item-title">{{ product.fin_prdt_nm }}</div>
            <div class="list-item-subtitle">{{ product.kor_co_nm }}</div>
          </div>
        </div>
        <div 
          class="list-item" 
          v-for="product in userLiked.deposits" 
          :key="product.id">
          <div class="list-item-content">
            <div class="list-item-title">{{ product.fin_prdt_nm }}</div>
            <div class="list-item-subtitle">{{ product.kor_co_nm }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>



<script setup>
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import axios from 'axios'

const userJoined = ref({})
const userLiked = ref({})
const store = useCounterStore()

const getUserJoined = async () => {
  try {
    const response = await axios.get(`${store.API_URL}/banks/user-joined`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    userJoined.value = response.data
    console.log(userJoined.value)
  } catch (error) {
    console.error(error)
  }
}

const getUserLiked = async () => {
  try {
    const response = await axios.get(`${store.API_URL}/banks/user-liked`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    userLiked.value = response.data
  } catch (error) {
    console.error(error)
  }
}

onMounted(() => {
  getUserJoined()
  getUserLiked()
})
</script>

<style scoped>
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.card {
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
  width:260px;
}

.card h2 {
  margin-bottom: 20px;
}

.list {
  list-style: none;
  padding: 0;
}


.list-item:hover {
  background-color: #f0f0f0;
}

.list-item-content {
  display: flex;
  flex-direction: column;
}

.list-item-title {
  font-weight: bold;
}

.list-item-subtitle {
  color: #666;
}
</style>
