<template>
  <div v-if="post">
    <button
      :class="['btn', 'buyit', { 'active-vote': userVoted === 'buyit' }]"
      @click="vote('buyit')"
    >
      🤩사세요 {{ userVoted_buy }}
    </button>
    <button
      :class="['btn', 'dontbuyit', { 'active-vote': userVoted === 'dontbuyit' }]"
      @click="vote('dontbuyit')"
    >
      🙄사지 마세요 {{ userVoted_dontbuy }}
    </button>
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
const userVoted_buy = ref(null);
const userVoted_dontbuy = ref(null);
const userVoted = ref(null);

const setUserVote = async () => {
  try {
    const buyitUrl = `${store.API_URL}/community/consumer/${props.postId}/buyit/`;
    const dontbuyitUrl = `${store.API_URL}/community/consumer/${props.postId}/dontbuyit/`;

    const buyitResponse = await axios.get(buyitUrl, { headers: { Authorization: `Token ${store.token}` } });
    const dontbuyitResponse = await axios.get(dontbuyitUrl, { headers: { Authorization: `Token ${store.token}` } });

    console.log('Buyit response:', buyitResponse.data);
    console.log('Dontbuyit response:', dontbuyitResponse.data);

    if (buyitResponse.data.buyit) {
      userVoted_buy.value = buyitResponse.data.buyit.length;
      console.log('있다', userVoted_buy.value.length);
    }
    if (dontbuyitResponse.data.dontbuyit) {
      userVoted_dontbuy.value = dontbuyitResponse.data.dontbuyit.length;
      console.log('있다', userVoted_dontbuy.value.length);
    }

    // 현재 사용자가 투표한 상태를 설정
    if (userVoted_buy.value.length > 0) {
      userVoted.value = 'buyit';
    } else if (userVoted_dontbuy.value.length > 0) {
      userVoted.value = 'dontbuyit';
    } else {
      userVoted.value = null;
    }
    
    console.log('Vote status fetched:', userVoted.value);
  } catch (error) {
    console.error('Error fetching vote status:', error);
  }
};

const vote = async (type) => {
  try {
    const url = `${store.API_URL}/community/consumer/${props.postId}/${type}/`;
    const response = await axios.post(url, {}, { headers: { Authorization: `Token ${store.token}` } });
    
    // 업데이트 이벤트를 발생시키고, 로컬 상태를 업데이트합니다.
    emit('updatePost', response.data);

    // 응답에서 새로운 투표 수를 받아와 로컬 상태를 업데이트합니다.
    if (type === 'buyit') {
      userVoted_buy.value = response.data.buyit ? response.data.buyit.length : 0;
      userVoted_dontbuy.value = response.data.dontbuyit ? response.data.dontbuyit.length : 0;
    } else if (type === 'dontbuyit') {
      userVoted_buy.value = response.data.buyit ? response.data.buyit.length : 0;
      userVoted_dontbuy.value = response.data.dontbuyit ? response.data.dontbuyit.length : 0;
    }
    
    // 사용자의 현재 투표 상태를 업데이트합니다.
    userVoted.value = type;

  } catch (error) {
    console.error('Error posting vote:', error);
  }
};

watch(
  () => props.post,
  (newPost) => {
    if (newPost) {
      newPost.buyit = newPost.buyit || [];
      newPost.dontbuyit = newPost.dontbuyit || [];
      setUserVote();
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
.btn {
  background: none;
  border: none;
  font-size: 16px;
  cursor: pointer;
  padding: 10px 20px;
  margin: 0 10px;
  outline: none;
  transition: color 0.3s;
}

.btn:hover {
  text-decoration: underline;
}

.btn.buyit {
  color: #53cca8;
}

.btn.dontbuyit {
  color: #ff4c4c;
}

.btn.active-vote.buyit {
  color: #53cca8;
  font-weight: bold;
}

.btn.active-vote.dontbuyit {
  color: #ff4c4c;
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
