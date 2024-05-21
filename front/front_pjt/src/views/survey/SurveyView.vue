<template>
<div>
    <div>
        <!-- <img src="@/assets/test/test.png" alt="Q6" class="Q"> -->
    </div>
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
.text{
    background: #bdffec;;
}
</style>
