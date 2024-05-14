<template>
    <div class="container">
        <div class="title-block">
        <h1>비밀번호 변경</h1>
            <p class="login-prompt">
               새로운 비밀번호를 입력해주세요.
            </p>
        </div>
        <form class="form">
            <div class="form-group">
                <label for="password">현재 비밀번호</label>
                <input id="password" placeholder="현재 비밀번호를 입력해주세요." />
            </div>
            <div class="form-group">
                <label for="newpassword">새 비밀번호</label>
                <input id="newpassword" type="password" placeholder="새 비밀번호를 입력해주세요." />
                <p>최소 8자부터 최대 16자까지 입력하세요.</p>
            </div>
            <div class="form-group">
                <label for="newpassword">새 비밀번호 확인</label>
                <input id="newpassword" type="password" placeholder="새 비밀번호를 다시 입력해주세요." />
            </div>

            <!-- <div class="button-group">
                <button type="button">카카오계정으로 로그인</button>
                <button type="button">카카오계정으로 로그인</button>
            </div> -->
            <button type="submit" class="submit-button">비밀번호 변경</button>
        </form>
    </div>
</template>

<script setup>
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

.form {
width: 100%;
max-width: 500px; /* 최대 너비 설정 */
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
  background-color: #4a5568;
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
</style>