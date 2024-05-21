<template>
<div class="product-compare">
    <v-btn icon @click="close" class="close-btn">
    <v-icon>fa-solid fa-times</v-icon>
    </v-btn>
    <ProductDetail 
    :selectedProducts="selectedProducts" 
    :selectedTerm="selectedTerm" 
    :userAmount="userAmount"
    :isDeposit="isDeposit" 
    @update:userAmount="updateUserAmount"
    />
</div>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue'
import ProductDetail from '@/components/bank/ProductDetail.vue'

const props = defineProps({
  selectedProducts: {
    type: Array,
    required: true
  },
  selectedTerm: {
    type: [Number, String],
    required: true
  },
  userAmount: {
    type: Number,
    required: true
  },
  isDeposit: {
    type: Boolean,
    required:true
  }
})

const emit = defineEmits(['close', 'update:userAmount']) // 'update:userAmount' 이벤트 추가

const close = () => {
  emit('close')
}

const updateUserAmount = (value) => {
  emit('update:userAmount', value)
}
</script>


<style scoped>
.product-compare {
position: relative;
padding: 20px;
background-color: white; /* 배경을 흰색으로 설정 */
border-radius: 2%;
}

.v-btn {
position: absolute;
top: 10px;
right: 10px;
}
</style>
