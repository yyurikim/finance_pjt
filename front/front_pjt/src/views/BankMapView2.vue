<template>
<div>
    <div class="d-flex align-center my-5">
    <div class="map-container">
        <Map2 :selectedDo="selectDo" :selectedCity="selectCity" :selectedBank="selectBank" ref="mapRef"/>
    </div>
    <div class="search-controls">
        <v-select
            variant="outlined"
            color="#75D9B1"
            :items="doName"
            label="광역시/도"
            v-model="selectDo"
            class="mr-2"
        ></v-select>

        <v-select
            variant="outlined"
            color="#75D9B1"
            :items="cityName"
            label="시/군/구"
            v-model="selectCity"
            class="mx-2"
        ></v-select>

        <v-select
            variant="outlined"
            color="#75D9B1"
            :items="bankList"
            label="은행"
            v-model="selectBank"
            class="mx-2"
        ></v-select>

        <v-btn
            variant="flat"
            color="#75D9B1"
            size="x-large"
            @click="Search"
            class="pr-7 ml-2 mb-6"
        >
            <v-icon class="me-1 mt-1">mdi-map-search-outline</v-icon>
            찾기
        </v-btn>
    </div>
    </div>
</div>
</template>
    

<script setup>
import { ref, onMounted, computed, watch } from 'vue'
import Map2 from '@/components/Map2.vue'
import axios from 'axios'

const selectBank = ref('전체보기')
const selectDo = ref('광역시/도')
const selectCity = ref('시/군/구')

const bankList = ['SC제일은행', '경남은행', '광주은행', '국민은행', '기업은행', '농협은행', '대구은행', '부산은행', '수협은행', '신한은행', '외환은행', '우리은행', '전북은행', '제주은행', '하나은행', '한국산업은행', '한국스탠다드차타드은행', '한국시티은행'];
const doName = ref(['강원도', '경기도', '경상남도', '경상북도', '광주광역시', '대구광역시', '대전광역시', '부산광역시', '서울특별시', '울산광역시', '인천시', '전라남도', '전라북도', '제주특별자치도', '충청남도', '충청북도'])

const cityName = ref()
const gangwon = ["강릉시","동해시","삼척시","속초시","원주시","춘천시","태백시","고성군","양구군","양양군","영월군","인제군","정선군","철원군","평창군","홍천군","화천군","횡성군"];
const gyeonggi = ["고양시","과천시","광명시","광주시","구리시","군포시","김포시","남양주시","동두천시","부천시","성남시","수원시","시흥시","안산시","안성시","안양시","양주시","오산시","용인시","의왕시","의정부시","이천시","파주시","평택시","포천시","하남시","화성시","가평군","양평군","여주군","연천군"];
const gyeongsangnam = ["거제시", "김해시", "마산시", "밀양시", "사천시", "양산시", "진주시", "진해시", "창원시", "통영시", "거창군", "고성군", "남해군", "산청군", "의령군", "창녕군", "하동군", "함안군", "함양군", "합천군"];
const gyeongsangbuk = ["경산시","경주시","구미시","김천시","문경시","상주시","안동시","영주시","영천시","포항시","고령군","군위군","봉화군","성주군","영덕군","영양군","예천군","울릉군","울진군","의성군","청도군","청송군","칠곡군"];
const gwangju = ["광산구", "남구", "동구", "북구", "서구"];
const daegu = ["남구", "달서구", "동구", "북구", "서구", "수성구", "중구", "달성군"];
const daejeon = ["대덕구", "동구", "서구", "유성구", "중구"];
const busan = ["강서구","금정구","남구","동구","동래구","부산진구","북구","사상구","사하구","서구","수영구","연제구","영도구","중구","해운대구","기장군"];
const seoul = ["강남구","강동구","강북구","강서구","관악구","광진구","구로구","금천구","노원구","도봉구","동대문구","동작구","마포구","서대문구","서초구","성동구","성북구","송파구","양천구","영등포구","용산구","은평구","종로구","중구","중랑구"];
const ulsan = ["남구","동구","북구","중구","울주군"];
const incheon = ["계양구","남구","남동구", "동구","부평구","서구","연수구","중구","강화군","옹진군"];
const jeonnam = ["광양시","나주시","목포시", "순천시","여수시","강진군","고흥군","곡성군","구례군","담양군","무안군","보성군","신안군","영광군","영암군","완도군","장성군","장흥군","진도군","함평군","해남군","화순군"];
const jeonbuk = ["군산시", "김제시", "남원시", "익산시", "전주시", "정읍시", "고창군", "무주군", "부안군", "순창군", "완주군", "임실군", "장수군", "진안군"];
const jeju = ["서귀포시","제주시","남제주군","북제주군"];
const chungbuk = ["제천시","청주시","충주시","괴산군","단양군","보은군","영동군","옥천군","음성군","증평군","진천군","청원군"];

watch(selectDo, () => {
    selectCity.value = null
  if (selectDo.value == "강원도") {
    cityName.value = gangwon;
  } else if (selectDo.value == "경기도") {
    cityName.value = gyeonggi;
  } else if (selectDo.value == "경상남도") {
    cityName.value = gyeongsangnam;
  } else if (selectDo.value == "경상북도") {
    cityName.value = gyeongsangbuk;
  } else if (selectDo.value == "광주광역시") {
    cityName.value = gwangju;
  } else if (selectDo.value == "대구광역시") {
    cityName.value = daegu;
  } else if (selectDo.value == "대전광역시") {
    cityName.value = daejeon;
  } else if (selectDo.value == "부산광역시") {
    cityName.value = busan;
  } else if (selectDo.value == "서울특별시") {
    cityName.value = seoul;
  } else if (selectDo.value == "울산광역시") {
    cityName.value = ulsan;
  } else if (selectDo.value == "인천시") {
    cityName.value = incheon;
  } else if (selectDo.value == "전라남도") {
    cityName.value = jeonnam;
  } else if (selectDo.value == "전라북도") {
    cityName.value = jeonbuk;
  } else if (selectDo.value == "제주특별자치도") {
    cityName.value = jeju;
  } else if (selectDo.value == "충청남도") {
    cityName.value = chungnam;
  } else if (selectDo.value == "충청북도") {
    cityName.value = chungbuk;
  }
})

// 키워드를 계산된 속성으로 결합
const keyword = computed(() => {
  let parts = [];
  if (selectDo.value !== '광역시/도') parts.push(selectDo.value);
  if (selectCity.value !== '시/군/구') parts.push(selectCity.value);
  if (selectBank.value !== '전체보기') parts.push(selectBank.value);
  return parts.join(' ');
});




</script>

<style scoped>
.search-controls {
  flex: 35%; /* 검색 컨트롤이 전체 공간의 35%를 차지하도록 설정 */
  display: flex;
  flex-direction: column; /* 세로 정렬 */
  justify-content: center; /* 중앙 정렬 */
  margin-right: 25px; /* 지도와의 간격 조정 */
  padding-left: 5rem;
  padding-right: 2rem;
}

.d-flex {
  display: flex;
  align-items: center;
  width: 100%; /* 부모 컨테이너 전체 너비를 사용하도록 설정 */
}

.map-container { /* 지도 컨테이너에 적용할 클래스 */
  flex: 65%; /* 지도가 전체 공간의 65%를 차지하도록 설정 */
  height: 400px; /* 높이 설정, 필요에 따라 조정 */
}

</style>
