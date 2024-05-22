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
              <v-card-actions v-if="post.user_name===localUserName">
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
.active-vote {
  font-weight: bold;
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
