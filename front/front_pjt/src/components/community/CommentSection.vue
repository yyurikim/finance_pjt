<template>
  <div class="app">
    <div class="container">
      <div class="form-group">
        <label for="comment">댓글 작성</label>
        <textarea
          id="comment"
          v-model.trim="content"
          class="input"
          rows="3"
          placeholder="댓글을 입력하세요"
          required
        ></textarea>
        <button @click="createComment" class="btn-sm mt-2">댓글 달기</button>
      </div>
      <div class="comment-list">
        <div v-for="comment in comments" :key="comment.id" class="list-item">
          <div class="list-item-content">
            <template v-if="editingCommentId === comment.id">
              <textarea
                v-model="editingCommentContent"
                class="input"
                rows="3"
              ></textarea>
              <button @click="updateComment(comment.id)" class="btn btn-primary">수정</button>
              <button @click="cancelEdit" class="btn btn-secondary">수정 취소</button>
            </template>
            <template v-else>
              <h4>{{ comment.user_name }}</h4>
              <p>{{ comment.content }}</p>
              <p>{{ new Date(comment.created_at).toLocaleString() }}</p>
              <button @click="startEdit(comment)" class="btn btn-primary">수정</button>
              <button @click="deleteComment(comment.id)" class="btn btn-error">삭제</button>
            </template>
          </div>
        </div>
        <div v-if="comments.length === 0" class="list-item">
          <div class="list-item-content">
            <h4>댓글이 없습니다.</h4>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const route = useRoute()
const comments = ref([])
const content = ref('')
const editingCommentId = ref(null)
const editingCommentContent = ref('')

const fetchComments = async () => {
  try {
    const response = await axios.get(`${store.API_URL}/community/${route.params.boardType}/${route.params.post_id}/comment/`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    comments.value = response.data
  } catch (error) {
    console.error('댓글 조회 실패:', error.response?.data || error.message)
  }
}

const createComment = async () => {
  try {
    const response = await axios.post(`${store.API_URL}/community/${route.params.boardType}/comment/`, {
      post_id: route.params.post_id,
      content: content.value,
    }, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    content.value = ''
    console.log('댓글 생성 성공:', response.data)
    fetchComments() // 댓글 생성 후 댓글 목록 다시 불러오기
  } catch (error) {
    console.error('댓글 생성 실패:', error.response?.data || error.message)
  }
}

const startEdit = (comment) => {
  editingCommentId.value = comment.id
  editingCommentContent.value = comment.content
}

const cancelEdit = () => {
  editingCommentId.value = null
  editingCommentContent.value = ''
}

const updateComment = async (commentId) => {
  try {
    const response = await axios.put(`${store.API_URL}/community/${route.params.boardType}/comment/${commentId}/`, {
      content: editingCommentContent.value,
      post_id: route.params.post_id,
    }, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    const updatedComment = response.data
    const index = comments.value.findIndex(comment => comment.id === commentId)
    if (index !== -1) {
      comments.value[index] = updatedComment
    }
    cancelEdit()
    console.log('댓글 수정 성공')
  } catch (error) {
    console.error('댓글 수정 실패:', error.response?.data || error.message)
  }
}

const deleteComment = async (commentId) => {
  try {
    await axios.delete(`${store.API_URL}/community/${route.params.boardType}/comment/${commentId}/`, {
      headers: {
        Authorization: `Token ${store.token}` }
    })
    comments.value = comments.value.filter(comment => comment.id !== commentId)
    console.log('댓글 삭제 성공')
  } catch (error) {
    console.error('댓글 삭제 실패:', error.response?.data || error.message)
  }
}

onMounted(fetchComments)

watch([() => route.params.post_id, () => route.params.boardType], fetchComments)
</script>

<style scoped>
.app {
  padding: 20px;
}

.container {
  max-width: 800px;
  margin: 0 auto;
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
  margin-right: 10px;
}

.btn-sm {
  display: inline-block;
  background-color: lightgray;
  padding: 5px 10px;
  border-radius: 5px;
}

.btn-primary {
  background-color: rgb(83, 204, 168);
  color: white;
}

.btn-secondary {
  background-color: grey;
  color: white;
}

.btn-error {
  background-color: #FF4C4C;
  color: white;
}

.mt-2 {
  margin-top: 1rem;
}

.comment-list {
  margin-top: 2rem;
}

.list-item {
  border: 1px solid #ddd;
  border-radius: 8px;
  margin-bottom: 10px;
  padding: 10px;
}

.list-item-content {
  display: block;
}

.list-item h4 {
  margin: 0 0 10px;
}

.list-item p {
  margin: 0 0 10px;
}
</style>
