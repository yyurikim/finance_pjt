<template>
    <div class="container">
      <img src="@/assets/test/test.png" alt="Q6" class="Q">
      <div>
        <button @click="startSurvey" class="text">나의 소비성향 확인하기 →</button>
      </div>
    </div>
</template>
  

<script>
import { inject } from 'vue';
import { useRouter } from 'vue-router';

export default {
setup() {
    const { reset } = inject('survey');
    const router = useRouter(); // useRouter는 setup 내부에서 호출

    const startSurvey = () => {
    reset();
    router.push('/survey/1');
    };

    return {
    startSurvey,
    };
},
};
</script>

<style scoped>
.container {
  width: 300px;
  height: 825px;
  margin: 10px auto;
  position: relative;
  text-align: center;
}

.container img {
  width: 100%;
  vertical-align: middle;
}

.text {
  position: absolute;
  background: #bdffec;
  z-index: 10;
  top: 50%; /* 버튼을 이미지의 중앙 위로 이동 */
  left: 50%;
  width: 220px;
  transform: translate(-50%, -50%); /* 중앙 정렬 */
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 10px; /* 버튼 크기와 패딩 조정 */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* 그림자 설정 */
  font-weight: bold;
}
</style>
