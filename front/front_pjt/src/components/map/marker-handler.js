class MarkerHandler {
  constructor(mapInstance, options = {}) {
    this.mapInstance = mapInstance;
    this.markers = [];
    this.overlays = [];
    this.markerClicked = options.markerClicked || function () {};
  }

  addMarker(position, title) {
    const marker = new window.kakao.maps.Marker({
      position,
      map: this.mapInstance,
    });

    // 제목이 15자를 넘을 경우 줄바꿈 추가
    const formattedTitle = title.length > 15 ? title.substring(0, 15) + '\n' + title.substring(15) : title;
    const content = `
      <div class="customoverlay">
        <div class="customoverlay-content">
          <span class="title">${formattedTitle}</span>
        </div>
        <div class="customoverlay-arrow"></div>
      </div>`;

    const customOverlay = new window.kakao.maps.CustomOverlay({
      position,
      content,
      yAnchor: 2.1, // yAnchor를 조정하여 오버레이를 위로 이동시킵니다.
    });

    // 마커 클릭 이벤트를 통해 오버레이를 표시합니다
    window.kakao.maps.event.addListener(marker, 'click', () => {
      // 모든 오버레이를 닫습니다
      this.overlays.forEach(overlay => overlay.setMap(null));
      // 클릭한 마커의 오버레이만 엽니다
      customOverlay.setMap(this.mapInstance);
    });

    this.markers.push(marker);
    this.overlays.push(customOverlay);
  }

  clearMarkers() {
    this.markers.forEach(marker => marker.setMap(null));
    this.overlays.forEach(overlay => overlay.setMap(null));
    this.markers = [];
    this.overlays = [];
  }
}

export default MarkerHandler;
