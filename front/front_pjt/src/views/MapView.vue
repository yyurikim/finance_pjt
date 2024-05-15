<template>
    <div>
      <h3>kakao map 검색</h3>
      <div class="controll">
        <button @click="zoom(1)">
          <span class="material-icons"> zoom_in </span>
        </button>
        <button @click="zoom(-1)">
          <span class="material-icons"> zoom_out </span>
        </button>
      </div>
      <div class="map-area">
        <div class="searchbox">
            <div>
                <input type="text" placeholder="검색어를 입력하세요" @keyup.enter="serachPlace" />
            </div>
            <div class="results">
                <div class="place" v-for="rs in search.results" :key="rs.id" @click="showPlace(rs)">
                <h4>{{ rs.place_name }}</h4>
                <div class="addr">{{ rs.address_name }}</div>
                </div>

            </div>
        </div>
  
        <KakaoMap ref="kmap" class="kmap" :options="mapOption" />
      </div>
    </div>
</template>
  
  <script>
  import KakaoMap from "@/components/map/kakap.vue";
  import api from "@/service/api";
  import MarkerHandler from "@/components/map/marker-handler";

  export default {
  components: {
    KakaoMap,
  },
  data() {
    return {
      mapOption: {
        center: {
          lat: 33.450701,
          lng: 126.570667,
        },
        level: 8,
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
</script>

<style lang="scss">
button {
  border: 1px solid transparent;
  padding: 6px;
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
.map-area {
  display: flex;
  position: relative;
  .searchbox {
    position: absolute;
    top: 0;
    left: 0;
    height: 600px;
    z-index: 10000;
    background-color: #ffffffaa;
    width: 300px;
    display: flex;
    flex-direction: column;
    .results {
      flex: 1 1 auto;
      overflow-y: auto;
      .place {
        padding: 8px;
        cursor: pointer;
        &:hover {
          background-color: rbga(240, 248, 255, 0.657);
        }
        h4 {
          margin: 0;
        }
      }
    }
  }
  // .banks {
  //   .bank {
  //     padding: 10px;
  //     border: 1px solid transparent;
  //     &:hover {
  //       background-color: aliceblue;
  //       border-color: #6a9dff;
  //       cursor: pointer;
  //     }
  //     &:active {
  //       background-color: rgb(166, 197, 224);
  //       border-color: #4471c5;
  //     }
  //     &.active {
  //       background-color: rgb(253, 229, 150);
  //       border-color: rgb(211, 173, 3);
  //     }
  //     h4 {
  //       margin: 0;
  //     }
  //   }
  // }
  .kmap {
    flex: 1 1 auto;
    .overlay-popup {
      background-color: #ffffffaa;
      box-shadow: 0 0 8px #0000004d, 0 0 1px 2px #00000022;
      max-width: 200px;
      min-width: 160px;
      h3 {
        margin: 0;
        padding: 8px;
        background-color: #ed4215;
        color: white;
        font-weight: 400;
        font-size: 16px;
      }
      .addr {
        padding: 8px;
        white-space: break-spaces;
      }
    }
  }
}
</style>