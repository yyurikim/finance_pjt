<template>
  <div class="home">
    <div class="nav-container">
      <nav>
        <ul v-if="isLogin">
          <li class="bar"><RouterLink :to="{ name: 'profile' }">프로필</RouterLink></li>
          <li class="bar"><RouterLink :to="{ name: 'changepwd' }">비밀번호 변경</RouterLink></li>
          <li class="bar"><RouterLink :to="{ name: 'changeinfo' }">회원정보 수정</RouterLink></li>
          <li class="bar">
            <form @submit.prevent="logOut">
              <button type="submit" class="nav-button">로그아웃</button>
            </form>
          </li>
          <li class="bar">
            <form @submit.prevent="deleteUser">
              <button type="submit" class="nav-button">회원탈퇴</button>
            </form>
          </li>
        </ul>
        <ul v-else>
          <li class="bar"><RouterLink :to="{ name: 'signup' }">회원가입</RouterLink></li>
          <li class="bar"><RouterLink :to="{ name: 'login' }">로그인</RouterLink></li>
        </ul>
      </nav>
    </div>

    <section class="title">
      <div class="centered-container">
        <div class="centered">
          <h1>어쩌구저쩌구</h1>
          <h1>우리의 서비스</h1>
          <!-- <v-btn :to="{ name: 'survey' }" class="btn" outlined>
            <template v-slot:prepend></template>
            <h4>나의 소비성향 확인하기😁</h4>
            <template v-slot:append></template>
          </v-btn> -->
        </div>
      </div>
    </section>

    <div class="test">
      <section class="link">
        <RouterLink :to="{ name: 'profile' }" class="link-item"><img src="@/assets/icon/profile-icon.png" alt="Profile" />
        <span>프로필</span></RouterLink>
        <RouterLink :to="{ name: 'map' }" class="link-item"><img src="@/assets/icon/map-icon.png" alt="BankMap" />
        <span>근처 은행</span></RouterLink>
        <RouterLink :to="{ name: 'bank' }" class="link-item"><img src="@/assets/icon/bankbook.png" alt="Bank" />
        <span>예적금 상품</span></RouterLink>
        <RouterLink :to="{ name: 'exchange_rate' }" class="link-item"><img src="@/assets/icon/exchange-icon.png" alt="ExchangeRate" />
        <span>환율</span></RouterLink>
        <RouterLink :to="{ name: 'community' }" class="link-item"><img src="@/assets/icon/community-icon.png" alt="Community" />
        <span>커뮤니티</span></RouterLink>
        <RouterLink :to="{ name: 'survey' }" class="link-item"><img src="@/assets/icon/mang1.png" alt="Community" />
        <span>테스트 바로가기👽</span></RouterLink>
      </section>

      <section class="content-section">
        <img src="@/assets/test1.png" alt="" class="img1">
      </section>

      <section>
        <div class="carousel">
          <Carousel />
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
import Carousel from '@/components/main/Carousel.vue';
import { useCounterStore } from '@/stores/counter';
import { onMounted } from 'vue';

const store = useCounterStore();
const { isLogin, logOut, deleteUser } = store;

onMounted(() => {
  // Perform any setup if needed
});
</script>

<style scoped>
.home {
  width: 80%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.nav-container {
  position: absolute;
  top: 0;
  width: 78%;
  z-index: 3; /* Ensure the nav is on top */
  display: flex;
  justify-content: center; /* Center the nav container */
  margin-top: 3rem;
  font-size: 1.2rem;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2)
}

.nav-container nav ul {
  list-style: none;
  display: flex;
  justify-content: center; /* Center the nav items */
  padding: 0;
  margin: 0;
}

.nav-container nav ul li {
  margin: 0 1.6rem;
  margin-top: 8px;
}

.bar {
  margin: 0 1.5rem; /* Adjust the margin to align items */
}
.nav-button{
  color: white;
  margin-top: -7px;
}
.nav-container nav ul li a,
.nav-container nav ul li .nav-link {
  color: white; /* Change the color to white */
  text-decoration: none;
  background: none;
  border: none;
  font: inherit;
  cursor: pointer;
  padding: 0;
}

.title, .link, .content-section, .carousel {
  width: 100%;
}

.title {
  /* background: url('@/assets/test.jpg') no-repeat center center; */
  background: url('@/assets/busan.png') no-repeat center center;
  background-size: cover;
  text-align: center;
  padding: 2rem;
  margin-top: 25px;
  color: white;
  position: relative;
  height: 70vh; /* Adjust the height as needed */
  /* width: 130vh; */
  z-index: 1; /* Ensure title section is above other content */
}

.centered-container {
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  height: 100%; /* Full height of the section */
  top: 0; /* Adjust the top margin to leave space for nav */
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 2; /* Ensure centered content is above nav and title background */
}

.centered {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center; /* Center the text horizontally */
}

.test {
  background: white;
  width: 97%;
  margin: 0 auto;
  margin-top: -50px; /* Adjust this value as needed to pull it up */
  z-index: 2; /* Ensure it stays above other content */
  position: relative;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Optional: Add some shadow for effect */
  border-radius: 10px; /* Optional: Add rounded corners */
}

.btn {
  color: black;
  background-color: #fff;
  text-align: center;
  padding: 0.5rem 0.4rem;
  border-radius: 0.2rem;
  font-size: 0.9rem;
  margin-top: 1rem;
  display: inline-block;
  text-decoration: none;
}

.link {
  display: flex;
  justify-content: space-around;
  padding: 2.5rem 0;
}

.link-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-decoration: none;
}

.link img {
  width: 70px;
  height: 70px;
}

.link span {
  margin-top: -1rem;
  color: black; /* Adjust the color as needed */
  font-size: 0.9rem; /* Adjust the font size as needed */
  text-align: center;
}

.content-section {
  width: 100%;
  margin: 50px 0;
}

.service1 {
  padding: 1rem;
  text-align: center;
  margin: 1rem 0;
}

.service2 {
  background-color: #f0f0f0;
  padding: 1rem;
  text-align: center;
  margin: 1rem 0;
}

.carousel {
  text-align: center;
  margin-top: 4rem;
}

img {
  margin: 30px;
}

.img1 {
  width: 100%;
  margin: 0px;
}
</style>
