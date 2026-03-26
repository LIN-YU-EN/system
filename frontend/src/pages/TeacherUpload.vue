<template>
  <div class="teacher-upload-page">
    <div class="upload-card">
      <h1>教材上傳</h1>
      <p class="subtitle">先選擇單元並建立單元名稱，再前往檔案管理頁面</p>

      <div class="form-grid">
        <div class="form-group">
          <label>單元</label>
          <select v-model="form.unit" class="select-input">
            <option disabled value="">請選擇單元</option>
            <option v-for="item in unitOptions" :key="item" :value="item">
              {{ item }}
            </option>
          </select>
        </div>

        <div class="form-group">
          <label>單元名稱</label>
          <input
            v-model="form.unit_title"
            type="text"
            placeholder="例如：Python 基礎語法"
          />
        </div>
      </div>

      <div class="actions">
        <button class="next-btn" @click="goNext">下一步：上傳檔案</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const unitOptions = ref([
  'Unit 1',
  'Unit 2',
  'Unit 3'
])

const form = reactive({
  unit: '',
  unit_title: ''
})

function goNext() {
  router.push('/teacher/upload/files')
}
</script>

<style scoped>
.teacher-upload-page {
  min-height: calc(100vh - 70px);
  padding: 32px;
}

.upload-card {
  max-width: 900px;
  margin: 0 auto;
  background: rgba(255, 255, 255, 0.95);
  border-radius: 20px;
  padding: 32px;
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.12);
}

.subtitle {
  color: #666;
  margin-top: 8px;
}

.form-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin-top: 24px;
}

.form-group {
  display: flex;
  flex-direction: column;
}

.form-group label {
  font-weight: 600;
  margin-bottom: 8px;
  color: #333;
}

.form-group input {
  padding: 12px 14px;
  border: 1px solid #ddd;
  border-radius: 10px;
  font-size: 14px;
  outline: none;
}

.form-group input:focus {
  border-color: #667eea;
}

.select-input {
  padding: 12px 14px;
  border: 1px solid #ddd;
  border-radius: 10px;
  font-size: 14px;
  outline: none;
  background: white;
}

.select-input:focus {
  border-color: #667eea;
}

.actions {
  margin-top: 28px;
  display: flex;
  justify-content: flex-end;
}

.next-btn {
  border: none;
  padding: 12px 22px;
  border-radius: 10px;
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
  background: linear-gradient(135deg, #667eea, #764ba2);
  color: white;
}
</style>