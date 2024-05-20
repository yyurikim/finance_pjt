<template>
<div>
    <div>
        <h1>Q8. 출근길에 커피를 사가려는 당신☕</h1>
    </div>
    
    <div>
        <div 
            class="button-like" 
            @click="answer(true)" 
            tabindex="0" 
            @keypress.enter="answer(true)"
            role="button"
            >
            <h3>텀블러를 사용한다</h3>
            <h3>환경 보호하고 할인도 받아야지!</h3>
        </div>
        <div 
            class="button-like" 
            @click="answer(false)" 
            tabindex="0" 
            @keypress.enter="answer(false)"
            role="button"
        >
        <h3>텀블러를 사용하면 좋은 건 알지만..</h3>
        <h3>너무 무겁고 귀찮은 걸?</h3>
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
router.push('/survey/9'); // 다음 질문으로 이동
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
