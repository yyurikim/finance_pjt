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
    
    emit('updatePost', response.data);

    if (type === 'buyit') {
      userVoted_buy.value = response.data.buyit ? response.data.buyit.length : 0;
      userVoted_dontbuy.value = response.data.dontbuyit ? response.data.dontbuyit.length : 0;
    } else if (type === 'dontbuyit') {
      userVoted_buy.value = response.data.buyit ? response.data.buyit.length : 0;
      userVoted_dontbuy.value = response.data.dontbuyit ? response.data.dontbuyit.length : 0;
    }
    
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