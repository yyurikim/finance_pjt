<template>
<div>
    <div>
        <h1>나의 소비 성향은?</h1>
    </div>
    <div>
        <button @click="startSurvey">시작하기</button>
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
