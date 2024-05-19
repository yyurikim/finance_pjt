<template>
  <v-app>
    <v-container>
      <v-row justify="center">
        <v-col cols="12" md="8" lg="6">
          <v-btn
            v-for="(label, type) in boardTypes"
            :key="type"
            @click="fetchPosts(type)"
            class="mb-4"
          >
            {{ label }}
          </v-btn>
          <v-btn
            color="primary"
            class="mb-4"
            @click="goToCreatePost"
          >
            글쓰기
          </v-btn>
          <post-list :posts="posts" :boardType="currentBoardType"/>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useCommunityStore } from '@/stores/community';
import PostList from '@/components/community/PostList.vue';

export default {
  components: {
    PostList
  },
  setup() {
    const communityStore = useCommunityStore();
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
      goToCreatePost
    };
  }
};
</script>

<style scoped>
.v-btn {
  margin-right: 10px;
}
</style>


<!-- <template>
  <v-app>
    <v-container>
      <v-row justify="center">
        <v-col cols="12" md="8" lg="6">
          <v-btn
          v-for="(label, type) in boardTypes"
          :key="type"
          @click="fetchPosts(type)"
          class="mb-4"
          >
          {{ label }}
        </v-btn>
        <v-btn
          color="primary"
          class="mb-4"
          @click="goToCreatePost"
        >
          글쓰기
        </v-btn>
          <post-list :posts="posts" :boardType="currentBoardType"/>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useCommunityStore } from '@/stores/community';
import PostList from '@/components/community/PostList.vue';

export default {
  components: {
    PostList
  },
  setup() {
    const communityStore = useCommunityStore();
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
      if (boardType === 'all') {
        // Fetch all posts from all categories
        let allPosts = [];
        for (let type in boardTypes) {
          if (type !== 'all') {
            const response = await communityStore.fetchPosts(type);
            allPosts = allPosts.concat(response.data);
          }
        }
        posts.value = allPosts;
      } else {
        const response = await communityStore.fetchPosts(boardType);
        posts.value = response.data;
      }
    };

    const goToCreatePost = () => {
      router.push({ name: 'post_create' });
    };

    onMounted(() => fetchPosts('all'));

    return {
      posts,
      boardTypes,
      currentBoardType,
      fetchPosts,
      goToCreatePost
    };
  }
};
</script>

<style scoped>
.v-btn {
  margin-right: 10px;
}
</style> -->


<!-- <template>
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
import { ref, onMounted, watch } from 'vue';
import { useRouter } from 'vue-router';
import { useCommunityStore } from '@/stores/community';

export default {
  props: {
    boardType: {
      type: String,
      required: true
    }
  },
  setup(props) {
    const communityStore = useCommunityStore();
    const router = useRouter();
    const posts = ref([]);

    const fetchPosts = async () => {
      try {
        const response = await communityStore.fetchPosts(props.boardType);
        posts.value = communityStore.posts[props.boardType];
      } catch (error) {
        console.error(error);
      }
    };

    onMounted(fetchPosts);
    watch(() => props.boardType, fetchPosts);  // boardType이 변경될 때마다 게시글을 다시 불러옵니다.

    const goToPostDetail = (postId) => {
      router.push({ name: 'post_detail', params: { post_id: postId } });
    };

    const goToCreatePost = () => {
      router.push({ name: 'post_create', params: { boardType: props.boardType } });
    };

    return {
      posts,
      goToPostDetail,
      goToCreatePost
    };
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
</style> -->





<!-- <template>
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
  
  
 -->

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