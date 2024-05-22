<template>
  <div v-if="post">
    <v-btn :class="{'active-vote': userVoted === 'buyit'}" color="success" @click="vote('buyit')">
      사세요 {{ post.buyit.length }}
    </v-btn>
    <v-btn :class="{'active-vote': userVoted === 'dontbuyit'}" color="warning" @click="vote('dontbuyit')">
      사지 마세요 {{ post.dontbuyit.length }}
    </v-btn>
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter';
import axios from 'axios';

const props = defineProps({
  post: { type: Object, required: true },
  postId: { type: String, required: true },
  boardType: { type: String, required: true },
});

const emit = defineEmits(['updatePost']);
const store = useCounterStore();
const userVoted = ref(null);

const setUserVote = () => {
  if (props.post.user_vote) {
    userVoted.value = props.post.user_vote;
  } else {
    userVoted.value = null;
  }
};

const vote = async (type) => {
  try {
    const url = `${store.API_URL}/community/consumer/${props.postId}/${type}/`;
    const response = await axios.post(url, {}, { headers: { Authorization: `Token ${store.token}` } });
    console.log('Vote response:', response.data);
    emit('updatePost', response.data);
    userVoted.value = type;
  } catch (error) {
    console.error(error);
  }
};

watch(
  () => props.post,
  (newPost) => {
    if (newPost) {
      // 기본값 설정
      newPost.buyit = newPost.buyit || [];
      newPost.dontbuyit = newPost.dontbuyit || [];
      setUserVote();
      // 좋아요/싫어요 수가 업데이트 되었는지 확인
      console.log('Post votes updated:', newPost.buyit, newPost.dontbuyit);
    }
  },
  { immediate: true }
);

onMounted(() => {
  setUserVote();
});
</script>

<style scoped>
.active-vote {
  font-weight: bold;
}
</style>


<!-- <template>
  <div>
    <v-btn :class="{'active-vote': userVoted === 'buyit'}" color="success" @click="vote('buyit')">
      사세요 {{ post.buyit ? post.buyit.length : 0 }}
    </v-btn>
    <v-btn :class="{'active-vote': userVoted === 'dontbuyit'}" color="warning" @click="vote('dontbuyit')">
      사지 마세요 {{ post.dontbuyit ? post.dontbuyit.length : 0 }}
    </v-btn>
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import axios from 'axios'

// Props 정의
const props = defineProps({
  post: {
    type: Object,
    required: true
  },
  postId: {
    type: String,
    required: true
  },
  boardType: {
    type: String,
    required: true
  }
})

// Emits 정의
const emit = defineEmits(['updatePost'])

// Store 및 기타 변수 초기화
const store = useCounterStore()
const userVoted = ref(null)


const setUserVote = () => {
  if (props.post.userVote) {
    userVoted.value = props.post.userVote
  } else {
    userVoted.value = null
  }
}

// 투표 함수 정의
const vote = async (type) => {
  try {
    const url = `${store.API_URL}/community/consumer/${props.postId}/${type}/`
    const response = await axios.post(url, {}, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    // 투표 후 응답 데이터로 post 객체 업데이트
    console.log('Vote response:', response.data)
    emit('updatePost', response.data)
    userVoted.value = type
  } catch (error) {
    console.error(error)
  }
}

let post = ref(null)

onMounted(async () => {
  const response = await axios.get(`/api/posts/${props.postId}`)
  post.value = response.data
})

onMounted(() => {
  setUserVote()
})

// watch(() => props.post, (newPost) => {
//   if (newPost.userVote) {
//     userVoted.value = newPost.userVote
//   } else {
//     userVoted.value = null
//   }
// })

watch(() => props.post, (newPost) => {
  setUserVote()
})
</script>

<style scoped>
.active-vote {
  font-weight: bold;
}
</style> -->
<!-- <script setup>
import { ref, watch, onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter';
import axios from 'axios';

const props = defineProps({
  post: { type: Object, required: true },
  postId: { type: String, required: true },
  boardType: { type: String, required: true },
});

const emit = defineEmits(['updatePost']);
const store = useCounterStore();
const userVoted = ref(null);

const setUserVote = () => {
  if (props.post.user_vote) {
    userVoted.value = props.post.user_vote;
  } else {
    userVoted.value = null;
  }
};

const vote = async (type) => {
  try {
    const url = `${store.API_URL}/community/consumer/${props.postId}/${type}/`;
    const response = await axios.post(url, {}, { headers: { Authorization: `Token ${store.token}` } });
    console.log('Vote response:', response.data);
    emit('updatePost', response.data);
    userVoted.value = type;
  } catch (error) {
    console.error(error);
  }
};

watch(
  () => props.post,
  (newPost) => {
    if (newPost) {
      // 기본값 설정
      newPost.buyit = newPost.buyit || [];
      newPost.dontbuyit = newPost.dontbuyit || [];
      setUserVote();
      // 좋아요/싫어요 수가 업데이트 되었는지 확인
      console.log('Post votes updated:', newPost.buyit, newPost.dontbuyit);
    }
  },
  { immediate: true }
);

onMounted(() => {
  setUserVote();
});
</script>

<style scoped>
.vote-btn {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  color: white;
  cursor: pointer;
  font-size: 16px;
  margin: 5px;
  transition: background-color 0.3s ease;
}

.success {
  background-color: #4CAF50; /* Green */
}

.warning {
  background-color: #FFC107; /* Amber */
}

.active-vote {
  box-shadow: 0px 0px 12px rgba(0,0,0,0.2);
}

.vote-btn:hover {
  opacity: 0.9;
}

</style> -->


<!-- <template>
  <div>
    <v-btn :class="{'active-vote': userVoted === 'buyit'}" color="success" @click="vote('buyit')">
      사세요 {{ post.buyit ? post.buyit.length : 0 }}
    </v-btn>
    <v-btn :class="{'active-vote': userVoted === 'dontbuyit'}" color="warning" @click="vote('dontbuyit')">
      사지 마세요 {{ post.dontbuyit ? post.dontbuyit.length : 0 }}
    </v-btn>
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import axios from 'axios'

// Props 정의
const props = defineProps({
  post: {
    type: Object,
    required: true
  },
  postId: {
    type: String,
    required: true
  },
  boardType: {
    type: String,
    required: true
  }
})

// Emits 정의
const emit = defineEmits(['updatePost'])

// Store 및 기타 변수 초기화
const store = useCounterStore()
const userVoted = ref(null)


const setUserVote = () => {
  if (props.post.userVote) {
    userVoted.value = props.post.userVote
  } else {
    userVoted.value = null
  }
}

// 투표 함수 정의
const vote = async (type) => {
  try {
    const url = `${store.API_URL}/community/consumer/${props.postId}/${type}/`
    const response = await axios.post(url, {}, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    // 투표 후 응답 데이터로 post 객체 업데이트
    console.log('Vote response:', response.data)
    emit('updatePost', response.data)
    userVoted.value = type
  } catch (error) {
    console.error(error)
  }
}

let post = ref(null)

onMounted(async () => {
  const response = await axios.get(`/api/posts/${props.postId}`)
  post.value = response.data
})

onMounted(() => {
  setUserVote()
})

// watch(() => props.post, (newPost) => {
//   if (newPost.userVote) {
//     userVoted.value = newPost.userVote
//   } else {
//     userVoted.value = null
//   }
// })

watch(() => props.post, (newPost) => {
  setUserVote()
})
</script>

<style scoped>
.active-vote {
  font-weight: bold;
}
</style> -->
