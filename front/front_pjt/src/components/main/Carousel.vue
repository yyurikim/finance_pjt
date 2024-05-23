<template>
  <div class="carousel-container">
    <div class="carousel">
      <div 
        v-for="(image, index) in images" 
        :key="index" 
        class="carousel-item"
        @mouseover="handleMouseOver(index)"
        @mouseleave="handleMouseLeave"
      >
        <a :href="image.link" target="_blank" rel="noopener noreferrer">
          <img :src="image.src" :alt="image.alt" class="carousel-image" />
        </a>
      </div>
    </div>
  </div>
</template>


<script setup>
import { ref } from 'vue';

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

const activeIndex = ref(null);

const handleMouseOver = (index) => {
  activeIndex.value = index;
};

const handleMouseLeave = () => {
  activeIndex.value = null;
};
</script>


<style scoped>
.carousel-container {
  display: flex;
  justify-content: center;
  width: 100%;
  overflow: hidden;
  padding: 20px;
  box-sizing: border-box;
}

.carousel {
  display: flex;
  align-items: center;
  justify-content: center; /* Add this line to center items horizontally */
  width: 100%;
  position: relative;
  margin-bottom: 4rem;
}

.carousel-item {
  position: relative;
  transition: transform 0.3s ease, z-index 0.3s ease;
  margin-right: -30px; /* Negative margin to overlap items */
}

.carousel-item:hover {
  z-index: 10; /* Bring hovered item to the front */
}

.carousel-image {
  width: 100px;
  height: 100px;
  cursor: pointer;
  object-fit: contain;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  border-radius: 12px;
  transition: transform 0.3s ease;
}

.carousel-item:hover .carousel-image {
  transform: scale(1.2); /* Scale up the image on hover */
  margin-right: 0; /* Remove margin on hover */
}
</style>
