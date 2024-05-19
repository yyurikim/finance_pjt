<template>
  <v-app>
    <v-container class="d-flex align-center justify-center" style="height: 100vh;">
      <v-row>
        <v-col cols="12" md="8" lg="6">
          <v-card class="pa-5">
            <h1 class="text-center">게시글 작성</h1>
            <v-form @submit.prevent="createArticle">
              <v-combobox
                label="게시판"
                v-model="category"
                :items="['자유게시판', '소비게시판', '7일 소비생활 챌린지']"
                outlined
                dense
              ></v-combobox>
              <v-text-field
                variant="outlined"
                label="제목"
                v-model.trim="title"
                :rules="[v => !!v || '제목을 입력해주세요']"
                dense
                class="mt-4"
              ></v-text-field>
              <v-textarea
                variant="outlined"
                label="내용"
                v-model.trim="content"
                :rules="[v => !!v || '내용을 입력해주세요']"
                dense
                class="mt-4"
              ></v-textarea>
              <v-file-input
                label="사진 첨부"
                prepend-icon="mdi-camera"
                variant="filled"
                v-model="image"
                dense
                class="mt-4"
              ></v-file-input>
              <v-btn 
                block
                color="primary"
                type="submit"
                class="mt-4"
              >
                게시물 포스팅
              </v-btn>
            </v-form>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useCommunityStore } from '@/stores/community'

const communityStore = useCommunityStore()
const router = useRouter()
const route = useRoute()

const title = ref(null)
const content = ref(null)
const category = ref(route.params.boardType || '자유게시판')
const image = ref(null)

const categoryMap = {
  '자유게시판': 'bulletin',
  '소비게시판': 'consumer',
  '7일 소비생활 챌린지': 'challenge'
}

const createArticle = async () => {
  const formData = new FormData()
  formData.append('title', title.value)
  formData.append('content', content.value)
  if (image.value) {
    formData.append('image', image.value)
  }

  const apiCategory = categoryMap[category.value] || 'bulletin'  // 기본값 설정

  try {
    const response = await communityStore.addPost(apiCategory, formData)
    router.push({ name: 'community', params: { boardType: apiCategory } })
  } catch (error) {
    console.error(error)
  }
}
</script>

<style>
</style>



<!-- <template>
  <v-app>
    <v-container class="d-flex align-center justify-center" style="height: 100vh;">
      <v-row>
        <v-col cols="12" md="8" lg="6">
          <v-card class="pa-5">
            <h1 class="text-center">게시글 작성</h1>
            <v-form @submit.prevent="createArticle">
              <v-combobox
                label="게시판"
                v-model="category"
                :items="['자유게시판', '살까 말까?!', '7일 소비생활 챌린지']"
                outlined
                dense
              ></v-combobox>
              <v-text-field
                variant="outlined"
                label="제목"
                v-model.trim="title"
                :rules="[v => !!v || '제목을 입력해주세요']"
                dense
                class="mt-4"
              ></v-text-field>
              <v-textarea
                variant="outlined"
                label="내용"
                v-model.trim="content"
                :rules="[v => !!v || '내용을 입력해주세요']"
                dense
                class="mt-4"
              ></v-textarea>
              <v-file-input
                label="사진 첨부"
                prepend-icon="mdi-camera"
                variant="filled"
                v-model="image"
                dense
                class="mt-4"
              ></v-file-input>
              <v-btn 
                block
                color="primary"
                type="submit"
                class="mt-4"
              >
                게시물 포스팅
              </v-btn>
            </v-form>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const store = useCounterStore()
const title = ref(null)
const content = ref(null)
const category = ref(null)
const image = ref(null)
const router = useRouter()

const createArticle = async () => {
  const formData = new FormData()
  formData.append('title', title.value)
  formData.append('content', content.value)
  formData.append('category', category.value)
  if (image.value) {
    formData.append('image', image.value)
  }

  try {
    const response = await axios.post(`${store.API_URL}/community/`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
        Authorization: `Token ${store.token}`
      }
    })
    router.push({ name: 'community' })
  } catch (error) {
    console.error(error)
  }
}
</script>

<style>
</style> -->
