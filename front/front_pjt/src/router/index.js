import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import SignupView from '@/views/user/SignupView.vue'
import LoginView from '@/views/user/LoginView.vue'
import ChangePwdView from '@/views/user/ChangePwdView.vue'
import ExrateView from '@/views/ExrateView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignupView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/changepwd',
      name: 'changepwd',
      component: ChangePwdView
    },
    {
      path: '/exchange_rate',
      name: 'exchange_rate',
      component : ExrateView
    }
  ]
})

export default router