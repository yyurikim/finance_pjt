<template>
    <div>
        <h1>로그아웃, 회원탈퇴 확인 페이지</h1>

    <form @submit.prevent="store.logOut" class="form">
        <button type="submit" class="submit-button">로그아웃</button>
    </form>

    <form @submit.prevent="store.deleteUser" class="form">
        <button type="submit" class="submit-button">회원탈퇴</button>
    </form>

    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()


</script>
<style scoped>
.submit-button {
    margin-top: 20px;
    padding: 10px 20px;
    background-color: #f44336; /* Red */
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

.form {
    margin-bottom: 20px;
}

</style>