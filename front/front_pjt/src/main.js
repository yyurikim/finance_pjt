import { createApp } from 'vue'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import App from './App.vue'
import { useKakao } from 'vue3-kakao-maps/@utils'
import router from './router'


import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import '@mdi/font/css/materialdesignicons.css'
import { ko } from 'vuetify/locale'

const vuetify = createVuetify({
    components,
    directives,
    locale: {
      locale: 'ko',
      messages: { ko }
    }
  })

  
useKakao('021b90905734d34c992a1ca610cde403')
const app = createApp(App)

const pinia = createPinia()

pinia.use(piniaPluginPersistedstate)

// app.use(createPinia())
app.use(pinia)
app.use(router)
app.use(vuetify)
app.mount('#app')
