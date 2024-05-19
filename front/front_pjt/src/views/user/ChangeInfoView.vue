<template>
<v-container class="py-12 md:py-16 lg:py-20">
    <v-row justify="center">
    <v-col cols="12" md="8">
        <v-card class="elevation-2">
        <v-card-title class="text-center">
            <div class="w-full">
            <h1 class="text-3xl font-bold tracking-tight">Edit Profile</h1>
            <p class="text-gray-500 dark:text-gray-400">Update your profile information.</p>
            </div>
        </v-card-title>
        <v-card-text>
            <v-form>
            <v-row>
                <v-col cols="12" md="6">
                <v-text-field
                    label="Name"
                    v-model="form.name"
                    placeholder="Enter your name"
                    outlined
                    dense
                ></v-text-field>
                </v-col>
                <v-col cols="12" md="6">
                <v-file-input
                    label="Profile Image"
                    v-model="form.profileImage"
                    placeholder="Upload your profile image"
                    outlined
                    dense
                ></v-file-input>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="12" md="6">
                <v-text-field
                    label="Email"
                    v-model="form.email"
                    placeholder="Enter your email"
                    type="email"
                    outlined
                    dense
                ></v-text-field>
                </v-col>
                <v-col cols="12" md="6">
                <v-text-field
                    label="Age"
                    v-model="form.age"
                    placeholder="Enter your age"
                    type="number"
                    outlined
                    dense
                ></v-text-field>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="12" md="6">
                <v-select
                    label="Gender"
                    v-model="form.gender"
                    :items="genders"
                    placeholder="Select gender"
                    outlined
                    dense
                ></v-select>
                </v-col>
                <v-col cols="12" md="6">
                <v-select
                    label="Job"
                    v-model="form.job"
                    :items="jobs"
                    placeholder="Select job"
                    outlined
                    dense
                ></v-select>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="12" md="6">
                <v-select
                    label="Salary"
                    v-model="form.salary"
                    :items="salaries"
                    placeholder="Select salary range"
                    outlined
                    dense
                ></v-select>
                </v-col>
                <v-col cols="12" md="6">
                <v-select
                    label="Favorite Bank"
                    v-model="form.favoriteBank"
                    :items="banks"
                    placeholder="Select favorite bank"
                    outlined
                    dense
                ></v-select>
                </v-col>
            </v-row>
            </v-form>
        </v-card-text>
        <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" @click="saveChanges">Save Changes</v-btn>
        </v-card-actions>
        </v-card>
    </v-col>
    </v-row>
</v-container>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import { useCounterStore } from '@/stores/counter';

const counter = useCounterStore();

// Form data
const form = ref({
name: '',
profileImage: null,
email: '',
age: null,
gender: '',
job: '',
salary: '',
favoriteBank: ''
});

// Options for select inputs
const genders = ['남성', '여성'];
const jobs = ['직장인', '학생', '자영업', '프리랜서', '주부', '은퇴자', '무직', '기타'];
const salaries = ['200만원 이하', '201만원 ~ 300만원', '301만원 ~ 400만원', '401만원 ~ 500만원', '501만원 ~ 600만원', '601만원 이상'];
const banks = ['SC제일은행', '경남은행', '광주은행', '국민은행', '기업은행', '농협은행', '대구은행', '부산은행', '수협은행', '신한은행', '외환은행', '우리은행', '전북은행', '제주은행', '카카오뱅크', '케이뱅크', '토스뱅크', '하나은행', '한국산업은행', '한국스탠다드차타드은행', '한국시티은행', '기타'];

const router = useRouter();

const saveChanges = () => {
const formData = new FormData();
formData.append('name', form.value.name);
formData.append('profile_img', form.value.profileImage);
formData.append('email', form.value.email);
formData.append('age', form.value.age);
formData.append('gender', form.value.gender);
formData.append('job', form.value.job);
formData.append('salary', form.value.salary);
formData.append('favorite_bank', form.value.favoriteBank);

axios.post('http://localhost:8000/api/v1/accounts/update-user-info/', formData, {
    headers: {
    Authorization: `Token ${counter.token}`
    }
})
.then(response => {
    console.log('Response data:', response.data);
    router.push({ name: 'home' }); // 라우트 이름과 경로가 일치하는지 확인
})
.catch(error => {
    console.error('Failed to update user info:', error);
});
};
</script>

<style scoped>
.text-center {
text-align: center;
}

.text-gray-500 {
color: #6b7280;
}

.dark\:text-gray-400 {
color: #9ca3af;
}

.ml-auto {
margin-left: auto;
}
</style>
