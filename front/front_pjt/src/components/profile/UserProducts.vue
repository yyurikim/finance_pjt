<template>
  <v-container v-if="userJoined && userLiked">
    <v-row>
      <v-col cols="12" md="6">
        <v-card>
          <v-card-title><strong>가입한 상품</strong></v-card-title>
          <v-card-text>
            <v-list>
              <v-list-item 
                v-for="product in userJoined.savings" 
                :key="product.id"
                @click="() => openProductDetails(product)">
                <v-list-item-content>
                  <v-list-item-title>{{ product.fin_prdt_nm }}</v-list-item-title>
                  <v-list-item-subtitle>{{ product.kor_co_nm }}</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
              <v-list-item 
                v-for="product in userJoined.deposits" 
                :key="product.id"
                @click="() => openProductDetails(product)">
                <v-list-item-content>
                  <v-list-item-title>{{ product.fin_prdt_nm }}</v-list-item-title>
                  <v-list-item-subtitle>{{ product.kor_co_nm }}</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card-text>
        </v-card>
      </v-col>

      <v-col cols="12" md="6">
        <v-card>
          <v-card-title><strong>관심있는 상품</strong></v-card-title>
          <v-card-text>
            <v-list>
              <v-list-item 
                v-for="product in userLiked.savings" 
                :key="product.id"
                @click="() => openProductDetails(product)">
                <v-list-item-content>
                  <v-list-item-title>{{ product.fin_prdt_nm }}</v-list-item-title>
                  <v-list-item-subtitle>{{ product.kor_co_nm }}</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
              <v-list-item 
                v-for="product in userLiked.deposits" 
                :key="product.id"
                @click="() => openProductDetails(product)">
                <v-list-item-content>
                  <v-list-item-title>{{ product.fin_prdt_nm }}</v-list-item-title>
                  <v-list-item-subtitle>{{ product.kor_co_nm }}</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
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
  getUserJoined();
  getUserLiked();
});

</script>

<style scoped>

</style>