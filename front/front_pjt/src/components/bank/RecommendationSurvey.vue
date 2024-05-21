<template>
  <div v-if="data">
    {{ data }}
    <v-row>
      <v-tabs v-model="selectedTerm" background-color="white" slider-color="blue">
        <v-tab key="6" @click="setTerm(6)" :class="{'active-tab': selectedTerm === 6}">6개월</v-tab>
        <v-tab key="12" @click="setTerm(12)" :class="{'active-tab': selectedTerm === 12}">12개월</v-tab>
        <v-tab key="24" @click="setTerm(24)" :class="{'active-tab': selectedTerm === 24}">24개월</v-tab>
        <v-tab key="36" @click="setTerm(36)" :class="{'active-tab': selectedTerm === 36}">36개월</v-tab>
      </v-tabs>
    </v-row>
    <v-row>
      <v-col cols="12" md="6">
        <v-card>
          <v-card-title><strong>예금 추천상품</strong></v-card-title>
          <v-list>
            <v-list-item v-for="(product, index) in data[`${selectedTerm}개월`].deposits.slice(0, 5)" :key="index" @click="openDialog(product)">
              <v-list-item-content>
                <v-list-item-title>{{ product.fin_prdt_nm }}</v-list-item-title>
                <v-list-item-subtitle>{{ product.kor_co_nm }}</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-list>
        </v-card>
      </v-col>
      <v-col cols="12" md="6">
        <v-card>
          <v-card-title><strong>적금 추천상품</strong></v-card-title>
          <v-list>
            <v-list-item v-for="(product, index) in data[`${selectedTerm}개월`].savings.slice(0, 5)" :key="index" @click="openDialog(product)">
              <v-list-item-content>
                <v-list-item-title>{{ product.fin_prdt_nm }}</v-list-item-title>
                <v-list-item-subtitle>{{ product.kor_co_nm }}</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-list>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-card>
          <v-card-title>고객님의 소비 성향({{ usertype }})에 맞는 상품을 추천했어요 </v-card-title>
          <v-card-text>
            <p>1. {{ savingType }}</p>
            <p>2. {{ meaningoutType }}</p>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-dialog v-model="dialog" persistent max-width="600px">
      <v-card>
        <v-card-title class="text-h5">{{ dialogProduct.fin_prdt_nm }}</v-card-title>
        <v-card-text>
          <p><strong>은행명</strong></p>
          <p>{{ dialogProduct.kor_co_nm }}</p>
          <p><strong>금리</strong></p>
          <p><strong>우대조건</strong></p>
          <p>{{ dialogProduct.spcl_cnd }}</p>
          <p><strong>기타 유의사항</strong></p>
          <p>{{ dialogProduct.etc_note }}</p>
          <!-- 다른 필요한 정보 추가 -->
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="dialog = false">닫기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>


<script setup>
import { ref, onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter';
import axios from 'axios';

const store = useCounterStore();
const URL = `${store.API_URL}/banks/recommendation_by_survey/`;
const data = ref(null);
const savings = ref([]);
const deposits = ref([]);
const dialogProduct = ref({});
const dialog = ref(false);


const error = ref(null);
const usertype = ref(null);
const savingType = ref('');
const meaningoutType = ref('');
const selectedTerm = ref(6); // 기본값으로 6개월 설정

const setTerm = (term) => {
  selectedTerm.value = term;
};

const openDialog = (product) => {
  dialogProduct.value = product;
  dialog.value = true;
};

onMounted(async () => {
  try {
    const response = await axios.get(URL, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    });
    data.value = response.data;
    savings.value = response.data.savings || [];
    deposits.value = response.data.deposits || [];
    usertype.value = response.data.user_type;
    savingType.value = (usertype.value === 'EIG' || usertype.value === 'EIV' || usertype.value === 'FIG' || usertype.value === 'FIV') ? '자유로운 소비를 추구하는 고객님의 성향에 맞는 자유적립식 상품을 추천했어요' : '계획적인 소비를 추구하는 고객님의 성향에 맞는 정액적립식 상품을 추천했어요';
    meaningoutType.value = (usertype.value === 'EIG' || usertype.value === 'FIG' || usertype.value === 'ERG' || usertype.value === 'FRG') ? '합리적인 소비에 맞는 합리적 재태크를 위해 높은 이율의 상품을 추천했어요' : '재태크와 함께 우리 사회도 챙길 수 있는 상품을 추천했어요';
  } catch (err) {
    console.error('Error fetching data:', err);
    if (err.response) {
      error.value = `Error: ${err.response.status} - ${err.response.statusText}`;
    } else if (err.request) {
      error.value = 'No response received from server';
    } else {
      error.value = `Request error: ${err.message}`;
    }
  }
});
</script>

<style scoped>
.active-tab {
  background-color: rgb(182, 223, 236); /* Deep purple background for active tabs */
  color: white; /* White text for active tabs */
}
</style>
<!-- <template>

  <div>
    <div v-if="data">
      <h3>적금 추천상품:</h3>
      <ul>
        <li v-for="(product, index) in data['36개월'].savings.slice(0, 3)" :key="index">
          {{ product.fin_prdt_nm }} - {{ product.kor_co_nm }}
        </li>
      </ul>
      <h3>예금 추천상품:</h3>
      <ul>
        <li v-for="(product, index) in data['36개월'].deposits.slice(0, 3)" :key="index">
          {{ product.fin_prdt_nm }} - {{ product.kor_co_nm }}
        </li>
      </ul>
    </div>
    <br>
    <div>
      <p>고객님의 소비 성향({{ usertype }})에 맞게 추천된 상품들이에요!</p>
      <ul>
        <li>{{ savingType }}</li>
        <li>{{ meaningoutType }}</li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter';
import axios from 'axios';

const store = useCounterStore()
const URL = `${store.API_URL}/banks/recommendation_by_survey/`
const data = ref(null);
const savings = ref([]);
const deposits = ref([]);
const error = ref(null);
const usertype = ref(null)
const savingType = ref('')
const meaningoutType = ref('')
onMounted(async () => {
  try {
    const response = await axios.get(URL, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    });
    data.value = response.data;
    savings.value = response.data.savings || [];
    deposits.value = response.data.deposits || [];
    usertype.value = response.data.user_type;
    savingType.value = (response.data.user_type === 'EIG' || response.data.user_type === 'EIV' || response.data.user_type === 'FIG' || response.data.user_type === 'FIV') ? '자유로운 소비를 추구하는 고객님의 성향에 맞는 자유적립식 상품을 추천했어요' : '계획적인 소비를 추구하는 고객님의 성향에 맞는 정액적립식 상품을 추천했어요';
    meaningoutType.value = (response.data.user_type === 'EIG' || response.data.user_type === 'FIG' || response.data.user_type === 'ERG' || response.data.user_type === 'FRG') ? '합리적인 소비에 맞는 합리적 재태크를 위해 높은 이율의 상품을 추천했어요' : '재태크와 함께 우리 사회도 챙길 수 있는 상품을 추천했어요';
  } catch (err) {
    console.error('Error fetching data:', err);
    if (err.response) {
      error.value = `Error: ${err.response.status} - ${err.response.statusText}`;
    } else if (err.request) {
      error.value = 'No response received from server';
    } else {
      error.value = `Request error: ${err.message}`;
    }
  }
});
</script>

<style scoped>
/* 스타일은 필요에 따라 추가 */
</style> -->


<!-- <template>
  <div>
    <div>{{ data }}</div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter';
import axios from 'axios';

const store = useCounterStore()
const URL = `${store.API_URL}/banks/recommendation_by_survey/`
const data = ref(null);
const error = ref(null);

onMounted(async () => {
  try {
    const response = await axios.get(URL,{
      headers: {
        Authorization: `Token ${store.token}`
      }
    });
    data.value = response.data;
  }
   catch (err) {
    console.error('Error fetching data:', err);
    if (err.response) {
      error.value = `Error: ${err.response.status} - ${err.response.statusText}`;
    } else if (err.request) {
      error.value = 'No response received from server';
    } else {
      error.value = `Request error: ${err.message}`;
    }
  }
});
</script>

<style scoped>

</style> -->