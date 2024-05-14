import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import { useKakao } from 'vue3-kakao-maps/@utils'
import router from './router'

useKakao('021b90905734d34c992a1ca610cde403')
const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
