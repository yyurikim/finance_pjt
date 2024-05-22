<template>
  <div class="carousel-container">
    <i class="fa-solid fa-arrow-left nav-button left" @click="prevSlide"></i>
    <Carousel
      ref="carousel"
      :items-to-show="8"
      :items-to-scroll="1"
      :autoplay-interval="3000"
      :transition-speed="500"
      :loop="true"
      :pause-on-hover="true"
    >
      <Slide v-for="(image, index) in images" :key="index">
        <a :href="image.link" target="_blank" rel="noopener noreferrer">
          <img :src="image.src" :alt="image.alt" class="carousel-image" />
        </a>
      </Slide>
    </Carousel>
    <i class="fa-solid fa-arrow-right nav-button right" @click="nextSlide"></i>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { Carousel, Slide } from 'vue3-carousel';
import 'vue3-carousel/dist/carousel.css';

const carousel = ref(null);

const images = ref([
  { src: new URL('@/assets/banklogo/bnk.png', import.meta.url).href, alt: 'BNK', link: 'https://www.busanbank.co.kr/ib20/mnu/BHP00001' },
  { src: new URL('@/assets/banklogo/daegu.png', import.meta.url).href, alt: 'Daegu', link: 'https://www.dgb.co.kr/dgb_ebz_main.jsp' },
  { src: new URL('@/assets/banklogo/gwangju.png', import.meta.url).href, alt: 'Gwangju', link: 'https://m.kjbank.com/mweb/main/' },
  { src: new URL('@/assets/banklogo/hana.png', import.meta.url).href, alt: 'Hana', link: 'https://www.kebhana.com/' },
  { src: new URL('@/assets/banklogo/ibk.png', import.meta.url).href, alt: 'IBK', link: 'https://www.ibk.co.kr/' },
  { src: new URL('@/assets/banklogo/jeju.png', import.meta.url).href, alt: 'Jeju', link: 'https://www.e-jejubank.com/JeJuBankInfo.do' },
  { src: new URL('@/assets/banklogo/kakao.png', import.meta.url).href, alt: 'Kakao', link: 'https://m.kakaobank.com/' },
  { src: new URL('@/assets/banklogo/kdb.png', import.meta.url).href, alt: 'KDB', link: 'https://www.kdb.co.kr/index.jsp' },
  { src: new URL('@/assets/banklogo/kbank.png', import.meta.url).href, alt: 'KBank', link: 'https://www.kbanknow.com/ib20/mnu/PBKMAN000000' },
  { src: new URL('@/assets/banklogo/kookmin.png', import.meta.url).href, alt: 'Kookmin', link: 'https://www.kbstar.com/' },
  { src: new URL('@/assets/banklogo/nonghyup.png', import.meta.url).href, alt: 'Nonghyup', link: 'https://www.nhbank.com/nhmn/KO_NHMN_01.do' },
  { src: new URL('@/assets/banklogo/shinhan.png', import.meta.url).href, alt: 'Shinhan', link: 'https://www.shinhan.com/index.jsp' },
  { src: new URL('@/assets/banklogo/standard.png', import.meta.url).href, alt: 'Standard', link: 'https://www.standardchartered.co.kr/np/kr/Intro.jsp' },
  { src: new URL('@/assets/banklogo/suhyup.png', import.meta.url).href, alt: 'Suhyup', link: 'https://suhyup-bank.com/' },
  { src: new URL('@/assets/banklogo/woori.png', import.meta.url).href, alt: 'Woori', link: 'https://www.wooribank.com/' },
  { src: new URL('@/assets/banklogo/toss.png', import.meta.url).href, alt: 'Toss', link: 'https://www.tossbank.com/' },
]);

const prevSlide = () => {
  carousel.value.prev();
};

const nextSlide = () => {
  carousel.value.next();
};
</script>

<style scoped>
.carousel-container {
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  overflow: hidden; /* Prevent overflow */
  padding: 20px; /* Add padding to match other sections */
}

.carousel-image {
  width: 80px; /* Adjust the size as needed */
  height: 80px; /* Adjust the size as needed */
  cursor: pointer;
  object-fit: contain; /* Ensures the image fits within the specified dimensions */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Adds a shadow to the images */
  border-radius: 12px; /* Optional: Adds rounded corners */
  margin: 0 10px; /* Adds margin between images */
}

.nav-button {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  border: none;
  font-size: 1rem;
  cursor: pointer;
  z-index: 10;
  padding: 0.3rem;
  border-radius: 50%;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  background-color: white;
}

.nav-button.left {
  left: 10px;
}

.nav-button.right {
  right: 10px;
}

.slide-transition {
  transition: transform 1s ease;
}
</style>
