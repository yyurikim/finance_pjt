import { ref, computed, watch } from 'vue'; // watch 추가
import { defineStore } from 'pinia';
import axios from 'axios';
import { useRouter } from 'vue-router';

export const useCounterStore = defineStore('counter', () => {
  
  const API_URL = 'http://127.0.0.1:8000';
  const token = ref(localStorage.getItem('token')); // 초기 토큰 값을 localStorage에서 가져옵니다.
  const router = useRouter();

  // heartStatus 초기화 및 로컬 스토리지에서 값 불러오기
  const heartStatus = ref({});
  const storedHeartStatus = localStorage.getItem('heartStatus');
  if (storedHeartStatus) {
    try {
      heartStatus.value = JSON.parse(storedHeartStatus);
    } catch (e) {
      console.error('Failed to parse heartStatus from localStorage:', e);
    }
  }

  const isLogin = computed(() => {
    return token.value !== null;
  });

  // heartStatus 변경 시 로컬 스토리지에 저장
  watch(heartStatus, (newStatus) => {
    localStorage.setItem('heartStatus', JSON.stringify(newStatus));
  }, { deep: true });

  const toggleLike = async (deposit) => {
    try {
      const url = `${API_URL}/banks/like-deposit/${deposit.deposit_id}/`;
      console.log('Token!!!', token.value);
      const response = await axios.post(url, {}, {
        headers: {
          Authorization: `Token ${token.value}`
        }
      });

      // Update the liked status in the deposit object
      deposit.liked = response.data.liked;

      // Update heartStatus
      heartStatus.value[deposit.deposit_id] = response.data.liked;

      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  const heartStatus1 = ref({});
  const storedHeartStatus1 = localStorage.getItem('heartStatus1');
  if (storedHeartStatus1) {
    try {
      heartStatus1.value = JSON.parse(storedHeartStatus1);
    } catch (e) {
      console.error('Failed to parse heartStatus1 from localStorage:', e);
    }
  }

  // heartStatus 변경 시 로컬 스토리지에 저장
  watch(heartStatus1, (newStatus) => {
    localStorage.setItem('heartStatus1', JSON.stringify(newStatus));
  }, { deep: true });

  const toggleLike1 = async (saving) => {
    try {
      const url = `${API_URL}/banks/like-saving/${saving.saving_id}/`;
      console.log('Token!!!', token.value);
      const response = await axios.post(url, {}, {
        headers: {
          Authorization: `Token ${token.value}`
        }
      });

      saving.liked = response.data.liked;
      heartStatus1.value[saving.saving_id] = response.data.liked;

      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  const userInfo = ref();
  const getUserInfo = function (user_id) {
    axios({
      method: 'get',
      url: `${API_URL}api/v1/accounts/${user_id}/info/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) => {
        userInfo.value = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
  };

  const userId = ref(null);

  const logIn = function(payload) {
    const { username, password } = payload;
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((res) => {
        console.log('로그인 성공!');
        console.log(res.data);
        console.log(res.data.key);
        token.value = res.data.key;
        userId.value = username;
        localStorage.setItem('token', res.data.key); // 로그인 성공 시 토큰을 localStorage에 저장
        router.push({ name: 'home' });
      })
      .catch((error) => {
        console.log(error);
        window.alert('아이디 또는 비밀번호가 틀렸습니다.');
      });
  };

  const logOut = function() {
    token.value = null;
    userId.value = null;
    localStorage.removeItem('token');
    router.push({ name: 'login' });
  };

  const signUp = function(payload) {
    const { username, email, password1, password2 } = payload;
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
        console.log('회원가입 성공!');
        const password = password1;
        logIn({ username, password });
      })
      .catch((error) => {
        console.log('회원가입 실패:', error.response.data);
        window.alert("회원가입에 실패했습니다: " + error.response.data);
      });
  };

  const changePassword = (payload) => {
    const { currentPassword, newPassword } = payload;
    axios({
      method: 'post',
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
      alert('비밀번호가 성공적으로 변경되었습니다.');
      router.push({ name:'home' });
    })
    .catch((error) => {
      console.error('비밀번호 변경 실패:', error.response.data);
      alert('비밀번호 변경에 실패했습니다: ' + error.response.data.detail);
    });
  };

  const deleteUser = function() {
    const answer = window.confirm("회원탈퇴 하시겠습니까?");
    if (answer) {
      const re_answer = window.confirm("정말 회원탈퇴 하시겠습니까?");
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
            window.alert("회원탈퇴 되었습니다.");
            router.push({ name: 'signup' });
          })
          .catch((err) => {
            console.log(err);
            window.alert("회원탈퇴 중 문제가 발생했습니다.");
          });
      }
    }
  };

  return { API_URL, signUp, logIn, userInfo, token, isLogin, userId, logOut, deleteUser, changePassword, getUserInfo, heartStatus, toggleLike, heartStatus1, toggleLike1 };
});
