<template>
  <div>
    <header>
      <nav>
        <RouterLink :to="{name:'test'}">Test</RouterLink> |
        <RouterLink :to="{name:'home'}">Home</RouterLink> |
        <RouterLink :to="{name:'map'}">BankMap</RouterLink> |
        <RouterLink :to="{name:'exchange_rate'}">ExchangeRate</RouterLink> |
        <RouterLink :to="{name:'community'}">Community</RouterLink> |
        <RouterLink :to="{name:'signup'}">Signup</RouterLink> |
        <RouterLink :to="{name:'login'}">Login</RouterLink> |
        <RouterLink :to="{name:'changepwd'}">Changepwd</RouterLink> |
        <RouterLink :to="{name:'bank'}">bank</RouterLink>
      </nav>
    </header>
    <RouterView/>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
</style>
