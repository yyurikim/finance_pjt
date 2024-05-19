<template>
<div>
    <div>
        <h1>Q3. 방을 둘러보던 당신, 뜯지도 않은 새 물건을 발견했습니다 🤔</h1>
    </div>
    
    <div>
        <div 
            class="button-like" 
            @click="answer(true)" 
            tabindex="0" 
            @keypress.enter="answer(true)"
            role="button"
            >
            <h3>분명 내가 사긴 했는데...</h3>
            <h3>언제 어디서 산 거지?</h3>
        </div>
        <div 
            class="button-like" 
            @click="answer(false)" 
            tabindex="0" 
            @keypress.enter="answer(false)"
            role="button"
        >
        <h3>이거 몇달 전 집 앞 가게에서 샀는데!</h3>
        <h3>이제 찾았네~</h3>
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
router.push('/survey/4'); // 다음 질문으로 이동
};
</script>

<style scoped>
.button-like {
  display: inline-block;
  padding: 10px 20px;
  margin: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: #f0f0f0;
  cursor: pointer;
  text-align: center;
  user-select: none;
}
.button-like:focus {
  outline: none;
  box-shadow: 0 0 3px 2px rgba(21, 156, 228, 0.4);
}
</style>
