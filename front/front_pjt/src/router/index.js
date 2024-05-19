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
import SurveyView from '@/views/survey/SurveyView.vue'
import ResultView from '@/views/survey/ResultView.vue'
import Survey1 from '@/components/survey/Survey1.vue'
import Survey2 from '@/components/survey/Survey2.vue'
import Survey3 from '@/components/survey/Survey3.vue'
import Survey4 from '@/components/survey/Survey4.vue'
import Survey5 from '@/components/survey/Survey5.vue'
import Survey6 from '@/components/survey/Survey6.vue'
import Survey7 from '@/components/survey/Survey7.vue'
import Survey8 from '@/components/survey/Survey8.vue'
import Survey9 from '@/components/survey/Survey9.vue'

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
    { path: '/survey', name: 'survey', component : SurveyView },
    { path: '/survey/1', name: 'survey1', component: Survey1 },
    { path: '/survey/2', name: 'survey2', component: Survey2 },
    { path: '/survey/3', name: 'survey3', component: Survey3 },
    { path: '/survey/4', name: 'survey4', component: Survey4 },
    { path: '/survey/5', name: 'survey5', component: Survey5 },
    { path: '/survey/6', name: 'survey6', component: Survey6 },
    { path: '/survey/7', name: 'survey7', component: Survey7 },
    { path: '/survey/8', name: 'survey8', component: Survey8 },
    { path: '/survey/9', name: 'survey9', component: Survey9 },
    { path: '/survey/result', name: 'result', component: ResultView },
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