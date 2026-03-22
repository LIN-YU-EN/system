import { createRouter, createWebHistory } from "vue-router";
import AuthPage from "../pages/AuthPage.vue";
import TeacherDashboard from "../pages/TeacherDashboard.vue";
import TeacherUpload from "../pages/TeacherUpload.vue";
import StudentDashboard from "../pages/StudentDashboard.vue";
import HomePage from "../pages/HomePage.vue";

const routes = [
  { path: "/", component: HomePage },
  { path: "/login", component: AuthPage },

  // 教師端
  { path: "/teacher", component: TeacherDashboard },
  { path: "/teacher/upload", component: TeacherUpload },
  //學生端
  { path: "/student", component: StudentDashboard },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});


// ✅ 守門員：教師端一律要登入（沒登入才踢回 /login）
router.beforeEach((to) => {
  const userRaw = localStorage.getItem("user");
  const user = userRaw ? JSON.parse(userRaw) : null;

  if (to.path.startsWith("/teacher") && (!user || user.role !== "teacher")) {
    return "/login";
  }

  if (to.path.startsWith("/student") && (!user || user.role !== "student")) {
    return "/login";
  }
});

export default router;