<!-- <template>
    <div v-if="post">
      <h1>{{ post.title }}</h1>
      <p v-if="post.image_url">
        <img :src="post.image_url" alt="Post Image" width="100px" height="100px">
      </p>
    </div>
  </template>
  
  <script setup>
  import axios from 'axios'
  import { onMounted, ref } from 'vue'
  import { useCounterStore } from '@/stores/counter'
  import { useRoute } from 'vue-router'
  
  const store = useCounterStore()
  const route = useRoute()
  const post = ref(null)
  
  onMounted(() => {
    axios({
      method: 'get',
      url: `${store.API_URL}/community/post/${route.params.post_id}/`
    })
    .then((response) => {
      post.value = response.data
      console.log(response.data)
    })
    .catch((error) => {
      console.log(error)
      console.log(`${store.API_URL}/community/post/${route.params.post_id}`)
      console.log(error.response ? error.response.data : error.message)
    })
  })
  </script>
  
  <style scoped>
  </style>
   -->

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
              </div>
            </v-card>
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
  
  const store = useCounterStore()
  const route = useRoute()
  const router = useRouter()
  const post = ref(null)
  
  const fetchPost = async () => {
    try {
      const response = await axios.get(`${store.API_URL}/community/post/${route.params.post_id}/`)
      post.value = response.data
    } catch (error) {
      console.error(error)
    }
  }
  
  const editPost = () => {
    router.push({ name: 'post_update', params: { post_id: route.params.post_id } })
  }


  const goToPostList = () => {
    router.push({ name: 'community' })
  }
  
  
  const deletePost = function () {
    axios({
        method: 'delete',
        url: `${store.API_URL}/community/post/${route.params.post_id}/`,
        headers: {
            Authorization: `Token ${store.token}`
        }
    })
    .then((res) => {
        console.log('게시글 삭제')
        router.push({name: 'community'})
    })
    .catch((err) => {
        console.log(err)
    })
}
  
  onMounted(fetchPost)
  </script>
  
  <style scoped>
  </style>
  