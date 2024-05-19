<template>
<div>
    <div>
        <h1>Q5. 월급날이 얼마 남지 않아 여유 자금이 없는 당신, 갑자기 가지고 싶었던 물건의 품절이 풀렸습니다 🫨</h1>
    </div>
    
    <div>
        <div 
            class="button-like" 
            @click="answer(true)" 
            tabindex="0" 
            @keypress.enter="answer(true)"
            role="button"
            >
            <h3>이번 한 번만!</h3>
            <h3>주변 사람이나 신용카드의 도움을 빌린다</h3>
        </div>
        <div 
            class="button-like" 
            @click="answer(false)" 
            tabindex="0" 
            @keypress.enter="answer(false)"
            role="button"
        >
        <h3>언젠가 다시 풀리겠지~</h3>
        <h3>다음을 기약한다</h3>
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
router.push('/survey/6'); // 다음 질문으로 이동
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
