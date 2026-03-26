<template>
  <div class="page">
    <div class="card">
      <h1>影片與字幕上傳</h1>
      <p class="subtitle">請上傳 mp4 與對應的 srt 字幕檔</p>

      <div class="file-group">
        <label>影片檔案（.mp4）</label>
        <input type="file" accept=".mp4,video/mp4" @change="handleVideo" />
        <small>{{ videoName || '尚未選擇影片' }}</small>
      </div>

      <div class="file-group">
        <label>字幕檔案（.srt）</label>
        <input type="file" accept=".srt" @change="handleSrt" />
        <small>{{ srtName || '尚未選擇字幕' }}</small>
      </div>

      <div class="actions">
        <button class="back" @click="goBack">返回</button>
        <button class="submit" @click="submitFiles">上傳</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const videoFile = ref(null)
const srtFile = ref(null)

const videoName = ref('')
const srtName = ref('')

function handleVideo(e) {
  const file = e.target.files[0]
  videoFile.value = file
  videoName.value = file ? file.name : ''
}

function handleSrt(e) {
  const file = e.target.files[0]
  srtFile.value = file
  srtName.value = file ? file.name : ''
}

function goBack() {
  router.push('/teacher/upload')
}

function submitFiles() {
  console.log('video:', videoFile.value)
  console.log('srt:', srtFile.value)
}
</script>

<style scoped>
.page {
  min-height: calc(100vh - 70px);
  padding: 32px;
}

.card {
  max-width: 700px;
  margin: 0 auto;
  padding: 32px;
  background: rgba(255,255,255,0.95);
  border-radius: 20px;
  box-shadow: 0 12px 30px rgba(0,0,0,0.12);
}

.subtitle {
  margin-top: 8px;
  color: #666;
}

.file-group {
  margin-top: 24px;
  display: flex;
  flex-direction: column;
}

.file-group label {
  font-weight: 600;
  margin-bottom: 8px;
}

.file-group input {
  padding: 8px;
}

.file-group small {
  margin-top: 8px;
  color: #666;
}

.actions {
  margin-top: 30px;
  display: flex;
  justify-content: space-between;
}

.back {
  padding: 10px 20px;
  border-radius: 10px;
  border: none;
  background: #ccc;
  cursor: pointer;
}

.submit {
  padding: 10px 20px;
  border-radius: 10px;
  border: none;
  background: linear-gradient(135deg,#667eea,#764ba2);
  color: white;
  cursor: pointer;
}
</style>