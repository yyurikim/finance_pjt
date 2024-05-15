const api = {
    harbor: {
      all(callback) {
        const harbors = [
          {
            seq: 398,
            place: "제주항 국제 여객 터미널",
            lat: 33.52456237850086,
            lng: 126.54371888191963,
          },
          {
            seq: 399,
            place: "통영항",
            lat: 34.83952733985843,
            lng: 128.42015935198992,
          },
          {
            seq: 400,
            place: "부산 국제 크루즈 터미널",
            lat: 35.07980714092641,
            lng: 129.0798233676466,
          },
        ];
        callback({ success: true, harbors });
      },
    },
  };
  
  export default api;