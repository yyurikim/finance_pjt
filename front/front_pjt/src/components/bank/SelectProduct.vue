<template>
  <div class="container">
    <div v-for="(product, index) in selectedProducts" :key="index" class="item" @click="removeProduct(index)">
      <h3>{{ product.fin_prdt_nm }}</h3>
      <h4>최대 {{ product.intr_rate }}%</h4>
    </div>
    <div v-for="index in emptySlots" :key="'empty-' + index" class="item">
      <v-icon style="margin-bottom: 10px;">fa-solid fa-magnifying-glass</v-icon>
      <p>금융 상품을 비교해보세요!</p>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref, computed } from 'vue';

export default defineComponent({
  name: 'SelectProduct',
  setup() {
    const selectedProducts = ref([]);

    const emptySlots = computed(() => {
      return 3 - selectedProducts.value.length;
    });

    const addProduct = (product, isDeposit, selectedTerm) => {
      if (selectedProducts.value.length >= 3) {
        alert('금융 상품은 3개를 초과해 선택할 수 없습니다.');
        return;
      }

      if (selectedProducts.value.length > 0) {
        const firstProduct = selectedProducts.value[0];
        if (firstProduct.isDeposit !== isDeposit || firstProduct.selectedTerm !== selectedTerm) {
          alert('동일한 조건에서 상품을 선택해주세요!');
          return;
        }
      }

      if (selectedProducts.value.some(p => p.fin_prdt_cd === product.fin_prdt_cd)) {
        alert('이미 선택한 상품입니다.');
        return;
      }
      selectedProducts.value.push({ ...product, isDeposit, selectedTerm });
    };

    const removeProduct = (index) => {
      selectedProducts.value.splice(index, 1);
    };

    return {
      selectedProducts,
      emptySlots,
      addProduct,
      removeProduct,
    };
  },
});
</script>

<style scoped>
.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 20px auto;
  width: 75%;
  margin-bottom: 70px;
  margin-top: 50px;
  gap: 10px; /* 아이템 간격 조정 */
}

.item {
  width: 280px; /* 지정된 가로 너비 */
  height: 120px; /* 지정된 세로 너비 */
  border: 1px solid #ccc;
  padding: 30px;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center; /* 중앙 정렬 추가 */
}
.item h3 {
  margin-bottom: 10px; /* h3와 h4 사이의 여백 */
}
.item h4 {
  margin-top: 0; /* h4의 상단 마진 제거 */
}
</style>
