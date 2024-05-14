<template>
  <div ref="mapContainer" style="width:100%; height: 400px;"></div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

// 환경 변수를 가져옵니다.
const VITE_KAKAO_MAP_KEY = import.meta.env.VITE_KAKAO_MAP_KEY
console.log('Kakao Map API Key:', VITE_KAKAO_MAP_KEY)

const mapContainer = ref(null)

const loadKakaoMap = (container) => {
  const script = document.createElement('script')
  script.src = `https://dapi.kakao.com/v2/maps/sdk.js?appkey=${VITE_KAKAO_MAP_KEY}&autoload=false`
  document.head.appendChild(script)

  script.onload = () => {
    if (window.kakao && window.kakao.maps) {
      window.kakao.maps.load(() => {
        const options = {
          center: new window.kakao.maps.LatLng(35.09612803874684, 128.8536006613105),
          level: 3, // 지도 확대 레벨
          maxLevel: 5, // 지도 축소 제한 레벨
        }
        const mapInstance = new window.kakao.maps.Map(container, options)
      })
    } else {
      console.error("Kakao Maps API 로드 실패")
    }
  }

  script.onerror = () => {
    console.error("Kakao Maps API 스크립트 로드 실패")
    console.log('Kakao Map API Key:', VITE_KAKAO_MAP_KEY)
  }
}

onMounted(() => {
  if (mapContainer.value) {
    loadKakaoMap(mapContainer.value)
  } else {
    console.error("mapContainer가 정의되지 않음")
  }
})
</script>

<style scoped>
</style>
