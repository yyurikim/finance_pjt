<template>
  <header :class="{ hidden: isHomeView, whiteBackground: !isHomeView }">
    <nav>
      <RouterLink :to="{ name: 'home' }" class="logo">Home</RouterLink>
      <ul>
        <li><RouterLink :to="{ name: 'profile' }">Profile</RouterLink></li>
        <li><RouterLink :to="{ name: 'bank' }">Bank</RouterLink></li>
        <li><RouterLink :to="{ name: 'map' }">BankMap</RouterLink></li>
        <li><RouterLink :to="{ name: 'exchange_rate' }">ExchangeRate</RouterLink></li>
        <li><RouterLink :to="{ name: 'community' }">Community</RouterLink></li>
        <li><RouterLink :to="{ name: 'test' }">Test</RouterLink></li>
        <li><RouterLink :to="{ name: 'changepwd' }">Changepwd</RouterLink></li>
        <li><RouterLink :to="{ name: 'changeinfo' }">Changeinfo</RouterLink></li>
      </ul>
    </nav>
  </header>
</template>

<script setup>
const props = defineProps({
  isHomeView: {
    type: Boolean,
    required: true,
  },
});
</script>

<style scoped>
header {
  padding: 1rem;
  transition: background-color 0.3s, box-shadow 0.3s;
  box-shadow: 0 4px 6px -6px rgba(0, 0, 0, 0.2); /* Shadow only at the bottom */
}

header.hidden {
  display: none;
}

header.whiteBackground {
  background-color: #fff;
  height: 3.5rem;
  box-shadow: 0 4px 6px -6px rgba(0, 0, 0, 0.5); /* Shadow only at the bottom */
}

nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

nav .logo {
  font-size: 1.5rem;
  font-weight: bold;
  color: #333;
  text-decoration: none;
}

nav ul {
  list-style: none;
  display: flex;
  justify-content: center; /* Center align the navigation links */
  padding: 0;
  margin: 0;
  flex-grow: 1; /* Allow the ul to grow and center the items */
}

nav ul li {
  margin: 0 1rem;
}

nav ul li a {
  color: #333;
  text-decoration: none;
  font-size: 1rem;
  padding: 0.5rem;
  transition: color 0.3s, background-color 0.3s;
}

nav ul li a:hover {
  color: #007bff;
  background-color: #f0f0f0;
  border-radius: 0.3rem;
}

@media (max-width: 768px) {
  nav ul {
    flex-direction: column;
    align-items: center;
  }

  nav ul li {
    margin: 0.5rem 0;
  }
}
</style>
