<template>
  <div style="padding:40px; max-width:600px; margin:auto;">
    <h1>SSCI Adaptive Learning System</h1>

    <div style="margin-bottom:20px;">
      <button @click="page = 'login'">登入</button>
      <button @click="page = 'register'" style="margin-left:10px;">
        註冊
      </button>
    </div>

    <Login v-if="page === 'login'" />
    <Register v-else />
  </div>
</template>

<script setup>
import { ref } from "vue"
import Login from "./pages/Login.vue"
import Register from "./pages/Register.vue"

const page = ref("login")
</script>