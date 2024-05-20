
<template>
  <v-app>
    <v-container class="d-flex align-center justify-center" style="height: 100vh;">
      <v-row>
        <v-col cols="12" md="8" lg="6">
          <v-btn color="primary" class="mb-4" @click="goToPostList">목록으로 돌아가기</v-btn>
          <v-card class="pa-5">
            <div v-if="post">
              <v-card-title>{{ post.title }}</v-card-title>
              <v-card-subtitle>작성자: {{ post.user_name }}</v-card-subtitle>
              <v-card-subtitle>작성 시간: {{ new Date(post.created_at).toLocaleString() }}</v-card-subtitle>
              <v-card-text>{{ post.content }}</v-card-text>
              <div v-if="post.image_url">
                <v-img :src="post.image_url" alt="Post Image" width="300px" height="300px"></v-img>
              </div>
              <v-card-actions>
                <v-btn color="primary" @click="editPost">수정</v-btn>
                <v-btn color="error" @click="deletePost">삭제</v-btn>
              </v-card-actions>
              <div v-if="route.params.boardType === 'consumer' && post">
                <!-- <v-btn color="success" @click="vote('buyit')">사세요 {{ post.buyit ? post.buyit.length : 0 }}</v-btn>
                <v-btn color="warning" @click="vote('dontbuyit')">사지 마세요 {{ post.dontbuyit ? post.dontbuyit.length : 0 }}</v-btn> -->
                <v-btn :class="{'active-vote': userVoted === 'buyit'}" color="success" @click="vote('buyit')">
                  사세요 {{ post.buyit ? post.buyit.length : 0 }}
                </v-btn>
                <v-btn :class="{'active-vote': userVoted === 'dontbuyit'}" color="warning" @click="vote('dontbuyit')">
                  사지 마세요 {{ post.dontbuyit ? post.dontbuyit.length : 0 }}
                </v-btn>
              </div>
            </div>
          </v-card>
          <CommentSection :comments="comments" @commentCreated="handleCommentCreated" />
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import axios from 'axios'
import CommentSection from '@/components/community/CommentSection.vue'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const post = ref(null)
const comments = ref([])
const userVoted = ref(null)
const currentUserId = ref(store.userInfo)


const fetchPost = async () => {
  try {
    const response = await axios.get(`${store.API_URL}/community/${route.params.boardType}/${route.params.post_id}/`)
    post.value = response.data
    console.log(currentUserId)
  } catch (error) {
    console.error(error)
  }
}

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

const handleCommentCreated = (newComment) => {
  comments.value.push(newComment)
}

const editPost = () => {
  router.push({ name: 'post_update', params: { boardType: route.params.boardType, post_id: route.params.post_id } })
}

const goToPostList = () => {
  router.push({ name: 'community', params: { boardType: route.params.boardType } })
}

const deletePost = async () => {
  try {
    await axios.delete(`${store.API_URL}/community/${route.params.boardType}/${route.params.post_id}/`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    console.log('게시글 삭제')
    router.push({ name: 'community', params: { boardType: route.params.boardType } })
  } catch (error) {
    console.error(error)
  }
}

const vote = async (type) => {
  try {
    const url = `${store.API_URL}/community/consumer/${route.params.post_id}/${type}/`
    const response = await axios.post(url, {}, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    post.value = response.data
    userVoted.value = type
    console.log(response.data)
  } catch (error) {
    console.error(error)
  }
}


onMounted(() => {
  fetchPost()  
  fetchComments(),
  currentUserId
})
</script>

<style scoped>

</style>