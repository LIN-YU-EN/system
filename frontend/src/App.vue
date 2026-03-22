<template>
  <Navbar />
  <div class="page">
    <router-view />
  </div>
</template>

<script setup>
import Navbar from "./components/Navbar.vue";
</script>

<style>
.page {
  margin-top: 70px; /* 跟 navbar 高度一樣 */
}
</style>