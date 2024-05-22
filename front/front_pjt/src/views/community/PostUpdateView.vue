<template>
  <div class="app">
    <div class="container">
      <div class="row align-center justify-center" style="height: 100vh;">
        <div class="column col-12">
          <div class="card pa-5">
            <h1 class="text-center">게시글 수정</h1>
            <form @submit.prevent="updateArticle">
              <div class="form-group">
                <label for="category" class="form-label">게시판</label>
                <select id="category" v-model="category" class="input" required>
                  <option value="자유게시판">자유게시판</option>
                  <option value="소비게시판">소비게시판</option>
                  <option value="7일 소비생활 챌린지">7일 소비생활 챌린지</option>
                </select>
              </div>
              <div class="form-group mt-4">
                <label for="title" class="form-label">제목</label>
                <input
                  type="text"
                  id="title"
                  v-model.trim="title"
                  class="input"
                  placeholder="제목을 입력해주세요"
                  required
                />
              </div>
              <div class="form-group mt-4">
                <label for="content" class="form-label">내용</label>
                <textarea
                  id="content"
                  v-model.trim="content"
                  class="input"
                  rows="6"
                  placeholder="내용을 입력해주세요"
                  required
                ></textarea>
              </div>
              <div class="form-group mt-4">
                <label for="image" class="form-label">사진 첨부</label>
                <input
                  type="file"
                  id="image"
                  @change="onFileChange"
                  class="input"
                />
              </div>
              <div v-if="currentImage">
                <p>현재 이미지:</p>
                <img :src="currentImage" alt="Current Image" width="100px" height="100px">
              </div>
              <button type="submit" class="btn btn-primary mt-4">수정하기</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
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

const categoryMap = {
  'bulletin': '자유게시판',
  'consumer': '소비게시판',
  'challenge': '7일 소비생활 챌린지'
}

const fetchPost = async () => {
  try {
    const response = await axios.get(`${store.API_URL}/community/${route.params.boardType}/${route.params.post_id}/`)
    const post = response.data
    title.value = post.title
    content.value = post.content
    category.value = categoryMap[route.params.boardType]  // 카테고리 기본값 설정
    currentImage.value = post.image_url  // 현재 이미지 URL 설정
  } catch (error) {
    console.error(error)
  }
}

const updateArticle = async () => {
  const formData = new FormData()
  formData.append('title', title.value)
  formData.append('content', content.value)
  formData.append('category', category.value)  // 카테고리 추가
  if (image.value) {
    formData.append('image', image.value)
  }

  try {
    await axios.put(`${store.API_URL}/community/${route.params.boardType}/${route.params.post_id}/`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
        Authorization: `Token ${store.token}`
      }
    })
    router.push({ name: 'community', params: { boardType: route.params.boardType } })
  } catch (error) {
    console.error(error.response.data)  // 오류 메시지 출력
  }
}

const onFileChange = (e) => {
  const files = e.target.files
  if (files.length > 0) {
    image.value = files[0]
  }
}

onMounted(fetchPost)
</script>
<style scoped>
.app {
  padding: 20px;
}

.container {
  width: 800px;
  margin: 0 auto;
}

.row {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.column {
  padding: 10px;
  box-sizing: border-box;
}


.form-label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
  text-align: left;
}

.col-12 {
  flex: 0 0 100%;
  max-width: 100%;
}

.card {
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.text-center {
  text-align: center;
}

.form-group {
  margin-bottom: 1.5rem;
}

.input {
  width: 100%;
  padding: 10px;
  margin-top: 5px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-sizing: border-box;
}

.btn {
  display: inline-block;
  padding: 10px 20px;
  background-color: rgb(83, 204, 168);
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  text-align: center;
  font-size: 16px;
}

.btn-primary {
  background-color: rgb(83, 204, 168);
  color: white;
}

.mt-4 {
  margin-top: 1.5rem;
}

.pa-5 {
  padding: 20px;
}
</style>


<!-- <template>
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
   -->