<template>
  <div class="nav">
    <div class="left">
      <span class="brand" @click="go('/')">Python</span>
    </div>

    <div class="right">
        <template v-if="user">
            <div class="user-menu-wrapper">
                <button class="user-btn" @click="toggleMenu">
                    {{ user.name }}
                    <span class="arrow">▼</span>
                </button>

                <div v-if="menuOpen" class="dropdown">
                    <div class="dropdown-header">
                        <div class="avatar">👤</div>
                        <div>
                            <div class="user-title">{{ user.name }}</div>
                            <div class="user-subtitle">{{ user.username }}</div>
                        </div>
                    </div>

                    <div class="dropdown-item" @click="goProfile">個人設定</div>
                    <div class="dropdown-item">繁體中文</div>
                    <div class="dropdown-divider"></div>
                    <div class="dropdown-item logout-item" @click="logout">登出</div>
                </div>
            </div>
        </template>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from "vue";
import { useRouter, useRoute } from "vue-router";

const router = useRouter();
const route = useRoute();

const user = ref(null);
const menuOpen = ref(false);

function loadUser() {
  const raw = localStorage.getItem("user");
  user.value = raw ? JSON.parse(raw) : null;
}

loadUser();

watch(
  () => route.fullPath,
  () => {
    loadUser();
    menuOpen.value = false;
  }
);

function go(path) {
  menuOpen.value = false;
  router.push(path);
}

function toggleMenu() {
  menuOpen.value = !menuOpen.value;
}

function goProfile() {
  menuOpen.value = false;
  alert("個人設定頁面下一步會做");
}

function logout() {
  localStorage.removeItem("user");
  user.value = null;
  menuOpen.value = false;
  router.push("/login");
}
</script>

<style scoped>
.nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 70px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 24px;
  box-sizing: border-box;
  color: white;
  background: linear-gradient(135deg, #5f9cff, #a855f7);
  z-index: 999;
}

.left,
.right {
  display: flex;
  align-items: center;
  gap: 16px;
}

.brand {
  font-size: 24px;
  font-weight: bold;
  cursor: pointer;
}

.action-btn,
.user-btn {
  padding: 8px 18px;
  border-radius: 20px;
  border: none;
  background: rgba(255,255,255,0.2);
  color: white;
  cursor: pointer;
  font-size: 15px;
}

.action-btn:hover,
.user-btn:hover {
  background: rgba(255,255,255,0.35);
}

.user-menu-wrapper {
  position: relative;
}

.arrow {
  margin-left: 8px;
  font-size: 12px;
}

.dropdown {
  position: absolute;
  top: 48px;
  right: 0;
  width: 220px;
  background: white;
  color: #222;
  border-radius: 10px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.18);
  overflow: hidden;
}

.dropdown-header {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 16px;
  background: #f5f5f5;
}

.avatar {
  font-size: 28px;
}

.user-title {
  font-weight: 700;
}

.user-subtitle {
  font-size: 13px;
  color: #666;
}

.dropdown-item {
  padding: 14px 16px;
  cursor: pointer;
}

.dropdown-item:hover {
  background: #f7f7f7;
}

.dropdown-divider {
  height: 1px;
  background: #e5e5e5;
}

.logout-item {
  color: #c0392b;
}
</style>