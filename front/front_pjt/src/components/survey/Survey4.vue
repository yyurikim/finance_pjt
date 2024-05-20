<template>
<div>
    <div>
        <h1>Q4. 방학을 맞아 해외로 떠난 당신! 마음에 쏙 드는 물건 발견했습니다 😎</h1>
    </div>
    
    <div>
        <div 
            class="button-like" 
            @click="answer(true)" 
            tabindex="0" 
            @keypress.enter="answer(true)"
            role="button"
            >
            <h3>예산을 넘긴 했지만 해외까지 왔는 걸?</h3>
            <h3>이건 사야 해!</h3>
        </div>
        <div 
            class="button-like" 
            @click="answer(false)" 
            tabindex="0" 
            @keypress.enter="answer(false)"
            role="button"
        >
        <h3>충동소비 그게 뭐지?</h3>
        <h3>관전에 기름칠이나 해줘</h3>
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
router.push('/survey/5'); // 다음 질문으로 이동
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
