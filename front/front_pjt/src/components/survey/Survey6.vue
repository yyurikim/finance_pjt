<template>
<div>
    <div>
        <h1>Q6. 난 분명 매달 똑같은 월급을 받는데😭</h1>
    </div>
    
    <div>
        <div 
            class="button-like" 
            @click="answer(true)" 
            tabindex="0" 
            @keypress.enter="answer(true)"
            role="button"
            >
            <h3>늘 가난하지만 유독 가난한 달이 있다</h3>
        </div>
        <div 
            class="button-like" 
            @click="answer(false)" 
            tabindex="0" 
            @keypress.enter="answer(false)"
            role="button"
        >
        <h3>늘 보통으로 가난하다</h3>
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
