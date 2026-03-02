<template>
  <div>
    <h2>登入</h2>

    <div>
      <input v-model="username" placeholder="帳號" />
    </div>

    <div style="margin-top: 8px;">
      <input v-model="password" type="password" placeholder="密碼" />
    </div>

    <button style="margin-top: 12px;" @click="onLogin">登入</button>
    <div style="margin-top: 10px;">
        <a href="#" @click.prevent="onForgot">忘記密碼？</a>
    </div>

    <p v-if="msg" style="margin-top: 10px;">{{ msg }}</p>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { api } from "../services/api";

const emit = defineEmits(["login-success"]);

const username = ref("");
const password = ref("");
const msg = ref("");

async function onLogin() {
  msg.value = "";

  try {
    const res = await api.post("/api/auth/login", {
      username: username.value,
      password: password.value,
    });

    // 你的後端回傳格式目前是：{ message, user: { ... } }
    const user = res.data?.user;

    // 存到瀏覽器（下次重新整理還在）
    localStorage.setItem("user", JSON.stringify(user));

    msg.value = "登入成功 ✅";
    emit("login-success", user);
  } catch (e) {
    msg.value = "登入失敗 ❌（請確認帳密）";
  }
}
function onForgot() {
  alert("忘記密碼功能下一步會做（先顯示這個提示）");
}
</script>