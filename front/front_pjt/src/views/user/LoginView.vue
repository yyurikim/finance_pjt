<template>
    <div class="container">
        <div class="title-block">
        <h1>로그인</h1>
            <p class="login-prompt">
                아직 Mingle의 회원이 아니신가요?
                <RouterLink to="/signup" class="login-link">회원가입</RouterLink>
            </p>
        </div>
        <form @submit.prevent="logIn" class="form">
            <div class="form-group">
                <label for="username">아이디</label>
                <input v-model.trim="username" id="username" placeholder="아이디를 입력해주세요." />
            </div>
            <div class="form-group">
                <label for="password">비밀번호</label>
                <input v-model.trim="password" id="password" type="password" placeholder="비밀번호를 입력해주세요." />
                <p>최소 8자부터 최대 16자까지 입력하세요.</p>
            </div>

            <!-- <div class="button-group">
                <button type="button">카카오계정으로 로그인</button>
                <button type="button">카카오계정으로 로그인</button>
            </div> -->
            <button type="submit" class="submit-button">로그인</button>
        </form>
    </div>
</template>

<script setup>
import {ref} from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'

const username = ref(null)
const password = ref(null)
const store = useCounterStore()

const logIn = function(){
  const payload = {
    username: username.value,
    password : password.value
  }
  store.logIn(payload)
}
</script>


<style scoped>
.container {
display: flex;
flex-direction: column;
align-items: center;
padding: 24px;
margin-top:30px;
}

.title-block {
text-align: center;
}

.form {
width: 100%;
max-width: 800px; /* 최대 너비 설정 */
margin-top: 16px;
display: flex;
flex-direction: column; /* 모든 자식 요소를 세로로 정렬 */
align-items: center;
}

.form-group {
  width: 100%; /* 부모 요소의 너비를 전부 채우도록 설정 */
  margin-bottom: 24px;
}

.form-group label {
  display: block;
  font-weight: bold;
  margin-bottom: 8px;
}

.form-group input {
  width: 100%; /* input 요소 너비 최대로 설정 */
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.form-group p {
  color: #718096;
  font-size: 12px;
}

.submit-button {
  width: calc(100% - 16px); /* 입력 필드와 같은 너비를 갖도록 조정 */
  background-color: rgb(83, 204, 168);
  color: white;
  margin-left: 15px; /*중앙 정렬 안 맞는 거 */
  padding: 12px;
  border-radius: 4px;
  border: none;
  cursor: pointer;
  text-align: center;
}

.login-prompt {
  font-size: 16px;
}

.login-link {
  margin-left: 10px;
  color: blue;
  text-decoration: underline;
}
</style>
