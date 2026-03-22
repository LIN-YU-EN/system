<template>
  <div style="padding: 24px; color: white;">
    <h1>學生頁面</h1>
    <p>這裡之後會顯示學生資訊與班級內容。</p>
  </div>
</template>

<script setup>
const user = JSON.parse(localStorage.getItem("user") || "null");
</script>