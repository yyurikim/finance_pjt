import { createRouter, createWebHistory } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import TestView from '@/views/TestView.vue'
import HomeView from '@/views/HomeView.vue'
import MapView from '@/views/MapView.vue'
import SignupView from '@/views/user/SignupView.vue'
import LoginView from '@/views/user/LoginView.vue'
import ChangePwdView from '@/views/user/ChangePwdView.vue'
import ExrateView from '@/views/ExrateView.vue'
import PostListView from '@/views/community/PostListView.vue'
import PostCreateView from '@/views/community/PostCreateView.vue'
import PostDetailView from '@/views/community/PostDetailView.vue'
import PostUpdateView from '@/views/community/PostUpdateView.vue'
import BankView from '@/views/bank/BankView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/test',
      name: 'test',
      component: TestView
    },
    {
      path: '/map',
      name: 'map',
      component: MapView
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
    },
    {
      path: '/community',
      name: 'community',
      component : PostListView
    },
    {
      path: '/post_create',
      name: 'post_create',
      component : PostCreateView
    },
    {
      path: '/:boardType/post/:post_id',
      name: 'post_detail',
      component: PostDetailView,
      props: true
    },
    {
      path: '/:boardType/post/:post_id/update',
      name: 'post_update',
      component : PostUpdateView
    },
    {
      path: '/bank',
      name: 'bank',
      component : BankView
    },
  ]

})

router.beforeEach((to, from) => {
  const store = useCounterStore()

  // 인증되지 않은 사용자는 비밀번호 변경 페이지에 접근할 수 없음
  if (to.name === 'changepwd' && !store.isLogin) {
    window.alert('로그인이 필요해요!!')
    return { name: 'login' }
  }

  // 인증된 사용자는 회원가입과 로그인 페이지에 접근할 수 없음
  if ((to.name === 'signup' || to.name === 'login') ) {
    if (store.isLogin) {
    window.alert('이미 로그인 했습니다.')
    return { name: 'home' }
  }}
})

export default router