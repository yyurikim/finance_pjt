<template>
<div>
    <h1>검색 기능</h1>
    <div class="map-container elevation-7 mb-15"> 
        <!-- div로 묶으니까 지도 안 나옴 나중에 위치 수정 필 -->
        <v-btn 
            variant="text"
            color="#75D9B1"
            @click="clickCurrentSearch"
            class="current-search-btn"
            rounded="xl"
            elevation="8"
            size="large"
        > 
            <v-icon class="me-1">mdi-reload</v-icon>
            현 위치에서 검색
        </v-btn>
        <div ref="mapContainer" style="width:100%; height: 100%;"></div>
        <div class="controll">
            <button class="zoom-control zoom-in" @click="zoomIn">
                <span class="material-icons">zoom_in</span>
            </button>
            <button class="zoom-control zoom-out" @click="zoomOut">
                <span class="material-icons">zoom_out</span>
            </button>
        </div>
        
    </div>
</div>
</template>
    
    
<script setup>
import { ref, onMounted } from 'vue';

const VITE_KAKAO_MAP_KEY = import.meta.env.VITE_KAKAO_MAP_KEY;
const mapContainer = ref(null);

let map = null;  // map 인스턴스를 저장할 변수를 상위 스코프에 선언

const loadKakaoMap = (container) => {
    const script = document.createElement('script');
    script.src = `https://dapi.kakao.com/v2/maps/sdk.js?appkey=${VITE_KAKAO_MAP_KEY}&autoload=false`;
    document.head.appendChild(script);

    script.onload = () => {
        if (window.kakao && window.kakao.maps) {
            window.kakao.maps.load(() => {
                const options = {
                    center: new window.kakao.maps.LatLng(35.09612803874684, 128.8536006613105),
                    level: 3,
                    maxLevel: 5,
                };
                map = new window.kakao.maps.Map(container, options); // map 변수에 인스턴스 저장
            });
        } else {
            console.error("Kakao Maps API 로드 실패");
        }
    };
};

// 현위치 버튼을 누르면, 지도 중심이 현위치로 이동하도록
const setCenter = function (lat, lon) {
    const moveLatLon = new kakao.maps.LatLng(lat, lon);
    map.setLevel(6)
    // 지도 중심을 이동 시킵니다
    map.setCenter(moveLatLon)

}

function zoomIn() {
    if (map) {
        var level = map.getLevel();
        map.setLevel(level - 1);  // 메서드 이름을 올바르게 사용
    }
}

function zoomOut() {
    if (map) {
        var level = map.getLevel();
        map.setLevel(level + 1);
    }
}

onMounted(() => {
    if (mapContainer.value) {
        loadKakaoMap(mapContainer.value);
    }
});
</script>

<style scoped>
button{
    border: 1px solid transparent;
    padding: 6px;
    margin: 1px;
    background-color: #efefefdd;
    border-radius: 6px;
    &:hover {
        background-color: #ddd;
        border-color: #ddd;
        cursor: pointer;
    }
    &:active {
        background-color: #aaa;
        border-color: #aaa;
    }
}
.map-container {
  position: relative;
  width: 100%; /* 너비 조정 */
  height: 400px; /* 높이 지정 */
  margin: auto; /* 중앙 정렬 */
  margin: 2rem;
}

.zoom-control {
  position: absolute;
  top: 10px; /* 상단에서 10px 떨어진 위치 */
  background: white;
  border: none;
  cursor: pointer;
  padding: 8px;
  border-radius: 4px;
  z-index: 1000; /* 다른 요소 위에 표시되도록 z-index 설정 */
}

.zoom-control.zoom-in {
  right: 60px; /* 줌 인 버튼 위치 */
}

.zoom-control.zoom-out {
  right: 10px; /* 줌 아웃 버튼 위치 */
}
.current-search-btn{
    position: absolute;
    z-index: 1000;
}
</style>
