import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(localStorage.getItem('token')); // 초기 토큰 값을 localStorage에서 가져옵니다.
  const router = useRouter()
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      console.log('로그인 중')
      return true
    }
  })
  const userInfo = ref()
  const getUserInfo = function (user_id) {
    axios({
      method: 'get',
      url: `${API_URL}api/v1/accounts/${user_id}/info/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) => {
        userInfo.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const userId = ref(null)

  const logIn = function(payload) {
    const { username, password } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((res) => {
        console.log('로그인 성공!')
        console.log(res.data)
        console.log(res.data.key)
        token.value = res.data.key
        userId.value = username
        localStorage.setItem('token', res.data.key); // 로그인 성공 시 토큰을 localStorage에 저장
        router.push({name: 'home'})
      })
      .catch((error) => {
        console.log(error)
        window.alert('아이디 또는 비밀번호가 틀렸습니다.')
      })
  }

  const logOut = function() {
    token.value = null;
    userId.value = null;
    localStorage.removeItem('token');
    router.push({ name: 'login' });
  };

  const signUp = function(payload) {
    const { username, email, password1, password2 } = payload
    console.log(username, email, password1, password2, '확인!!!!'); // 입력 데이터 확인
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username,
        password1,
        password2,
        ...(email && { email })
      }
    })
      .then((response) => {
        console.log('회원가입 성공!')
        const password = password1
        logIn({ username, password })
      })
      .catch((error) => {
        console.log('회원가입 실패:', error.response.data)
        window.alert("회원가입에 실패했습니다: " + error.response.data)
      })
  }

  const changePassword = (payload) => {
    const { currentPassword, newPassword } = payload
    axios({
      method:'post',
      url: `${API_URL}/accounts/password/change/`,
      data: {
        current_password: currentPassword,
        new_password1: newPassword,
        new_password2: newPassword,
      },
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then((response) => {
      alert('비밀번호가 성공적으로 변경되었습니다.')
      router.push({name:'home'})
    })
    .catch((error) => {
      console.error('비밀번호 변경 실패:', error.response.data)
      alert('비밀번호 변경에 실패했습니다: ' + error.response.data.detail)
    })
  }

  const deleteUser = function() {
    const answer = window.confirm("회원탈퇴 하시겠습니까?")
    if (answer) {
      const re_answer = window.confirm("정말 회원탈퇴 하시겠습니까?")
      if (re_answer) {
          axios({
            method: 'delete',
            url: `${API_URL}/api/v1/accounts/user_delete/`,
            headers: {
                Authorization: `Token ${token.value}`
            }
          })
          .then((response) => {
            token.value = null;
            userId.value = null;
            localStorage.removeItem('token'); // 로컬 스토리지에서 토큰도 제거합니다.
            window.alert("회원탈퇴 되었습니다.")
            router.push({ name: 'signup' });
          })
          .catch((err) => {
            console.log(err)
            window.alert("회원탈퇴 중 문제가 발생했습니다.")
          })
      }
    }
  }

  return { API_URL, signUp, logIn, userInfo, token, isLogin, userId, logOut, deleteUser, changePassword, getUserInfo }
})
