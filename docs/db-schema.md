# 資料庫結構（MongoDB）

版本：v0.1

---

## users
- user_id
- role
- class_id
- account
- password_hash

---

## classes
- class_id
- class_name

---

## content
- unit_id
- video_id
- node_id

---

## questions
- question_id
- unit_id
- video_id
- node_id
- bloom
- difficulty_pool

---

## attempts
- user_id
- question_id
- correct
- attempt_no

---

## history_video
（第一次完成紀錄）
- user_id
- video_id
- score

---

## learning_trace
（最新狀態）
- user_id
- video_id
- node_id
- misconception_tag