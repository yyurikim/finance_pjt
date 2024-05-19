<template>
  <v-list>
    <v-list-item
      v-for="post in posts"
      :key="post.id"
      @click="goToPostDetail(post.id)"
      class="list-item"
    >
      <v-list-item-content>
        <v-list-item-title>{{ post.title }}</v-list-item-title>
        <v-list-item-subtitle>{{ post.content.substring(0, 50) }}...</v-list-item-subtitle>
        <v-list-item-avatar v-if="post.image_url" class="mt-2">
          <v-img :src="post.image_url" alt="Post Image" width="50" height="50"></v-img>
        </v-list-item-avatar>
      </v-list-item-content>
    </v-list-item>
  </v-list>
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
.list-item {
  cursor: pointer;
  transition: background-color 0.3s;
  border: 1px solid #ddd;
  border-radius: 8px;
  margin-bottom: 10px;
  padding: 10px;
}

.list-item:hover {
  background-color: #f0f0f0;
}
</style>
