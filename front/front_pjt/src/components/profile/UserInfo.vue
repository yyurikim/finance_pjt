<template>
    <div v-if="user">
      {{ user.profile_img }}
      <v-card class="mx-auto my-5 pa-5" max-width="400" height="500">
            <v-card-title class="d-flex align-center justify-center">
                <v-avatar size="300" class="mr-3">
                    <img :src="user.profile_img" alt="User Avatar" />
                  </v-avatar>
            </v-card-title>
            <v-card-text class="text-center">
              <div>
                <p>나의 목표 : {{ user.my_goal }}</p>
                <p>현재 가진 자산 : {{ user.deposit_amount }}원</p>
                <p>매달 저축할 금액 : {{ user.saving_amount }}원</p>
                <br>
                <h3><strong>{{ user.username }}</strong>님의 소비 성향은</h3>
                <h3><strong>{{ user.user_type }}</strong>입니다.</h3>
              </div>
              <button>설명 보기</button>
            </v-card-text>
        </v-card>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import axios from 'axios'

const store = useCounterStore()
const user = ref(null)

const fetchUserProfile = async () => {
  try {
    const response = await axios.get(`${store.API_URL}/api/v1/accounts/profile/`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    user.value = response.data
  } catch (error) {
    console.error('Error fetching user profile:', error)
  }
}

onMounted(fetchUserProfile)
</script>

<style scoped>

.v-card {
  max-width: 400px;
  margin: auto;
}
</style>