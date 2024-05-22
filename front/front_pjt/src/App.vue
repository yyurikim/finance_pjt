<template>
  <div id="app">
    <Header :isHomeView="isHomeView" />
    <main class="main-content">
      <RouterView @route-changed="onRouteChanged" />
    </main>
    <Footer />
  </div>
</template>

<script setup>
import { ref, watchEffect } from 'vue';
import { useRoute, onBeforeRouteUpdate } from 'vue-router';
import Header from '@/components/main/Header.vue';
import Footer from '@/components/main/Footer.vue';

const isHomeView = ref(true);
const route = useRoute();

watchEffect(() => {
  isHomeView.value = route.name === 'home';
});

const onRouteChanged = () => {
  isHomeView.value = route.name === 'home';
};
</script>

<style scoped>
#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  width: 100%;
  margin: 0 auto;
  padding: 1rem;
}

.main-content {
  flex: 1;
  width: 100%;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
}

footer {
  background-color: #ffffff;
  text-align: center;
  width: 100%;
}
</style>
