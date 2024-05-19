<template>
    <v-list>
      <v-list-item
        v-for="comment in comments"
        :key="comment.id"
        class="list-item"
      >
        <v-list-item-content>
          <template v-if="editingCommentId === comment.id">
            <v-textarea
              v-model="editingCommentContent"
              outlined
              dense
            ></v-textarea>
            <v-btn icon @click="updateComment(comment.id)">
              <v-icon>mdi-check</v-icon>
            </v-btn>
            <v-btn icon @click="cancelEdit">
              <v-icon>mdi-cancel</v-icon>
            </v-btn>
          </template>
          <template v-else>
            <v-list-item-title>{{ comment.user_name }}</v-list-item-title>
            <v-list-item-subtitle>{{ comment.content }}</v-list-item-subtitle>
            <v-list-item-subtitle>{{ new Date(comment.created_at).toLocaleString() }}</v-list-item-subtitle>
            <v-btn icon @click="startEdit(comment)">
              <v-icon>mdi-pencil</v-icon>
            </v-btn>
            <v-btn icon @click="deleteComment(comment.id)">
              <v-icon>mdi-delete</v-icon>
            </v-btn>
          </template>
        </v-list-item-content>
      </v-list-item>
      <v-list-item v-if="comments.length === 0">
        <v-list-item-content>
          <v-list-item-title>댓글이 없습니다.</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </template>
  
  <script setup>
  import { ref, onMounted, watch } from 'vue'
  import { useRoute } from 'vue-router'
  import axios from 'axios'
  import { useCounterStore } from '@/stores/counter'
  
  const store = useCounterStore()
  const route = useRoute()
  const comments = ref([])
  
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
          Authorization: `Token ${store.token}`
        }
      })
      comments.value = comments.value.filter(comment => comment.id !== commentId)
      console.log('댓글 삭제 성공')
    } catch (error) {
      console.error('댓글 삭제 실패:', error.response?.data || error.message)
    }
  }
  
  onMounted(fetchComments)
  
  // watch를 통해 route.params.post_id와 route.params.boardType이 변경될 때마다 fetchComments 호출
//   watch([() => route.params.post_id, () => route.params.boardType], fetchComments)
watch(comments, fetchComments) 
 </script>
  
  <style scoped>
  .list-item {
    border: 1px solid #ddd;
    border-radius: 8px;
    margin-bottom: 10px;
    padding: 10px;
  }
  </style>
  

<!-- <template>
    <v-list>
      <v-list-item
        v-for="comment in comments"
        :key="comment.id"
        class="list-item"
      >
        <v-list-item-content>
          <template v-if="editingCommentId === comment.id">
            <v-textarea
              v-model="editingCommentContent"
              outlined
              dense
            ></v-textarea>
            <v-btn icon @click="updateComment(comment.id)">
              <v-icon>mdi-check</v-icon>
            </v-btn>
            <v-btn icon @click="cancelEdit">
              <v-icon>mdi-cancel</v-icon>
            </v-btn>
          </template>
          <template v-else>
            <v-list-item-title>{{ comment.user_name }}</v-list-item-title>
            <v-list-item-subtitle>{{ comment.content }}</v-list-item-subtitle>
            <v-list-item-subtitle>{{ new Date(comment.created_at).toLocaleString() }}</v-list-item-subtitle>
            <v-btn icon @click="startEdit(comment)">
              <v-icon>mdi-pencil</v-icon>
            </v-btn>
            <v-btn icon @click="deleteComment(comment.id)">
              <v-icon>mdi-delete</v-icon>
            </v-btn>
          </template>
        </v-list-item-content>
      </v-list-item>
      <v-list-item v-if="comments.length === 0">
        <v-list-item-content>
          <v-list-item-title>댓글이 없습니다.</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </template>
  
  <script setup>
  import { ref, onMounted, watch } from 'vue'
  import { useRoute } from 'vue-router'
  import axios from 'axios'
  import { useCounterStore } from '@/stores/counter'
  
  const store = useCounterStore()
  const route = useRoute()
  const comments = ref([])
  
  const editingCommentId = ref(null)
  const editingCommentContent = ref('')
  
  const fetchComments = async () => {
    try {
      const response = await axios.get(`${store.API_URL}/community/bulletin/${route.params.post_id}/comment/`, {
        headers: {
          Authorization: `Token ${store.token}`
        }
      })
      comments.value = response.data
    } catch (error) {
      console.error('댓글 조회 실패:', error.response?.data || error.message)
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
      const response = await axios.put(`${store.API_URL}/community/bulletin/comment/${commentId}/`, {
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
      await axios.delete(`${store.API_URL}/community/bulletin/comment/${commentId}/`, {
        headers: {
          Authorization: `Token ${store.token}`
        }
      })
      comments.value = comments.value.filter(comment => comment.id !== commentId)
      console.log('댓글 삭제 성공')
    } catch (error) {
      console.error('댓글 삭제 실패:', error.response?.data || error.message)
    }
  }
  
  onMounted(fetchComments)
  
  // watch를 통해 props가 변경될 때마다 fetchComments 호출
  watch(comments, fetchComments)
  </script>
  
  <style scoped>
  .list-item {
    border: 1px solid #ddd;
    border-radius: 8px;
    margin-bottom: 10px;
    padding: 10px;
  }
  </style> -->
  
  

<!-- <template>
    <v-list>
      <v-list-item
        v-for="comment in comments"
        :key="comment.id"
        class="list-item"
      >
        <v-list-item-content>
          <template v-if="editingCommentId === comment.id">
            <v-textarea
              v-model="editingCommentContent"
              outlined
              dense
            ></v-textarea>
            <v-btn icon @click="updateComment(comment.id)">
              <v-icon>mdi-check</v-icon>
            </v-btn>
            <v-btn icon @click="cancelEdit">
              <v-icon>mdi-cancel</v-icon>
            </v-btn>
          </template>
          <template v-else>
            <v-list-item-title>{{ comment.user_name }}</v-list-item-title>
            <v-list-item-subtitle>{{ comment.content }}</v-list-item-subtitle>
            <v-list-item-subtitle>{{ new Date(comment.created_at).toLocaleString() }}</v-list-item-subtitle>
            <v-btn icon @click="startEdit(comment)">
              <v-icon>mdi-pencil</v-icon>
            </v-btn>
            <v-btn icon @click="deleteComment(comment.id)">
              <v-icon>mdi-delete</v-icon>
            </v-btn>
          </template>
        </v-list-item-content>
      </v-list-item>
      <v-list-item v-if="comments.length === 0">
        <v-list-item-content>
          <v-list-item-title>댓글이 없습니다.</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { useRoute } from 'vue-router'
  import axios from 'axios'
  import { useCounterStore } from '@/stores/counter'
  
  const store = useCounterStore()
  const route = useRoute()
  const comments = ref([])
  
  const editingCommentId = ref(null)
  const editingCommentContent = ref('')
  
  const fetchComments = async () => {
    try {
      const response = await axios.get(`${store.API_URL}/community/bulletin/${route.params.post_id}/comment/`, {
        headers: {
          Authorization: `Token ${store.token}`
        }
      })
      comments.value = response.data
      console.log(comments)
    } catch (error) {
      console.error('댓글 조회 실패:', error.response?.data || error.message)
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
      const response = await axios.put(`${store.API_URL}/community/bulletin/comment/${commentId}/`, {
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
      await axios.delete(`${store.API_URL}/community/bulletin/comment/${commentId}/`, {
        headers: {
          Authorization: `Token ${store.token}`
        }
      })
      comments.value = comments.value.filter(comment => comment.id !== commentId)
      console.log('댓글 삭제 성공')
    } catch (error) {
      console.error('댓글 삭제 실패:', error.response?.data || error.message)
    }
  }
  
  onMounted(fetchComments)
  </script>
  
  <style scoped>
  .list-item {
    border: 1px solid #ddd;
    border-radius: 8px;
    margin-bottom: 10px;
    padding: 10px;
  }
  </style> -->
  
<!-- <template>
    <v-list>
      <v-list-item
        v-for="comment in comments"
        :key="comment.id"
        class="list-item"
      >
        <v-list-item-content>
          <v-list-item-title>{{ comment.user.username }}</v-list-item-title>
          <v-list-item-subtitle>{{ comment.content }}</v-list-item-subtitle>
          <v-list-item-subtitle>{{ new Date(comment.created_at).toLocaleString() }}</v-list-item-subtitle>
          <v-btn icon @click="editComment(comment)">
            <v-icon>mdi-pencil</v-icon>
          </v-btn>
          <v-btn icon @click="deleteComment(comment.id)">
            <v-icon>mdi-delete</v-icon>
          </v-btn>
        </v-list-item-content>
      </v-list-item>
      <v-list-item v-if="comments.length === 0">
        <v-list-item-content>
          <v-list-item-title>댓글이 없습니다.</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { useRoute } from 'vue-router'
  import axios from 'axios'
  import { useCounterStore } from '@/stores/counter'
  
  const store = useCounterStore()
  const route = useRoute()
  const comments = ref([])
  
  const fetchComments = async () => {
    try {
      const response = await axios.get(`${store.API_URL}/community/bulletin/${route.params.post_id}/comment/`, {
        headers: {
          Authorization: `Token ${store.token}`
        }
      })
      comments.value = response.data
    } catch (error) {
      console.error('댓글 조회 실패:', error.response?.data || error.message)
    }
  }
  
  const editComment = (comment) => {
    // 댓글 수정 로직을 여기에 추가
    console.log('댓글 수정:', comment)
  }
  
  const deleteComment = async (commentId) => {
    try {
      await axios.delete(`${store.API_URL}/community/bulletin/comment/${commentId}/`, {
        headers: {
          Authorization: `Token ${store.token}`
        }
      })
      comments.value = comments.value.filter(comment => comment.id !== commentId)
      console.log('댓글 삭제 성공')
    } catch (error) {
      console.error('댓글 삭제 실패:', error.response?.data || error.message)
    }
  }
  
  onMounted(fetchComments)
  </script>
  
  <style scoped>
  .list-item {
    border: 1px solid #ddd;
    border-radius: 8px;
    margin-bottom: 10px;
    padding: 10px;
  }
  </style>
   -->