<template>
  <div>
    <h2>註冊</h2>
    <div>
      <input v-model="username" placeholder="帳號" />
    </div>
    <div style="margin-top:8px;">
      <input v-model="password" type="password" placeholder="密碼" />
    </div>
    <div style="margin-top:8px;">
      <input v-model="class_id" placeholder="班級 class_id（例 classA）" />
    </div>
    <button style="margin-top:12px;" @click="onRegister">註冊</button>
    <p v-if="msg">{{ msg }}</p>
  </div>
</template>

<script setup>
import { ref } from "vue";

const username = ref("");
const password = ref("");
const class_id = ref("classA");
const msg = ref("");

async function onRegister() {
  msg.value = "（先不連後端）你按到註冊了 ✅";
}
</script>