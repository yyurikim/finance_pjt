<template>
    <v-app>
      <v-container>
        <v-row>
          <v-col cols="12" md="4">
            <UserInfo />
          </v-col>
          <v-col cols="12" md="8">
            <!-- <financial-recommendations /> -->
            <RecommendationSurvey />
            <UserProducts />
          </v-col>
        </v-row>
      </v-container>
    </v-app>
  </template>
  
  <script setup>
  import UserInfo from '@/components/profile/UserInfo.vue'
  import RecommendationSurvey from '@/components/bank/RecommendationSurvey.vue'
  import UserProducts from '@/components/profile/UserProducts.vue';
  </script>
  
  <style scoped>
  </style>