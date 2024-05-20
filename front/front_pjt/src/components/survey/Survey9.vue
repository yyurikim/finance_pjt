<template>
  <div class="container">
    <img src="@/assets/test/Q9.png" alt="Q9" class="Q">
    <div class="buttons-container">
      <div 
        class="button" 
        @click="answer(true)" 
        tabindex="0" 
        @keypress.enter="answer(true)"
        role="button"
      >
      <h3>더 비싸긴 하지만 비슷한 디자인이라면</h3>
      <h3>사회적 기업에서 만든 물건을 구매한다</h3>
      </div>
      <div 
        class="button" 
        @click="answer(false)" 
        tabindex="0" 
        @keypress.enter="answer(false)"
        role="button"
      >
      <h3>조금이라도 더 저렴한 물건을 구매한다</h3>
      </div>
    </div>
  </div>
</template>

<script>
import { inject } from 'vue';
import { useRouter } from 'vue-router';

export default {
  setup() {
    const { addAnswer, calculateResult } = inject('survey');
    const router = useRouter();
    
    return {
      answer(response) {
        addAnswer(response);
        calculateResult();
        router.push('/survey/result'); // 다음 질문으로 이동
      },
    };
  },
};
</script>

<style scoped>
.container {
  width: 550px;
  height: 875px;
  margin: 10px auto;
  position: relative;
}

.container img {
  width: 100%;
  vertical-align: middle;
}

.buttons-container {
  position: absolute;
  top: 300px; /* 버튼들의 상단 위치 */
  left: 50%; /* 중앙 정렬을 위해 left 50% 설정 */
  transform: translateX(-50%); /* 중앙 정렬을 위해 translateX 사용 */
  display: flex;
  flex-direction: column;
  align-items: center;
}

.button {
  width: 400px;
  height: 75px;
  background-color: #fff;
  border-radius: 4px;
  cursor: pointer;
  text-align: center;
  user-select: none;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 그림자 설정 */
  margin-bottom: 20px; /* 버튼 간격 */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.button:focus {
  outline: none;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 포커스 시 그림자 설정 */
}
</style>
