<template>
  <div class="app">
    <div class="container">
      <div class="row align-center justify-center" style="height: 100vh;">
        <div class="column col-12">
          <div class="card">
            <h1 class="text-center">게시글 작성</h1>
            <form @submit.prevent="createArticle">
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
              <button type="submit" class="btn btn-primary mt-4">게시물 포스팅</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>



<script setup>
import { ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useCommunityStore } from '@/stores/community'

const communityStore = useCommunityStore()
const router = useRouter()
const route = useRoute()

const title = ref('')
const content = ref('')
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

const onFileChange = (e) => {
  const files = e.target.files
  if (files.length > 0) {
    image.value = files[0]
  }
}
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

.col-12 {
  flex: 0 0 100%;
  max-width: 100%;
}

.card {
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  max-width: 800px;
  width: 100%;
  margin: 0 auto;
}

.text-center {
  text-align: center;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
  text-align: left;
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
</style>