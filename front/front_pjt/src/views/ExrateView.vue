<template>
  <div>
<h1 class="title">환율 계산기</h1>
    <ExrateCalculator />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ExrateCalculator from '../components/ExrateCalculator.vue';
</script>

<style scoped>
.title {
  margin-top: 50px;
}

</style>