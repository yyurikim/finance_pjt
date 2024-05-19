import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import router from './router'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import { useKakao } from 'vue3-kakao-maps/@utils'


import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import { aliases, fa } from 'vuetify/iconsets/fa'
import '@mdi/font/css/materialdesignicons.css'
import '@fortawesome/fontawesome-free/css/all.css'; // FontAwesome CSS 파일
import { ko } from 'vuetify/locale'

const vuetify = createVuetify({
    components,
    directives,
    icons: {
      defaultSet: 'fa',
      aliases,
      sets: {
        fa,
      },
    },
    locale: {
      locale: 'ko',
      messages: { ko }
    }
  })

const app = createApp(App)

// Axios 설정
app.config.globalProperties.$http = axios.create({
  baseURL: 'http://127.0.0.1:8000/banks/api/'  // API 엔드포인트 기본 URL 설정
})

const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)
app.use(pinia)

app.use(router)
app.use(vuetify)
app.mount('#app')
