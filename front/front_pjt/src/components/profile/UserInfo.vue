<template>
    <div v-if="user">
      <p>{{ user }}</p>
      <v-card class="mx-auto my-5 pa-5" max-width="400">
            <v-card-title class="d-flex align-center justify-center">
                <v-avatar size="80" class="mr-3">
                    <v-img :src="user.profile_img" alt="User Avatar" />
                </v-avatar>
            </v-card-title>
            <!-- <v-card-subtitle class="text-center">{{ user.username }}</v-card-subtitle> -->
            <v-card-text class="text-center">
              <div>
                <strong>{{ user.username }}</strong>님의 소비 성향은
                <strong>{{ user.user_type }}</strong>입니다.
              </div>
                <!-- <div>
                    <strong>User Type:</strong> {{ user.user_type || 'N/A' }}
                </div>
                <div>
                    <strong>Email:</strong> {{ user.email }}
                </div>
                <div>
                    <strong>Joined:</strong> {{ new Date(user.date_joined).toLocaleDateString() }}
                </div> -->
            </v-card-text>
        </v-card>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import axios from 'axios'

const store = useCounterStore()
const user = ref(null)

const fetchUserProfile = async () => {
  try {
    const response = await axios.get(`${store.API_URL}/api/v1/accounts/profile/`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    user.value = response.data
  } catch (error) {
    console.error('Error fetching user profile:', error)
  }
}

onMounted(fetchUserProfile)
</script>

<style scoped>

.v-card {
  max-width: 400px;
  margin: auto;
}
</style>