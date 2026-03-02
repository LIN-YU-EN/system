<template>
  <div style="padding: 40px; max-width: 700px; margin: auto;">
    <h1>SSCI 自適應學習系統</h1>

    <!-- 如果已登入：顯示 Dashboard -->
    <div v-if="currentUser" style="margin-top: 20px;">
      <h2>已登入 ✅</h2>

      <div style="margin-top: 10px; line-height: 1.8;">
        <div><b>帳號：</b>{{ currentUser.username }}</div>
        <div><b>角色：</b>{{ currentUser.role }}</div>
        <div><b>班級：</b>{{ currentUser.class_id }}</div>
        <div><b>user_id：</b>{{ currentUser.id }}</div>
      </div>

      <button style="margin-top: 16px;" @click="logout">登出</button>
    </div>

    <!-- 未登入：顯示 Login/Register -->
    <div v-else>
      <div style="margin: 20px 0;">
        <button @click="page = 'login'">登入</button>
        <button @click="page = 'register'" style="margin-left: 10px;">註冊</button>
      </div>

      <Login v-if="page === 'login'" @login-success="onLoginSuccess" />
      <Register v-else @registered="page = 'login'" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import Login from "./pages/Login.vue";
import Register from "./pages/Register.vue";

const page = ref("register");
const currentUser = ref(null);

onMounted(() => {
  // 重新整理頁面也能保持登入
  const saved = localStorage.getItem("user");
  if (saved) currentUser.value = JSON.parse(saved);
});

function onLoginSuccess(user) {
  currentUser.value = user;
}

function logout() {
  localStorage.removeItem("user");
  currentUser.value = null;
  page.value = "login";
}
</script>