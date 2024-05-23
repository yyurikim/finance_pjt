<template>
  <div class="container">
    <div class="header">
      <h1>당신의 목표는?</h1>
    </div>
    <div class="form">
      <input type="text" :value="formattedSavingAmount" @input="updateSavingAmount($event.target.value)" placeholder="매달 저축할 금액 (적금 추천용)" class="input-field">
      <input type="text" :value="formattedDepositAmount" @input="updateDepositAmount($event.target.value)" placeholder="현재 보유중인 금액 (예금 추천용)" class="input-field">
      <input type="text" v-model="my_goal" placeholder="당신의 목표 한 줄" class="input-field">
      <button class="button-like" @click="submitData">확인!</button>
    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
import { useCounterStore } from '@/stores/counter';

export default {
  setup() {
    const router = useRouter();
    const store = useCounterStore();
    const saving_amount = ref('');
    const deposit_amount = ref('');
    const my_goal = ref('');

    const formattedSavingAmount = computed(() => {
  // 값이 있고, 숫자로 변환 가능한 경우에만 포맷
  return saving_amount.value ? Number(saving_amount.value).toLocaleString() : '';
});

const formattedDepositAmount = computed(() => {
  // 값이 있고, 숫자로 변환 가능한 경우에만 포맷
  return deposit_amount.value ? Number(deposit_amount.value).toLocaleString() : '';
});

    function updateSavingAmount(value) {
      saving_amount.value = value.replace(/\D/g, '');
    }

    function updateDepositAmount(value) {
      deposit_amount.value = value.replace(/\D/g, '');
    }

    const submitData = async () => {
      const postData = {
        saving_amount: saving_amount.value,
        deposit_amount: deposit_amount.value,
        my_goal: my_goal.value
      }
      try {
        const response = await axios.post(`${store.API_URL}/api/v1/accounts/update-user-goal/`, postData, {
          headers: {
            Authorization: `Token ${store.token}`
          }
        });
        console.log(response.data);
        router.push('/survey/result');
      } catch (error) {
        console.error(error);
      }
    }

    return {
      saving_amount,
      deposit_amount,
      my_goal,
      formattedSavingAmount,
      formattedDepositAmount,
      updateSavingAmount,
      updateDepositAmount,
      submitData
    };
  }
}
</script>


<style scoped>


.container {
  width: 550px;
  height: 875px;
  margin: 10px auto;
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: center; /* 세로 축 중앙 정렬 추가 */
  background-color: white;
}


.header {
  margin-bottom: 20px;
  text-align: center;
}

.form {
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center; /* 가로 축 중앙 정렬 추가 */
}
.input-field {
  margin: 10px 0;
  padding: 10px;
  width: 250px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
  justify-content: center;
}

.button-like {
  display: inline-block;
  padding: 10px 20px;
  margin: 10px;
  border: 1px solid rgb(83, 204, 168);
  border-radius: 4px;
  background-color: rgb(83, 204, 168);
  color: white;
  cursor: pointer;
  text-align: center;
  user-select: none;
  width : 100px;
}

.button-like:hover {
  background-color: rgb(83, 204, 168);
}

.button-like:focus {
  outline: none;
  box-shadow: 0 0 3px 2px rgba(21, 156, 228, 0.4);
}
</style>