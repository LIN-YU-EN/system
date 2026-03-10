import { createRouter, createWebHistory } from "vue-router";
import AuthPage from "../pages/AuthPage.vue";
import TeacherDashboard from "../pages/TeacherDashboard.vue";
import TeacherUpload from "../pages/TeacherUpload.vue";

const routes = [
  { path: "/", redirect: "/login" },
  { path: "/login", component: AuthPage },

  // 教師端
  { path: "/teacher", component: TeacherDashboard },
  { path: "/teacher/upload", component: TeacherUpload },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// ✅ 守門員：教師端一律要登入（沒登入才踢回 /login）
router.beforeEach((to) => {
  const user = localStorage.getItem("user");
  if (to.path.startsWith("/teacher") && !user) return "/login";
});

export default router;