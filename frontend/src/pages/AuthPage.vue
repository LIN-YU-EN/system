<template>
  <div class="bg">
    <div class="card">
      <div class="topTag">Login / Signup</div>

      <div class="tabs">
        <button :class="['tab', tab==='login'?'active':'']" @click="tab='login'">LOGIN</button>
        <button :class="['tab', tab==='signup'?'active':'']" @click="tab='signup'">SIGNUP</button>
      </div>

      <div class="form">
        <!-- LOGIN -->
        <template v-if="tab==='login'">

          <input v-model="loginUsername" class="input" placeholder="帳號" />
          <input v-model="loginPassword" class="input" type="password" placeholder="密碼" />

          <button class="btn" @click="onLogin">LOGIN</button>
        </template>

        <!-- SIGNUP（學生註冊） -->
        <template v-else>
          <input v-model="suUsername" class="input" placeholder="學生帳號" />
          <input v-model="suPassword" class="input" type="password" placeholder="密碼" />
          <input v-model="suName" class="input" placeholder="學生名稱" />

          <select v-model="suGender" class="input">
            <option value="M">男</option>
            <option value="F">女</option>
          </select>

          <select v-model="suClass" class="input">
            <option value="classA">classA</option>
            <option value="classB">classB</option>
          </select>

          <button class="btn" @click="onSignup">SIGNUP</button>
        </template>

        <p v-if="msg" class="msg">{{ msg }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { api } from "../services/api";
import { useRouter } from "vue-router";

const router = useRouter();
const tab = ref("login");
const msg = ref("");

// LOGIN
const loginUsername = ref("");
const loginPassword = ref("");

// SIGNUP（學生）
const suUsername = ref("");
const suPassword = ref("");
const suName = ref("");
const suGender = ref("M");
const suClass = ref("classA");

async function onLogin() {
  msg.value = "";
  try {
    const res = await api.post("/api/auth/login", {
      username: loginUsername.value,
      password: loginPassword.value,
    });

    const user = res.data?.user;
    localStorage.setItem("user", JSON.stringify(user));

    // ✅ 以資料庫回傳的 user.role 為準（不要信前端下拉）
    if (user?.role === "teacher") {
      router.push("/teacher/upload");
    } else {
      alert("學生端尚未開放（目前先做教師端上傳模組）");
      router.push("/login");
    }
  } catch (e) {
    msg.value = "登入失敗 ❌（請確認帳密）";
  }
}

async function onSignup() {
  msg.value = "";

  // 最基本前端檢查（避免空值）
  if (!suUsername.value || !suPassword.value || !suName.value) {
    msg.value = "請填完整：帳號 / 密碼 / 名稱";
    return;
  }

  try {
    await api.post("/api/auth/register", {
      username: suUsername.value,
      password: suPassword.value,
      name: suName.value,
      gender: suGender.value,
      class_id: suClass.value,
      role: "student",
    });

    msg.value = "註冊成功 ✅（請回到登入）";
    tab.value = "login";
  } catch (e) {
    msg.value = "註冊失敗 ❌（帳號可能已存在）";
  }
}
</script>

<style scoped>
.bg{
  height:100vh;
  display:flex;
  align-items:center;
  justify-content:center;
  
}
.card{
  width: 420px;
  background:#fff;
  border-radius:10px;
  box-shadow:0 18px 40px rgba(0,0,0,.35);
  position:relative;
  padding: 28px 26px 26px;
}
.topTag{
  position:absolute;
  top:-18px;
  left:50%;
  transform:translateX(-50%);
  padding:10px 18px;
  border-radius:8px;
  color:#fff;
  font-weight:700;
  background: linear-gradient(90deg,#ff8a65,#f06292);
}
.tabs{
  display:flex;
  border-radius:8px;
  overflow:hidden;
  margin-top: 12px;
}
.tab{
  flex:1;
  padding:10px 0;
  border:none;
  background:#f3f3f3;
  font-weight:700;
  cursor:pointer;
}
.tab.active{
  color:#fff;
  background: linear-gradient(90deg,#ff8a65,#f06292);
}
.form{ margin-top: 16px; }
.input{
  width:100%;
  box-sizing:border-box;
  margin-top: 10px;
  padding: 12px 12px;
  border:1px solid #ddd;
  border-radius:6px;
  outline:none;
}
.btn{
  width:100%;
  margin-top: 16px;
  padding: 12px 0;
  border:none;
  border-radius:6px;
  cursor:pointer;
  color:#fff;
  font-weight:800;
  background: linear-gradient(90deg,#ff8a65,#f06292);
}
.msg{ margin-top: 12px; color:#333; font-size: 14px; }
</style>