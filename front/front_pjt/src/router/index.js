import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import BankMapView2 from '@/views/BankMapView2.vue'
import SignupView from '@/views/user/SignupView.vue'
import LoginView from '@/views/user/LoginView.vue'
import ChangePwdView from '@/views/user/ChangePwdView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/map',
      name: 'map',
      component: BankMapView2
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
    }
  ]
})

export default router