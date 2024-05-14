<template>
<div class="container">
    <div class="title-block">
    <h1>회원가입</h1>
    <p class="login-prompt">
        맹꽁이의 회원이신가요?
        <RouterLink to="/login" class="login-link">로그인</RouterLink>
    </p>
    </div>
    <form class="form">
    <div class="form-group">
        <label for="username">이름</label>
        <input id="username" placeholder="이름을 입력해주세요." />
        <p>최소 2자부터 최대 10자까지 입력하세요.</p>
    </div>
    <div class="form-group">
        <label for="email">이메일</label>
        <input id="email" placeholder="ex) maengkkong@gmail.com" />
    </div>
    <div class="form-group">
        <label for="password">비밀번호</label>
        <input id="password" type="password" placeholder="비밀번호를 입력해주세요." />
        <p>최소 8자부터 최대 16자까지 입력하세요.</p>
    </div>
    <div class="form-group">
        <label for="password-confirm">비밀번호 확인</label>
        <input id="password-confirm" type="password" placeholder="비밀번호를 다시 입력해주세요." />
        <p>최소 8자부터 최대 16자까지 입력하세요.</p>
    </div>
    <!-- <div class="button-group">
        <button type="button">카카오계정으로 로그인</button>
        <button type="button">카카오계정으로 로그인</button>
    </div> -->
    <button type="submit" class="submit-button">회원가입</button>
    </form>
</div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
.container {
display: flex;
flex-direction: column;
align-items: center;
padding: 24px;
}

.title-block {
text-align: center;
}

.title-block h1 {
font-size: 32px;
font-weight: bold;
}

.title-block p {
margin-top: 8px;
color: #4a5568;
}

.form {
width: 100%;
max-width: 500px;
margin-top: 16px;
}

.form-group {
margin-bottom: 24px;
}

.form-group label {
display: block;
font-weight: bold;
margin-bottom: 8px;
}

.form-group input {
width: 100%;
padding: 8px;
border: 1px solid #ccc;
border-radius: 4px;
}

.form-group p {
color: #718096;
font-size: 12px;
}

.button-group {
display: flex;
flex-direction: column;
gap: 12px;
}

.submit-button {
width: 100%;
background-color: #4a5568;
color: white;
padding: 12px;
border-radius: 4px;
border: none;
margin-left: 10px; /*중앙 정렬 안 맞는 거 */
cursor: pointer;

}
.login-prompt {
  font-size: 16px; /* 글씨 크기 조절 */
}

.login-link {
  margin-left: 10px; /* 로그인 링크와 텍스트 사이의 간격 */
  color: blue; /* 링크 색상 */
  text-decoration: underline; /* 밑줄로 링크 표시 */
}
</style>
