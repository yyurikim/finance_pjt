<template>
    <div>
    <br>
      <h3>당신의 성향은! 🤔 </h3>
      <img :src="resultImage" alt="결과 이미지" v-if="resultImage">
    </div>
  </template>
  
  <script setup>
  import { ref, inject, onMounted, computed } from 'vue';
  import axios from 'axios';
  import { useCounterStore } from '@/stores/counter';
  
  const counter = useCounterStore();
  const survey = inject('survey');
  const result = ref('');
  
  const sendResult = async (resultValue) => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/v1/accounts/update-user-type/', {
        user_type: resultValue
      }, {
        headers: {
          Authorization: `Token ${counter.token}`
        }
      });
      console.log('User type updated:', response.data);
    } catch (error) {
      console.error('There was an error updating the user type:', error);
    }
  };
  
  const resultImage = ref('');
  
  const loadResultImage = async () => {
    if (result.value === 'ERV') {
      resultImage.value = (await import('@/assets/result/ERV.png')).default;
    } else if (result.value === 'EIV') {
      resultImage.value = (await import('@/assets/result/EIV.png')).default;
    } else if (result.value === 'FRG') {
      resultImage.value = (await import('@/assets/result/FRG.png')).default;
    } else if (result.value === 'EFG') {
      resultImage.value = (await import('@/assets/result/EFG.png')).default;
    } else if (result.value === 'EIG') {
      resultImage.value = (await import('@/assets/result/EIG.png')).default;
    } else if (result.value === 'FIG') {
      resultImage.value = (await import('@/assets/result/FIG.png')).default;
    } else if (result.value === 'FIV') {
      resultImage.value = (await import('@/assets/result/FIV.png')).default;
    } else {
      resultImage.value = (await import('@/assets/result/FRV.png')).default;
    }
  };
  
  if (survey) {
    result.value = survey.state.result;
  
    onMounted(async () => {
      await sendResult(result.value);
      await loadResultImage();
    });
  } else {
    console.error('survey is not injected');
  }
  </script>
  
  <style scoped>
  img {
    max-width: 100%;
    height: auto;
    display: block;
    margin-top:-25px;
  }
  </style>
  