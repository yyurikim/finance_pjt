<template>
  <div class="container">
    <div class="title-block">
      <h1>Edit Profile</h1>
      <p class="login-prompt">프로필 수정 페이지입니다😀</p>
    </div>
    <form class="form" @submit.prevent="saveChanges">
      <div class="form-group">
        <label for="name">이름</label>
        <input id="name" v-model.trim="form.name" type="text" placeholder="이름을 입력해주세요." />
      </div>
      <div class="form-group">
        <label for="profileImage">프로필 이미지</label>
        <input id="profileImage" @change="handleFileChange" type="file" />
      </div>
      <div class="form-group">
        <label for="email">이메일</label>
        <input id="email" v-model.trim="form.email" type="email" placeholder="이메일을 입력해주세요." />
      </div>
      <div class="form-group">
        <label for="age">나이</label>
        <input id="age" v-model.number="form.age" type="number"/>
      </div>
      <div class="form-group">
        <label for="gender">성별</label>
        <select id="gender" v-model="form.gender">
          <option v-for="gender in genders" :key="gender" :value="gender">{{ gender }}</option>
        </select>
      </div>
      <div class="form-group">
        <label for="job">직업</label>
        <select id="job" v-model="form.job">
          <option v-for="job in jobs" :key="job" :value="job">{{ job }}</option>
        </select>
      </div>
      <div class="form-group">
        <label for="salary">월급</label>
        <select id="salary" v-model="form.salary">
          <option v-for="salary in salaries" :key="salary.value" :value="salary.value">{{ salary.text }}</option>
        </select>
      </div>
      <div class="form-group">
        <label for="favoriteBank">주거래 은행</label>
        <select id="favoriteBank" v-model="form.favoriteBank">
          <option v-for="bank in banks" :key="bank" :value="bank">{{ bank }}</option>
        </select>
      </div>
      <button type="submit" class="submit-button">변경된 프로필 저장</button>
    </form>
  </div>
</template>


<script>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

export default {
  setup() {
    const counter = useCounterStore()
    const router = useRouter()

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
    })

    // Options for select inputs
    const genders = ['남성', '여성']
    const jobs = ['직장인', '학생', '자영업', '프리랜서', '주부', '은퇴자', '무직', '기타']
    const salaries = [
      { value: '200', text: '200만원 이하' },
      { value: '300', text: '201만원 ~ 300만원' },
      { value: '400', text: '301만원 ~ 400만원' },
      { value: '500', text: '401만원 ~ 500만원' },
      { value: '600', text: '501만원 ~ 600만원' },
      { value: '601', text: '601만원 이상' }
    ]
    const banks = ['SC제일은행', '경남은행', '광주은행', '국민은행', '기업은행', '농협은행', '대구은행', '부산은행', '수협은행', '신한은행', '외환은행', '우리은행', '전북은행', '제주은행', '카카오뱅크', '케이뱅크', '토스뱅크', '하나은행', '한국산업은행', '한국스탠다드차타드은행', '한국시티은행', '기타']

    const handleFileChange = (e) => {
      form.value.profileImage = e.target.files[0]
    }

    const fetchUserData = () => {
      axios.get('http://localhost:8000/api/v1/accounts/user-info/', {
        headers: {
          Authorization: `Token ${counter.token}`
        }
      })
      .then(response => {
        const data = response.data
        form.value.name = data.name
        form.value.email = data.email
        form.value.age = data.age
        form.value.gender = data.gender
        form.value.job = data.job
        form.value.salary = data.salary
        form.value.favoriteBank = data.favorite_bank
        // 프로필 이미지는 별도로 처리해야 함
      })
      .catch(error => {
        console.error('Failed to fetch user info:', error)
      })
    }

    const saveChanges = () => {
      const formData = new FormData()
      if (form.value.name) formData.append('name', form.value.name)
      if (form.value.profileImage) formData.append('profile_img', form.value.profileImage)
      if (form.value.email) formData.append('email', form.value.email)
      if (form.value.age) formData.append('age', form.value.age)
      if (form.value.gender) formData.append('gender', form.value.gender)
      if (form.value.job) formData.append('job', form.value.job)
      if (form.value.salary) formData.append('salary', form.value.salary)
      if (form.value.favoriteBank) formData.append('favorite_bank', form.value.favoriteBank)

      axios.post('http://localhost:8000/api/v1/accounts/update-user-info/', formData, {
        headers: {
          Authorization: `Token ${counter.token}`
        }
      })
      .then(response => {
        console.log('Response data:', response.data)
        router.push({ name: 'home' }) // 라우트 이름과 경로가 일치하는지 확인
      })
      .catch(error => {
        console.error('Failed to update user info:', error)
      })
    }

    onMounted(() => {
      fetchUserData()
    })

    return {
      form,
      genders,
      jobs,
      salaries,
      banks,
      handleFileChange,
      saveChanges
    }
  }
}
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 24px;
}

.title-block {
  text-align: center;
  margin-top: 5rem;
}

.form {
  width: 100%;
  max-width: 500px; /* 최대 너비 설정 */
  margin-top: 16px;
  display: grid;
  grid-template-columns: 1fr 1fr; /* 2개의 열을 생성 */
  grid-gap: 16px; /* 각 아이템 간격 */
}

.form-group {
  width: 100%; /* 부모 요소의 너비를 전부 채우도록 설정 */
  margin-bottom: 0.7rem;
}

.form-group label {
  display: block;
  font-weight: bold;
  margin-bottom: 8px;
}

.form-group input,
.form-group select {
  width: 100%; /* input 요소 너비 최대로 설정 */
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.submit-button {
  grid-column: span 2; /* 버튼을 두 개의 열을 모두 차지하도록 설정 */
  background-color: #4a5568;
  color: white;
  padding: 12px;
  border-radius: 4px;
  border: none;
  cursor: pointer;
  text-align: center;
}

.login-prompt {
  font-size: 16px;
  margin-top: 0.7rem;
  margin-bottom: 1rem;
}
</style>
