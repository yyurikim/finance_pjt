<!-- <template>
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
</template> -->

<template>
  <div v-if="user" class="profile-card-container">
    <!-- 이미지 표시 -->
    <div class="avatar-container">
      <img :src="`${store.API_URL}${user.profile_img}`" width="300px"><img>
    </div>
    
    <!-- 사용자 정보 -->
    <div class="user-info">
      <p>나의 목표: {{ user.my_goal }}</p>
      <p>현재 가진 자산: {{ user.deposit_amount }}원</p>
      <p>매달 저축할 금액: {{ user.saving_amount }}원</p>
      <h3><strong>{{ user.username }}</strong>님의 소비 성향은</h3>
      <h3><strong>{{ user.user_type }}</strong>입니다.</h3>
    </div>

    <!-- 버튼 -->
    <button>설명 보기</button>
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
    console.log("User data fetched:", user.value); // 데이터 확인
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

.profile-card-container {
  max-width: 400px;
  height: 500px;
  margin: 20px auto;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  border-radius: 10px;
}

.avatar-container {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.user-avatar {
  width: 250px;
  height: 250px;
  border-radius: 50%; /* 원형 이미지 */
}

.user-info {
  text-align: center;
}

.user-info p {
  margin: 10px 0;
}

button {
  display: block;
  width: 100%;
  padding: 10px;
  background-color: #007BFF;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
}

button:hover {
  background-color: #0056b3;
}

</style>