<template>
<div>
    <div>
        <h1>Q1. 지금! 당신의 통장 잔액을 대략적으로 알고 있나요?</h1>
        <h4>*예적금을 제외한 생활비 통장</h4>
    </div>

    <div>
        <div 
            class="button-like" 
            @click="answer(true)" 
            tabindex="0" 
            @keypress.enter="answer(true)"
            role="button"
            >
            <h3>대충 얼마 정도 있는지 알지~</h3>
            <h3>알고 있다</h3>
        </div>
        <div 
        class="button-like" 
        @click="answer(false)" 
        tabindex="0" 
        @keypress.enter="answer(false)"
        role="button"
        >
        <h3>얼마 있더라..?</h3>
        <h3>자세히 모른다</h3>
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
router.push('/survey/2'); // 다음 질문으로 이동
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
