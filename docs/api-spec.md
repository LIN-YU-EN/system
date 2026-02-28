# API Specification

版本：v0.1

Base URL:
http://localhost:5000/api/

---

## Auth
POST /api/auth/login
POST /api/auth/change-password

---

## Content
GET /api/units
GET /api/videos/{unit_id}

---

## Attempts
POST /api/attempts

---

## Analytics
GET /api/analytics/unit/{unit_id}

---

所有 API 回傳統一格式：

{
  "success": true/false,
  "message": "...",
  "data": {}
}