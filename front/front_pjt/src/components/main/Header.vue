<template>
  <header :class="{ hidden: isHomeView, whiteBackground: !isHomeView }">
    <nav>
      <RouterLink :to="{ name: 'home' }" class="logo">Home</RouterLink>
      <ul>
        <li><RouterLink :to="{ name: 'profile' }">Profile</RouterLink></li>
        <li><RouterLink :to="{ name: 'bank' }">Bank</RouterLink></li>
        <li><RouterLink :to="{ name: 'map' }">BankMap</RouterLink></li>
        <li><RouterLink :to="{ name: 'exchange_rate' }">ExchangeRate</RouterLink></li>
        <li><RouterLink :to="{ name: 'community' }">Community</RouterLink></li>
        <!-- <li><RouterLink :to="{ name: 'test' }">Test</RouterLink></li> -->
        <li><RouterLink :to="{ name: 'changepwd' }">Changepwd</RouterLink></li>
        <li><RouterLink :to="{ name: 'changeinfo' }">Changeinfo</RouterLink></li>
      </ul>
      <p v-if="user" class="hellouser">{{ user.username }}님 반가워요!</p>
      <RouterLink :to="{ name: 'profile' }">
      <img v-if="user" :src="profileImage" width="50px" height="50px"><img>
      </RouterLink>
    </nav>
  </header>
</template>

<script setup>
const props = defineProps({
  isHomeView: {
    type: Boolean,
    required: true,
  },
});

import { ref, onMounted, computed } from 'vue';
import { useCounterStore } from '@/stores/counter';
import axios from 'axios';
import defaultProfileImg from '@/assets/user/user.png';
const store = useCounterStore();
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

onMounted(fetchUserProfile)
</script>

<style scoped>
header {
  padding: 1rem;
  transition: background-color 0.3s, box-shadow 0.3s;
  box-shadow: 0 4px 6px -6px rgba(0, 0, 0, 0.2); /* Shadow only at the bottom */
}

header.hidden {
  display: none;
}

header.whiteBackground {
  background-color: #fff;
  height: 3.5rem;
  box-shadow: 0 4px 6px -6px rgba(0, 0, 0, 0.5); /* Shadow only at the bottom */
}

nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

nav .logo {
  font-size: 1.5rem;
  font-weight: bold;
  color: #333;
  text-decoration: none;
}

nav ul {
  list-style: none;
  display: flex;
  justify-content: center; /* Center align the navigation links */
  padding: 0;
  margin: 0;
  flex-grow: 1; /* Allow the ul to grow and center the items */
}

nav ul li {
  margin: 0 1rem;
}

nav ul li a {
  color: #333;
  text-decoration: none;
  font-size: 1rem;
  padding: 0.5rem;
  transition: color 0.3s, background-color 0.3s;
}

nav ul li a:hover {
  color: #007bff;
  background-color: #f0f0f0;
  border-radius: 0.3rem;
}

nav img {
  vertical-align: middle; /* 이미지를 텍스트와 중간 정렬 */
  margin-top: -15px; /* 이미지를 약간 위로 올림 */
  margin-left: 10px;
  border-radius: 50%;
}

.hellouser {
  margin-bottom: 0px
}

@media (max-width: 768px) {
  nav ul {
    flex-direction: column;
    align-items: center;
  }

  nav ul li {
    margin: 0.5rem 0;
  }
}
</style>
