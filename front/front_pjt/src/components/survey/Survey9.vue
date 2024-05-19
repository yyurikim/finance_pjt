<template>
<div>
    <div>
        <h1>Q9. 새 물건을 사고 싶은 당신, 장바구니에 담아 놨던 두 가지 물건이 떠오릅니다🙄</h1>
    </div>
    
    <div>
        <div 
            class="button-like" 
            @click="answer(true)" 
            tabindex="0" 
            @keypress.enter="answer(true)"
            role="button"
            >
            <h3>더 비싸긴 하지만..</h3>
            <h3>비슷한 디자인이라면 사회적 기업에서 만든 물건을 구매한다</h3>
        </div>
        <div 
            class="button-like" 
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
