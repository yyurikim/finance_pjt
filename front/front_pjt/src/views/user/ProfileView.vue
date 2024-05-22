<template>
  <div v-if="user">
    <h1 class="title">{{ user.username }}님의 프로필</h1>
    <div class="app-container">
      <div class="row">
        <div class="column col-12 md-4">
          <UserInfo />
          <UserProducts />
        </div>
        <div class="column col-12 md-8">
          <RecommendationSurvey />

        </div>
      </div>
    </div>
  </div>
</template>


  
  <script setup>
  import UserInfo from '@/components/profile/UserInfo.vue'
  import RecommendationSurvey from '@/components/bank/RecommendationSurvey.vue'
  import UserProducts from '@/components/profile/UserProducts.vue';
  import { useCounterStore } from '@/stores/counter'
  import { onMounted, ref } from 'vue';
  import axios from 'axios';
  
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
  .app-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
  }
  
  .row {
    display: flex;
    flex-wrap: wrap;
  }
  
  .column {
    padding: 10px;
    box-sizing: border-box;
  }
  
  .col-12 {
    flex: 0 0 100%;
    max-width: 100%;
  }
  
  .md-4 {
    flex: 0 0 33.333333%;
    max-width: 33.333333%;
  }
  
  .md-8 {
    flex: 0 0 66.666667%;
    max-width: 66.666667%;

  }

  .title {
    margin-top: 50px;
  }
  
  @media (max-width: 768px) {
    .md-4, .md-8 {
      flex: 0 0 100%;
      max-width: 100%;
      margin-right: 0; /* 작은 화면에서는 간격 제거 */
    }
  }
  
  .user-info-container, .recommendation-survey-container, .user-products-container {
    background: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px;
  }
  </style>