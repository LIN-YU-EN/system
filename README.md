# SSCI Adaptive Learning System

## 系統簡介
本系統為一套以 SRT 字幕驅動的 Python 程式設計教學平台，
採用 controlled adaptivity 設計，
區分：
- 題目固有難度
- 影片內練習等級
- 單元間正式等級（assessment-only）

## 系統架構
- Backend: Flask + Blueprint
- Frontend: Vue
- Database: MongoDB

## 啟動方式

### 1. 啟動後端
cd backend
python app.py

### 2. 啟動前端
cd frontend
npm run dev

## 核心原則
- 重做不回寫分級
- assessment-only
- 班級隔離
- 籤筒與分級脫鉤