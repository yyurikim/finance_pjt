<template>
  <div class="home">
    <div class="nav-container">
      <nav>
        <ul>
          <li><RouterLink :to="{ name: 'profile' }">Profile</RouterLink></li>
          <li><RouterLink :to="{ name: 'signup' }">Signup</RouterLink></li>
          <li><RouterLink :to="{ name: 'login' }">Login</RouterLink></li>
          <li><RouterLink :to="{ name: 'test' }">Test</RouterLink></li>
          <li><RouterLink :to="{ name: 'changepwd' }">Changepwd</RouterLink></li>
          <li><RouterLink :to="{ name: 'changeinfo' }">Changeinfo</RouterLink></li>
        </ul>
      </nav>
    </div>
    
    <section class="title">
      <div class="centered-container">
        <div class="centered">
          <h1>어쩌구저쩌구</h1>
          <h1>우리의 서비스</h1>
          <v-btn :to="{ name: 'survey' }" class="btn" outlined>
            <template v-slot:prepend>
            </template>
            나의 소비성향 확인하기😁
            <template v-slot:append>
            </template>
          </v-btn>
        </div>
      </div>
    </section>

    <div class="test">
      <section class="link">
        <RouterLink :to="{ name: 'profile' }" class="link-item"><img src="@/assets/icon/profile-icon.png" alt="Profile" />
        <span>Profile</span></RouterLink>
        <RouterLink :to="{ name: 'map' }" class="link-item"><img src="@/assets/icon/map-icon.png" alt="BankMap" />
        <span>Map</span></RouterLink>
        <RouterLink :to="{ name: 'exchange_rate' }" class="link-item"><img src="@/assets/icon/exchange-icon.png" alt="ExchangeRate" />
        <span>Exchange</span></RouterLink>
        <RouterLink :to="{ name: 'community' }" class="link-item"><img src="@/assets/icon/community-icon.png" alt="Community" />
        <span>Community</span></RouterLink>
      </section>

      <section class="content-section">
        <div class="service1">
          <h3>서비스1</h3>
          <p>전세계 00개국 환율을 한 눈에 확인하기 어쩌구!! 계산해보세요 어쩌구</p>
        </div>

        <div class="service2">
          <h3>서비스2</h3>
          <p>모든 은행의 예적금 상품 비교를 한 눈에 어쩌구</p>
        </div>
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
</script>

<style scoped>
.home {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.nav-container {
  position: absolute;
  top: 0;
  width: 100%;
  z-index: 3; /* Ensure the nav is on top */
  display: flex;
  justify-content: center; /* Center the nav container */
  margin-top: 3rem;
  font-size: 1.2rem;
}

.nav-container nav ul {
  list-style: none;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  padding: 0;
  margin: 0;
}

.nav-container nav ul li {
  margin: 0 1rem;
}

.nav-container nav ul li a {
  color: white; /* Change the color to white */
  text-decoration: none;
}

.title, .link, .content-section, .carousel {
  width: 100%;
}

.title {
  background: url('@/assets/busan.png') no-repeat center center;
  background-size: cover;
  text-align: center;
  padding: 2rem;
  color: white;
  position: relative;
  height: 60vh; /* Adjust the height as needed */
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
  padding: 1rem 0;
}

.link-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-decoration: none;
}

.link img {
  width: 50px;
  height: 50px;
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
</style>
