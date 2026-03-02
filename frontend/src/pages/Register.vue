<template>
  <div>
    <h2>註冊</h2>

    <div>
      <input v-model="username" placeholder="帳號" />
    </div>

    <div style="margin-top: 8px;">
      <input v-model="password" type="password" placeholder="密碼" />
    </div>

    <div style="margin-top: 8px;">
      <input v-model="class_id" placeholder="班級（例：classA）" />
    </div>

    <button style="margin-top: 12px;" @click="onRegister">註冊</button>

    <p v-if="msg" style="margin-top: 10px;">{{ msg }}</p>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { api } from "../services/api";

const username = ref("");
const password = ref("");
const class_id = ref("classA");
const msg = ref("");
const emit = defineEmits(["registered"])

async function onRegister() {
  msg.value = "";

  try {
    const res = await api.post("/api/auth/register", {
      username: username.value,
      password: password.value,
      class_id: class_id.value,
      role: "student",
    });

    msg.value = "註冊成功 ✅（現在可以去登入）";
    emit("registered")
    console.log(res.data);
  } catch (e) {
    msg.value = "註冊失敗 ❌（帳號可能已存在）";
  }
}
</script>