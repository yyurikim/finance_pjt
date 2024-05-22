<template>
  <div class="post-list">
    <div
      v-for="post in posts"
      :key="post.id"
      @click="goToPostDetail(post.id)"
      class="list-item"
    >
      <div class="list-item-content">
        <div class="text-content">
          <h3 class="list-item-title">{{ post.title }}</h3>
          <p class="list-item-subtitle">{{ post.content.substring(0, 50) }}</p>
          <p class="list-item-author">작성자: {{ post.user_name }}</p>
        </div>
        <div v-if="post.image_url" class="list-item-avatar">
          <img :src="post.image_url" alt="Post Image" width="70" height="70">
        </div>
      </div>
    </div>
  </div>
</template>



<script>
export default {
  props: {
    posts: {
      type: Array,
      required: true
    },
    boardType: {
      type: String,
      required: true
    }
  },
  methods: {
    goToPostDetail(postId) {
      this.$router.push({ name: 'post_detail', params: { boardType: this.boardType, post_id: postId } });
    }
  }
};
</script>

<style scoped>
.post-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.list-item {
  cursor: pointer;
  transition: background-color 0.3s;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 10px;
}

.list-item:hover {
  background-color: #f0f0f0;
}

.list-item-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.text-content {
  flex-grow: 1;
}

.list-item-title {
  font-size: 1.2rem;
  font-weight: bold;
  margin: 0;
  text-align: left; /* 왼쪽 정렬 */
}

.list-item-subtitle {
  margin: 10px 0;
  color: #666;
  text-align: left; /* 왼쪽 정렬 */
}

.list-item-author {
  margin: 0;
  color: #999;
  text-align: left; /* 왼쪽 정렬 */
}

</style>

