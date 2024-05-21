
<template>
  <div class="container">
    <div class="header">
      <h1>당신의 목표는?</h1>
    </div>
    <div class="form">
      <input type="number" v-model="saving_amount" placeholder="매달 저축하고 싶은 금액" class="input-field">
      <input type="number" v-model="deposit_amount" placeholder="현재 보유중인 금액" class="input-field">
      <input type="text" v-model="my_goal" placeholder="당신의 목표 한 줄" class="input-field">
      <button class="button-like" @click="submitData">Submit</button>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
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
      submitData
    };
  }
}
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  height: 100vh;
  background-color: #f7f7f7;
}

.header {
  margin-bottom: 20px;
}

.form {
  display: flex;
  flex-direction: column;
}

.input-field {
  margin: 10px 0;
  padding: 10px;
  width: 250px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
}

.button-like {
  display: inline-block;
  padding: 10px 20px;
  margin: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: #4CAF50;
  color: white;
  cursor: pointer;
  text-align: center;
  user-select: none;
  width : 100px;
}

.button-like:hover {
  background-color: #45a049;
}

.button-like:focus {
  outline: none;
  box-shadow: 0 0 3px 2px rgba(21, 156, 228, 0.4);
}
</style>


<!-- <template>
  <div>
    <div>
      <h1>당신의 목표는?</h1>
    </div>
    <div>
      <input type="number" v-model="saving_amount" placeholder="매달 저축하고 싶은 금액">
      <input type="number" v-model="deposit_amount" placeholder="현재 보유중인 금액">
      <input type="text" v-model="my_goal" placeholder="당신의 목표 한 줄">
      <button class="button-like" @click="submitData">Submit</button>
    </div>
  </div>
</template>
  
<script>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
import { useCounterStore } from '@/stores/counter';

export default {
  setup() {
    const router = useRouter();
    const store = useCounterStore();
    const saving_amount =ref(0)
    const deposit_amount =ref(0)
    const my_goal = ref('')

    const submitData = async () => {
      const postData = {
        saving_amount: saving_amount.value,
        deposit_amount: deposit_amount.value,
        my_goal: my_goal.value
      }
      try {
        const response = await axios.post(`${store.API_URL}/api/v1/accounts/update-user-goal/`, postData,{
          headers: {
            Authorization: `Token ${store.token}`
            }
        });
        console.log(response.data);
        router.push('/survey/result')
        } catch (error) {
        console.error(error);
        }
      }
      return {
        saving_amount,
        deposit_amount,
        my_goal,
        submitData
        };
      }
    }
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
  </style> -->
