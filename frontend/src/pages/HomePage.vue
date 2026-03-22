<template>
  <div class="home">
    <div class="content">
      <h1>Python 自適應學習系統</h1>
      <button @click="goLearning">進入學習</button>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";

const router = useRouter();

function goLearning() {
  const raw = localStorage.getItem("user");
  const user = raw ? JSON.parse(raw) : null;

  if (!user) {
    router.push("/login");
    return;
  }

  if (user.role === "teacher") {
    router.push("/teacher");
  } else if (user.role === "student") {
    router.push("/student");
  } else {
    router.push("/login");
  }
}
</script>

<style scoped>
.home {
  height: calc(100vh - 70px);
  display: flex;
  justify-content: center;
  align-items: center;
}

.content {
  text-align: center;
  color: white;
}

button {
  margin-top: 16px;
  padding: 10px 18px;
  border: none;
  border-radius: 20px;
  background: rgba(255,255,255,0.2);
  color: white;
  cursor: pointer;
}
</style>