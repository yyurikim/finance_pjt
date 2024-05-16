const api = {
    bank: {
      all(callback) {
        const banks = [
          {
            seq: 398,
            place: "신한은행 광안리지점",
            lat: 35.1486599431627,
            lng: 129.111059858553,
          },
          {
            seq: 399,
            place: "NH농협은행 부산남천동지점",
            lat: 35.1461084133495,
            lng: 129.111029046407,
          },
          {
            seq: 400,
            place: "우리은행 남천동지점",
            lat: 35.145602200056054,
            lng: 129.11117066365028,
          },
        ];
        callback({ success: true, banks });
      },
    },
  };
  
  export default api;