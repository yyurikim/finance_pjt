<template>
    <div style="width: 100%; height: 400px;"> <!-- 지도가 표시될 영역에 크기 설정 -->
      <KakaoMap :lat="coordinate.lat" :lng="coordinate.lng" :level="3">
        <KakaoMapMarker :lat="coordinate.lat" :lng="coordinate.lng"></KakaoMapMarker>
      </KakaoMap>
    </div>
  </template>
  
  <script setup>
  import { KakaoMap, KakaoMapMarker } from 'vue3-kakao-maps';
  const coordinate = {
      lat: 35.09612803874684,
      lng: 128.8536006613105 
  };
  </script>  