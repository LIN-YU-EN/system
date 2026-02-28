# API 規格說明（API Specification）

所有 API 皆以：

Base URL:
http://localhost:5000/api/

回傳格式統一：

{
  "success": true / false,
  "message": "說明文字",
  "data": {...}
}

---

# 一、Auth 模組

## 1. 登入

POST /api/auth/login

Request:
{
  "account": "學號",
  "password": "密碼"
}

Response:
{
  "success": true,
  "message": "登入成功",
  "data": {
    "token": "...",
    "role": "student",
    "class_id": "..."
  }
}

---

## 2. 修改密碼

POST /api/auth/change-password

Request:
{
  "old_password": "...",
  "new_password": "..."
}

Response:
{
  "success": true,
  "message": "密碼更新成功"
}

---

# 二、班級管理

## 1. 建立班級

POST /api/classes

Request:
{
  "class_name": "甲班"
}

---

## 2. 匯入學生

POST /api/users/import

Form-data:
file: CSV

Response:
{
  "success": true,
  "data": {
    "success_count": 30,
    "fail_count": 2
  }
}

---

# 三、教材管理

## 1. 建立單元

POST /api/units

## 2. 建立影片

POST /api/videos

## 3. 建立節點

POST /api/nodes

---

# 四、字幕

## 上傳字幕

POST /api/subtitles/upload

Response:
{
  "success": true,
  "data": {
    "segments": [...]
  }
}

---

# 五、題庫

GET /api/questions
POST /api/questions
PUT /api/questions/{id}
DELETE /api/questions/{id}

---

# 六、作答

POST /api/attempts

Request:
{
  "question_id": "...",
  "selected_option": "B",
  "response_time_sec": 12
}

Response:
{
  "success": true,
  "data": {
    "correct": true,
    "misconception_tag": null
  }
}

---

# 七、SUS

POST /api/sus

Request:
{
  "video_id": "...",
  "answers": [1,2,4,5,...]
}

---

# 八、單元分析

GET /api/analytics/unit/{unit_id}

Response:
{
  "success": true,
  "data": {
    "completion_rate": 0.87,
    "average_score": 0.62,
    "top_misconceptions": [...]
  }
}

---

# 九、籤筒

POST /api/lottery/draw

Response:
{
  "success": true,
  "data": {
    "draw_no": 2,
    "result": "上籤",
    "points": 30
  }
}

---

# 十、排行榜

GET /api/leaderboard

Response:
{
  "success": true,
  "data": [
    {"rank":1,"name":"王小明","points":300},
    ...
  ]
}