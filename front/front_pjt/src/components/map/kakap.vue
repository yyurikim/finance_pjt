<template>
    <div ref="map"></div>
  </template>
  
  <script>
  let kakao = window.kakao;
  export default {
    props: ["options"],
    data() {
      return {
        mapInstance: null,
      };
    },
    mounted() {
      console.log(this.options);
      kakao = kakao || window.kakao;
      console.log(this.$refs.map);
  
      var container = this.$refs.map;
  
      const { center, level } = this.options;
  
      this.mapInstance = new kakao.maps.Map(container, {
        center: new kakao.maps.LatLng(center.lat, center.lng),
        level,
      }); //지도 생성 및 객체 리턴
    },
    watch: {
      "options.level"(cur, prev) {
        console.log(`[LEVEL CHANGED] ${prev} => ${cur}`);
        this.mapInstance.setLevel(cur);
      },
      "options.center"(cur, prev) {
        console.log(`[NEW CENTER]`, cur.lat, cur.lng);
        this.mapInstance.setCenter(new kakao.maps.LatLng(cur.lat, cur.lng));
      }
    },
  };
  </script>
  
  <style>
  .kmap {
    height: 600px;
  }
  </style>