<template>
  <div style="padding: 24px; max-width: 900px; margin: auto;">
    <h1>教師端：影片 / 字幕上傳</h1>

    <div style="margin-top: 12px;">
      <button @click="goDashboard">回 Dashboard</button>
      <button style="margin-left: 8px;" @click="logout">登出</button>
    </div>

    <hr style="margin: 16px 0;" />

    <p>這裡接下來會放：</p>
    <ul>
      <li>unit_id（選擇或輸入）</li>
      <li>video_id（輸入）</li>
      <li>上傳 mp4 + srt</li>
    </ul>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";

const router = useRouter();

function goDashboard() {
  router.push("/teacher");
}

function logout() {
  localStorage.removeItem("user");
  router.push("/login");
}
</script>