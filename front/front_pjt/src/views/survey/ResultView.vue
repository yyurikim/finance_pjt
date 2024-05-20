<template>
<div>
    <h1>결과 페이지</h1>
    <p>당신의 성향은: {{ result }}</p>
</div>
</template>

<script setup>
import { ref, inject, onMounted } from 'vue';
import axios from 'axios';
import { useCounterStore } from '@/stores/counter';

const counter = useCounterStore();

// inject는 setup 함수 내에서 호출되어야 합니다
const survey = inject('survey');

const result = ref('');

if (survey) {
result.value = survey.state.result;

const sendResult = async (result) => {
    try {
    const response = await axios.post('http://127.0.0.1:8000/api/v1/accounts/update-user-type/', {
        user_type: result
    }, {
        headers: {
        Authorization: `Token ${counter.token}`
        }
    });
    console.log('User type updated:', response.data);
    } catch (error) {
    console.error('There was an error updating the user type:', error);
    }
};

onMounted(() => {
    sendResult(result.value);
});
} else {
console.error('survey is not injected');
}
</script>

<style scoped>
/* 스타일을 여기 추가하세요 */
</style>
