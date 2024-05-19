<template>
  <v-form @submit.prevent="createComment">
    <v-textarea
      label="댓글 작성"
      v-model.trim="content"
      outlined
      dense
    ></v-textarea>
    <v-btn 
      color="primary"
      type="submit"
      class="mt-2"
    >
      댓글 달기
    </v-btn>
  </v-form>
</template>

<script setup>
import { ref, defineEmits } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const route = useRoute()
const content = ref('')
const emit = defineEmits(['commentCreated'])

const createComment = async () => {
  try {
    const response = await axios.post(`${store.API_URL}/community/${route.params.boardType}/comment/`, {
      post_id: route.params.post_id,
      content: content.value,
    }, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    content.value = ''
    emit('commentCreated', response.data)
    console.log('댓글 생성 성공:', response.data)
  } catch (error) {
    console.error('댓글 생성 실패:', error.response.data)
  }
}
</script>

<style scoped>
</style>


<!-- 
<template>
  <v-form @submit.prevent="createComment">
    <v-textarea
      label="댓글 작성"
      v-model.trim="content"
      outlined
      dense
    ></v-textarea>
    <v-btn 
      color="primary"
      type="submit"
      class="mt-2"
    >
      댓글 달기
    </v-btn>
  </v-form>
</template>

<script setup>
import { ref, defineEmits } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const route = useRoute()
const content = ref('')
const emit = defineEmits(['commentCreated'])

const createComment = async () => {
  try {
    const response = await axios.post(`${store.API_URL}/community/bulletin/comment/`, {
      post_id: route.params.post_id,
      content: content.value,
    }, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    content.value = ''
    emit('commentCreated', response.data)
    console.log('댓글 생성 성공:', response.data)
  } catch (error) {
    console.error('댓글 생성 실패:', error.response?.data || error.message)
  }
}
</script>

<style scoped>
</style> -->


<!-- <template>
    <v-form @submit.prevent="createComment">
      <v-textarea
        label="댓글 작성"
        v-model.trim="content"
        outlined
        dense
      ></v-textarea>
      <v-btn 
        color="primary"
        type="submit"
        class="mt-2"
      >
        댓글 달기
      </v-btn>
    </v-form>
  </template>
  
  <script setup>
  import { ref,defineEmits  } from 'vue'
  import { useRoute } from 'vue-router'
  import axios from 'axios'
  import { useCounterStore } from '@/stores/counter'

  const store = useCounterStore()
  const route = useRoute()
  const content = ref('')
  const emit = defineEmits(['commentCreated'])


  const createComment = async () => {
    try {
      const response = await axios.post(`${store.API_URL}/community/bulletin/comment/`, {
        post_id: route.params.post_id,
        content: content.value,
      }, {
        headers: {
          Authorization: `Token ${store.token}`
        }
      })
      content.value = ''
      emit('commentCreated', response.data)
      // 댓글 생성 후 리스트를 갱신하거나, 생성된 댓글을 리스트에 추가하는 로직을 여기에 추가
      console.log('댓글 생성 성공:', response.data)
    } catch (error) {
      console.error('댓글 생성 실패:', error.response.data)}
  }
  </script>
  
  <style scoped>
  </style>
   -->