<template>
    <div class="container">
      <img src="@/assets/test/Q6.png" alt="Q6" class="Q">
      <div class="buttons-container">
        <div 
          class="button" 
          @click="answer(true)" 
          tabindex="0" 
          @keypress.enter="answer(true)"
          role="button"
        >
          <h5>늘 가난하지만 유독 가난한 달이 있다</h5>
        </div>
        <div 
          class="button" 
          @click="answer(false)" 
          tabindex="0" 
          @keypress.enter="answer(false)"
          role="button"
        >
          <h5>늘 보통으로 가난하다</h5>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { inject } from 'vue';
  import { useRouter } from 'vue-router';
  
  const { addAnswer } = inject('survey');
  const router = useRouter();
  
  const answer = (response) => {
    addAnswer(response);
    router.push('/survey/7'); // 다음 질문으로 이동
  };
  </script>
  
  <style scoped>
  .container {
    width: 400px;
    margin: 10px auto;
    position: relative;
  }
  
  .container img {
    width: 100%;
    vertical-align: middle;
  }
  
  .buttons-container {
    position: absolute;
    top: 216px; /* 버튼들의 상단 위치 */
    left: 50%; /* 중앙 정렬을 위해 left 50% 설정 */
    transform: translateX(-50%); /* 중앙 정렬을 위해 translateX 사용 */
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .button {
    width: 250px;
    height: 60px;
    background-color: #fff;
    border-radius: 4px;
    cursor: pointer;
    text-align: center;
    user-select: none;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 그림자 설정 */
    margin-bottom: 10px; /* 버튼 간격 */
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    font-weight: bold;
  }
  
  .button:focus {
    outline: none;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 포커스 시 그림자 설정 */
  }
  </style>