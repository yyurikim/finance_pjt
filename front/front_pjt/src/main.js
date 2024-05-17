import { createApp } from 'vue'
import { createPinia } from 'pinia'
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

  
const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(vuetify)
app.mount('#app')
