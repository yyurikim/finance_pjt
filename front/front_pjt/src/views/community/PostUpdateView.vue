<template>
    <v-app>
      <v-container class="d-flex align-center justify-center" style="height: 100vh;">
        <v-row>
          <v-col cols="12" md="8" lg="6">
            <v-card class="pa-5">
              <h1 class="text-center">게시글 수정</h1>
              <v-form @submit.prevent="updateArticle">
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
                <div v-if="currentImage">
                  <p>현재 이미지:</p>
                  <img :src="currentImage" alt="Current Image" width="100px" height="100px">
                </div>
                <v-btn 
                  block
                  color="primary"
                  type="submit"
                  class="mt-4"
                >
                  수정하기
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
  import { ref, onMounted } from 'vue'
  import { useCounterStore } from '@/stores/counter'
  import { useRouter, useRoute } from 'vue-router'
  
  const store = useCounterStore()
  const title = ref(null)
  const content = ref(null)
  const category = ref(null)
  const image = ref(null)
  const currentImage = ref(null)  // 현재 이미지를 표시하기 위한 변수
  const router = useRouter()
  const route = useRoute()
  
  onMounted(() => {
    axios({
      method: 'get',
      url: `${store.API_URL}/community/post/${route.params.post_id}/`
    })
    .then(response => {
      const post = response.data
      title.value = post.title
      content.value = post.content
      category.value = post.category  // 카테고리 기본값 설정
      currentImage.value = post.image_url  // 현재 이미지 URL 설정
    })
    .catch(error => {
      console.error(error)
    })
  })
  
  const updateArticle = () => {
    const formData = new FormData()
    formData.append('title', title.value)
    formData.append('content', content.value)
    formData.append('category', category.value)  // 카테고리 추가
    if (image.value) {
      formData.append('image', image.value)
    }
  
    axios({
      method: 'put',
      url: `${store.API_URL}/community/post/${route.params.post_id}/`,
      data: formData,
      headers: {
        'Content-Type': 'multipart/form-data',
        Authorization: `Token ${store.token}`
      }
    })
    .then(() => {
      router.push({ name: 'community' })
    })
    .catch(error => {
      console.error(error.response.data)  // 오류 메시지 출력
    })
  }
  </script>
  
  <style scoped>
  </style>
  