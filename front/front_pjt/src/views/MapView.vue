<template>
  <div>
  <h3>kakao map 검색</h3>
    
    <div class="a">
      <div class="map-container">
        <div class="controll">
      <button @click="zoom(-1)">
        <span class="material-icons"> zoom_in </span>
      </button>
      <button @click="zoom(1)">
        <span class="material-icons"> zoom_out </span>
      </button>
    </div>
        <KakaoMap ref="kmap" class="kmap" :options="mapOption" /> 
        <div class="searchbox">
            <div>
                <v-text-field
              label="검색어를 입력하세요"
              variant="underlined"
              v-model="search.keyword"
              @keyup.enter="serachPlace"
            ></v-text-field>
            </div>
            <div class="results">
            <v-card
              class="mx-auto"
              max-width="300"
              v-for="rs in search.results"
              :key="rs.id"
              @click="showPlace(rs)"
            >
              <v-list>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>{{ rs.place_name }}</v-list-item-title>
                    <v-list-item-subtitle>{{ rs.address_name }}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-card>
          </div>
        </div>

        <div class="search-controls">
            <v-select variant="outlined" color="#75D9B1" :items="doName" label="광역시/도" v-model="selectDo"></v-select>
            <v-select variant="outlined" color="#75D9B1" :items="cityName" label="시/군/구" v-model="selectCity"></v-select>
            <v-select variant="outlined" color="#75D9B1" :items="bankList" label="은행" v-model="selectBank"></v-select>
            <v-btn variant="flat" color="#75D9B1" size="medium" @click="Search">
            <v-icon class="me-1 mt-1">mdi-map-search-outline</v-icon></v-btn>
        </div>
    
      </div>
  </div>
        
        
    </div>
</template>
  
<script>
import KakaoMap from "@/components/map/NewMap.vue";
import MarkerHandler from "@/components/map/marker-handler";
import { ref, computed, watch } from 'vue'

export default {
components: {
  KakaoMap,
},
setup(){
  const selectBank = ref('전체보기')
const selectDo = ref('광역시/도')
const selectCity = ref('시/군/구')

const bankList = ['SC제일은행', '경남은행', '광주은행', '국민은행', '기업은행', '농협은행', '대구은행', '부산은행', '수협은행', '신한은행', '외환은행', '우리은행', '전북은행', '제주은행', '하나은행', '한국산업은행', '한국스탠다드차타드은행', '한국시티은행'];
const doName = ref(['강원도', '경기도', '경상남도', '경상북도', '광주광역시', '대구광역시', '대전광역시', '부산광역시', '서울특별시', '울산광역시', '인천시', '전라남도', '전라북도', '제주특별자치도', '충청남도', '충청북도'])

const cityName = ref([])
const citiesByRegion = {
      강원도: ["강릉시","동해시","삼척시","속초시","원주시","춘천시","태백시","고성군","양구군","양양군","영월군","인제군","정선군","철원군","평창군","홍천군","화천군","횡성군"],
      경기도: ["고양시","과천시","광명시","광주시","구리시","군포시","김포시","남양주시","동두천시","부천시","성남시","수원시","시흥시","안산시","안성시","안양시","양주시","오산시","용인시","의왕시","의정부시","이천시","파주시","평택시","포천시","하남시","화성시","가평군","양평군","여주군","연천군"],
      경상남도: ["거제시", "김해시", "마산시", "밀양시", "사천시", "양산시", "진주시", "진해시", "창원시", "통영시", "거창군", "고성군", "남해군", "산청군", "의령군", "창녕군", "하동군", "함안군", "함양군", "합천군"],
      경상북도: ["경산시","경주시","구미시","김천시","문경시","상주시","안동시","영주시","영천시","포항시","고령군","군위군","봉화군","성주군","영덕군","영양군","예천군","울릉군","울진군","의성군","청도군","청송군","칠곡군"],
      광주광역시: ["광산구", "남구", "동구", "북구", "서구"],
      대구광역시: ["남구", "달서구", "동구", "북구", "서구", "수성구", "중구", "달성군"],
      대전광역시: ["대덕구", "동구", "서구", "유성구", "중구"],
      부산광역시: ["강서구","금정구","남구","동구","동래구","부산진구","북구","사상구","사하구","서구","수영구","연제구","영도구","중구","해운대구","기장군"],
      서울특별시:["강남구","강동구","강북구","강서구","관악구","광진구","구로구","금천구","노원구","도봉구","동대문구","동작구","마포구","서대문구","서초구","성동구","성북구","송파구","양천구","영등포구","용산구","은평구","종로구","중구","중랑구"],
      울산광역시: ["남구","동구","북구","중구","울주군"],
      인천시: ["계양구","남구","남동구", "동구","부평구","서구","연수구","중구","강화군","옹진군"],
      전라남도: ["광양시","나주시","목포시", "순천시","여수시","강진군","고흥군","곡성군","구례군","담양군","무안군","보성군","신안군","영광군","영암군","완도군","장성군","장흥군","진도군","함평군","해남군","화순군"],
      전라북도: ["군산시", "김제시", "남원시", "익산시", "전주시", "정읍시", "고창군", "무주군", "부안군", "순창군", "완주군", "임실군", "장수군", "진안군"],
      제주특별자치도: ["서귀포시","제주시","남제주군","북제주군"],
      충청남도: ["천안시", "공주시", "보령시", "아산시", "서산시", "논산시", "계룡시", "당진시", "금산군", "부여군", "서천군", "청양군", "홍성군", "예산군", "태안군"],
      충청북도: ["제천시","청주시","충주시","괴산군","단양군","보은군","영동군","옥천군","음성군","증평군","진천군","청원군"],
      // 이하 생략
    };

    watch(selectDo, (newValue) => {
      if (newValue) {
        cityName.value = citiesByRegion[newValue] || [];
      }
    });

    return {
      selectBank, selectDo, selectCity, bankList, doName, cityName
    };

},
data() {
  return {
    mapOption: {
      center: {
        lat: 35.09612803874684, 
        lng: 128.8536006613105,
      },
      level: 6,
    },
    search: {
      keyword: null,
      pgn: null,
      results: [],
    },
  };
},
mounted() {
  const vueKakoMap = this.$refs.kmap;

  this.markers = new MarkerHandler(vueKakoMap, {
    markerClicked: (e) => {
      // console.log("[clicked ]", e);
      this.showOnMap(e);
    },
  });
},
methods: {
  serachPlace(e) {
      console.log(e.target.value);
      const keyword = e.target.value.trim();
      if (keyword.length === 0) return;
      const ps = new window.kakao.maps.services.Places();
      ps.keywordSearch(keyword, (data, status, pgn) => {
        console.log(data)
        console.log(status)
        console.log(pgn)
      this.search.keyword = keyword;
      this.search.pgn = pgn;
      this.search.results = data;
    });
      
  },
  zoom(delta) {
    const level = Math.max(3, this.mapOption.level + delta);
    this.mapOption.level = level;
    console.log("zoom", this.mapOption.level);
  },
  showOnMap(bank) {
    this.activeBank = bank;
    this.mapOption.center = {
      lat: bank.lat,
      lng: bank.lng,
    };
  },
  showPlace(place) {
      this.mapOption.center = {
      lat: place.y,
      lng: place.x,
    };
    this.markers.add(this.search.results, (result) => {
      console.log("[result]", result);
      return { lat: result.y, lng: result.x };
    });
  }
},
};


// 키워드를 계산된 속성으로 결합
const keyword = computed(() => {
  let parts = [];
  if (selectDo.value !== '광역시/도') parts.push(selectDo.value);
  if (selectCity.value !== '시/군/구') parts.push(selectCity.value);
  if (selectBank.value !== '전체보기') parts.push(selectBank.value);
  return parts.join(' ');
});
</script>

<style lang="scss">
button {
  border: 1px solid transparent;
  padding: 6px;
  background-color: #efefefdd;
  border-radius: 6px;
  &:hover {
    background-color: #ddd; /* 추가된 호버 효과 배경 색상 */
    cursor: pointer;
  }
}
.a{
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh; /* 화면 전체 높이 */
  width: 100%; /* 화면 전체 너비 */
  position: relative;
}
.map-container {
  display: flex;
  justify-content: center; /* 가로 중앙 정렬 */
  align-items: center;     /* 세로 중앙 정렬 */
  height: 75vh;           /* 화면 전체 높이 */
  margin: 50px;
  position: relative;
}

.kmap {
  flex: 1;                 /* 맵 컨테이너 공간 비율 설정 */
  height: 100%;            /* 맵 컨테이너 높이를 부모에 맞춤 */
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.4);
  // max-height: 600px; // 지도 위치 고정하면 다른 게 풀림
}

.searchbox {
  width: 300px; /* 고정 너비 지정 */
  margin-left: 20px;
  flex: 0.5;                 /* 검색 박스도 맵과 동일한 공간 비율을 가짐 */
  display: flex;
  flex-direction: column;
  height: 100%;            /* 부모 컨테이너의 높이를 상속받아 사용 */
}

.results {
  flex-grow: 1;            /* 결과 리스트가 가용 공간을 모두 채우도록 설정 */
  overflow-y: auto;        /* 필요 시 스크롤 생성 */
}

.search-controls {
  display: flex;
  align-items: center;    /* 세로 중앙 정렬 */
  justify-content: space-between; /* 요소들 사이에 균등 간격 */
  position: absolute;
  bottom: -20px;
  right: 310px;
  z-index: 1001;
  padding: 7px;
  border-radius: 8px; /* 경계선 둥글게 처리 */
}

.v-select, .v-btn {
  margin-right: 9px; /* 오른쪽 마진 추가 */
}

.v-btn {
  min-width: 3px; /* 버튼의 최소 너비 조정 */
  padding: 3px 5px; /* 패딩 조정 */
}

.v-select {
  flex-grow: 1; /* 각 선택 필드가 공간을 균등하게 차지하도록 설정 */
  width: 120px; /* 최대 너비 설정 */
}
.controll {
  position: absolute;
  top: 10px;
  left: 10px;
  z-index: 1001; /* 지도 위에 보이도록 z-index 설정 */
}

.addr {
  margin-bottom: 10px;
  color: #4c4b4b;
}
</style>