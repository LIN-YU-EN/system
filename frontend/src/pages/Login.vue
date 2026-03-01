<template>
  <div>
    <h2>登入</h2>
    <div>
      <input v-model="username" placeholder="帳號" />
    </div>
    <div style="margin-top:8px;">
      <input v-model="password" type="password" placeholder="密碼" />
    </div>
    <button style="margin-top:12px;" @click="onLogin">登入</button>
    <p v-if="msg">{{ msg }}</p>
  </div>
</template>

<script setup>
import { ref } from "vue";

const username = ref("");
const password = ref("");
const msg = ref("");

async function onLogin() {
  msg.value = "（先不連後端）你按到登入了 ✅";
}
</script>