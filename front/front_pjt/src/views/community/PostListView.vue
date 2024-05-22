<template>
  <div class="app">
    <h1 class="title">커뮤니티</h1>
    <div class="container">
      <div class="row justify-center">
        <div class="column col-12">
          <div class="button-group">
            <button
              v-for="(label, type) in boardTypes"
              :key="type"
              @click="fetchPosts(type)"
              class="btn mb-4 board-btn"
            >
              {{ label }}
            </button>
            <button
              v-if="store.isLogin"
              class="btn btn-primary mb-4 write-btn"
              @click="goToCreatePost"
            >
              글쓰기
            </button>
          </div>
          <post-list :posts="posts" :boardType="currentBoardType"/>
        </div>
      </div>
    </div>
  </div>
</template>





<script>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useCommunityStore } from '@/stores/community';
import { useCounterStore } from '@/stores/counter';
import PostList from '@/components/community/PostList.vue';

export default {
  components: {
    PostList
  },
  setup() {
    const communityStore = useCommunityStore();
    const store = useCounterStore();
    const router = useRouter();
    const posts = ref([]);
    const currentBoardType = ref('bulletin');
    const boardTypes = {
      'bulletin': '자유게시판',
      'consumer': '소비게시판',
      'challenge': '7일 소비생활 챌린지'
    };


    const fetchPosts = async (boardType) => {
      currentBoardType.value = boardType;
      const response = await communityStore.fetchPosts(boardType);
      posts.value = response.data;
    };

    const goToCreatePost = () => {
      router.push({ name: 'post_create' });
    };

    onMounted(() => fetchPosts(currentBoardType.value));

    return {
      posts,
      boardTypes,
      currentBoardType,
      fetchPosts,
      goToCreatePost,
      store,
    };
  }
};
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

.button-group {
  display: flex;
  justify-content: space-between;
  flex-wrap: nowrap;
  gap: 10px;
}

.board-btn {
  flex: 1;
  padding: 10px 20px;
  background-color: white;
  color: #000;
  border-radius: 5px;
  cursor: pointer;
  text-align: center;
  font-size: 0.9rem;
}

.board-btn:hover {
  background-color: #e0e0e0;
}

.write-btn {
  padding: 10px 20px;
  background-color: rgb(83, 204, 168);
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  text-align: center;
}

.mb-4 {
  margin-bottom: 1.5rem;
}

.title {
  margin-top:30px;
  margin-bottom: 10px;
}
</style>

