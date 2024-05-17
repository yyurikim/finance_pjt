<template>
    <v-app>
      <v-container>
        <v-row justify="center">
          <v-col cols="12" md="8" lg="6">
            <v-btn color="primary" class="mb-4" @click="goToCreatePost">글쓰기</v-btn>
            <v-list>
              <v-list-item
                v-for="post in posts"
                :key="post.id"
                @click="goToPostDetail(post.id)"
                class="list-item"
              >
                <v-list-item-content>
                  <v-list-item-title>{{ post.title }}</v-list-item-title>
                  <v-list-item-subtitle>
                    {{ post.content.substring(0, 50) }}...
                  </v-list-item-subtitle>
                  <v-list-item-avatar v-if="post.image_url" class="mt-2">
                    <v-img :src="post.image_url" alt="Post Image" width="50" height="50"></v-img>
                  </v-list-item-avatar>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-col>
        </v-row>
      </v-container>
    </v-app>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  import { useCommunityStore } from '@/stores/community';
  
  export default {
    setup() {
      const posts = ref([]);
      const communityStore = useCommunityStore();
      const router = useRouter();
  
      onMounted(async () => {
        try {
          const response = await communityStore.fetchPosts();
          posts.value = response.data;
        } catch (error) {
          console.error(error);
        }
      });
  
      const goToPostDetail = (postId) => {
        router.push({ name: 'post_detail', params: { post_id: postId } });
      };
  
      const goToCreatePost = () => {
        router.push({ name: 'post_create' });
      };
  
      return {
        posts,
        goToPostDetail,
        goToCreatePost
      };
    },
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
  
  .v-list-item-title {
    font-weight: bold;
  }
  
  .v-list-item-subtitle {
    color: #666;
    margin-top: 5px;
  }
  
  .v-list-item-avatar {
    margin-top: 10px;
  }
  </style>
  
  


<!-- <template>
    <div>
        <ul>
            <li v-for="post in posts" :key="post.id">
                {{ post.title }}
            </li>
        </ul>
    </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { useCommunityStore } from '@/stores/community';

export default {
    setup() {
        const posts = ref([]);
        const communityStore = useCommunityStore();
        const route = useRoute();
        const router = useRouter();

        onMounted(async () => {
            try {
                // Make an API call to fetch the posts
                const response = await communityStore.fetchPosts();
                posts.value = response.data; // Assuming the response contains an array of posts
            } catch (error) {
                console.error(error);
            }
        });

        return {
            posts,
        };
    },
};
</script> -->