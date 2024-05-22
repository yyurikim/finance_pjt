<template>
  <div v-if="user" class="profile-card-container">
    <div class="avatar-container">
      <img :src="profileImage" width="250px"><img>
    </div>
    
    <div class="user-info">
      <p>나의 목표: {{ user.my_goal }}</p>
      <p>현재 가진 자산: {{ formatNumber(user.deposit_amount) }}원</p>
      <p>매달 저축할 금액: {{ formatNumber(user.saving_amount) }}원</p>
      <h3><strong>{{ user.username }}</strong>님의 소비 성향은</h3>
      <h3><strong>{{ user.user_type }}</strong>입니다.</h3>
    </div>

    <!-- 버튼 -->
    <button>설명 보기</button>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useCounterStore } from '@/stores/counter'
import axios from 'axios'
import defaultProfileImg from '@/assets/user/user.png';


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

const profileImage = computed(() => {
  return user.value && user.value.profile_img
    ? `${store.API_URL}${user.value.profile_img}`
    : defaultProfileImg;
});

const formatNumber = (number) => {
  return number.toLocaleString()
}

onMounted(fetchUserProfile)
</script>

<style scoped>

.profile-card-container {
  width: 300px;
  /* margin-top: 80px; */
  padding: 20px;
  /* box-shadow: 0 4px 8px rgba(0,0,0,0.1); */
  border-radius: 10px;
  background-color: #fff; /* 배경색 추가 */
  margin-right: 30px;
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
  width: 50%;
  padding: 10px;
  background-color: rgb(83, 204, 168);
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  margin-top: 20px; /* 버튼 상단 여백 추가 */
  margin-left: 25%; /* 버튼 중앙 정렬 */
}

button:hover {
  background-color: rgb(33, 182, 137);
}

img {
  border-radius: 60%;
}


</style>