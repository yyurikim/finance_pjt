<template>
  <div class="app">
    <div class="container">
      <div class="row align-center justify-center" style="height: 100vh;">
        <div class="column col-12">
          <div class="button-group">
            <button class="btn" @click="goToPostList">목록으로 돌아가기</button>
            </div>          
            <div class="card pa-5">
            <div v-if="post">
              <h2 class="card-title">{{ post.title }}</h2>
              <p class="card-subtitle">작성자: {{ post.user_name }}</p>
              <p class="card-subtitle">작성 시간: {{ new Date(post.created_at).toLocaleString() }}</p>
              <p class="card-text">{{ post.content }}</p>
              <div v-if="post.image_url" class="card-image">
                <img :src="post.image_url" alt="Post Image" width="300px" height="300px">
              </div>
              <div class="card-actions" v-if="post.user_name === localUserName">
                <button class="btn btn-primary" @click="editPost">수정</button>
                <button class="btn btn-error" @click="deletePost">삭제</button>
              </div>
              <div v-if="route.params.boardType === 'consumer' && post">
                <VoteButtons :post="post" :postId="route.params.post_id" :boardType="route.params.boardType" @updatePost="handlePostUpdate" />
              </div>
            </div>
          </div>
          <CommentSection :comments="comments" @commentCreated="handleCommentCreated" />
        </div>
      </div>
    </div>
  </div>
</template>



<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useCounterStore } from '@/stores/counter';
import axios from 'axios';
import CommentSection from '@/components/community/CommentSection.vue';
import VoteButtons from '@/components/community/VoteButtons.vue';

const store = useCounterStore();
const route = useRoute();
const router = useRouter();
const post = ref(null);
const comments = ref([]);
const currentUserId = ref(store.userInfo);
const localUserName = localStorage.getItem('username');


const fetchPost = async () => {
  try {
    const response = await axios.get(`${store.API_URL}/community/${route.params.boardType}/${route.params.post_id}/`);
    console.log('Fetch post response:', response.data);
    const data = response.data;
    data.buyit = data.buyit;
    data.dontbuyit = data.dontbuyit;
    post.value = data;

    console.log(data)
    // 추가된 코드
    if (post.value) {
      // 값이 제대로 나올 때까지 기다리는 동안 로딩 상태를 표시
      post.value.loading = true;
    }

    // 초기화 후, post 데이터가 설정된 후에 userVote를 설정
    if (data.user_vote) {
      post.value.user_vote = data.user_vote;
    }
  } catch (error) {
    console.error(error);
  }
};

const fetchComments = async () => {
  try {
    const response = await axios.get(`${store.API_URL}/community/${route.params.boardType}/${route.params.post_id}/comment/`, { headers: { Authorization: `Token ${store.token}` } });
    comments.value = response.data;
  } catch (error) {
    console.error('댓글 조회 실패:', error.response?.data || error.message);
  }
};

const handleCommentCreated = (newComment) => {
  comments.value.push(newComment);
};

const editPost = () => {
  router.push({ name: 'post_update', params: { boardType: route.params.boardType, post_id: route.params.post_id } });
};

const goToPostList = () => {
  router.push({ name: 'community', params: { boardType: route.params.boardType } });
};

const deletePost = async () => {
  try {
    await axios.delete(`${store.API_URL}/community/${route.params.boardType}/${route.params.post_id}/`, { headers: { Authorization: `Token ${store.token}` } });
    console.log('게시글 삭제');
    router.push({ name: 'community', params: { boardType: route.params.boardType } });
  } catch (error) {
    console.error(error);
  }
};

const handlePostUpdate = (updatedPost) => {
  Object.assign(post.value, updatedPost);
  console.log('Post updated:', post.value);
};

onMounted(async () => {
  await fetchPost();
  await fetchComments();
});
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
}

.card-title {
  font-size: 1.5rem;
  font-weight: bold;
  margin-bottom: 10px;
}

.card-subtitle {
  color: #666;
  margin-bottom: 10px;
}

.card-text {
  margin-bottom: 10px;
}

.card-image img {
  display: block;
  margin: 10px auto;
  border-radius: 10px;
}

.card-actions {
  display: flex;
  justify-content: flex-end; /* 버튼들을 오른쪽으로 정렬 */
  gap: 10px; /* 버튼 간격 추가 */
  margin-top: 10px;
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
  background-color: rgb(93, 135, 212);
  color: white;
}

.btn-error {
  background-color: #FF4C4C;
  color: white;
}

.mb-4 {
  margin-bottom: 1.5rem;
}

.pa-5 {
  padding: 20px;
}

.button-group {
  display: flex;
  justify-content: flex-start; /* 왼쪽 정렬 */
  margin-bottom: 20px;
}
</style>



<!-- <template>
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
                <VoteButtons :post="post" :postId="route.params.post_id" :boardType="route.params.boardType" @updatePost="handlePostUpdate" />
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
import VoteButtons from '@/components/community/VoteButtons.vue'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const post = ref(null)
const comments = ref([])
const currentUserId = ref(store.userInfo)

const fetchPost = async () => {
  try {
    const response = await axios.get(`${store.API_URL}/community/${route.params.boardType}/${route.params.post_id}/`)
    console.log('Fetch post response:', response.data)
    post.value = response.data
    // 초기화 후, post 데이터가 설정된 후에 userVote를 설정
    if (response.data.user_vote) {
      post.value.user_vote = response.data.user_vote
    }
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

const handlePostUpdate = (updatedPost) => {
  Object.assign(post.value, updatedPost)
  console.log('Post updated:', post.value)
}

onMounted(async () => {
  await fetchPost()
  await fetchComments()
})
</script>

<style scoped>
.active-vote {
  font-weight: bold;
}
</style> -->
