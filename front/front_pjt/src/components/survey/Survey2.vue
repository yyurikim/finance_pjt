<template>
<div>
    <div>
        <h1>Q2. 오프라인에서 당신에게 찰떡인 옷을 보았습니다 🫡</h1>
    </div>

    <div>
        <div 
            class="button-like" 
            @click="answer(true)" 
            tabindex="0" 
            @keypress.enter="answer(true)"
            role="button"
            >
            <h3>온라인에서 가격을 비교해 싼 곳에서 구매한다</h3>
            <h4>ex) 무신사</h4>
        </div>
        <div 
        class="button-like" 
        @click="answer(false)" 
        tabindex="0" 
        @keypress.enter="answer(false)"
        role="button"
        >
        <h3>지금이 바로 기회! 바로 사버린다</h3>
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
router.push('/survey/3'); // 다음 질문으로 이동
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
