<template>
  <div class="first">
    <h1>은행 상품 목록</h1>
    <SelectProduct ref="selectProduct" />

    <div class="switch-row">
      <div class="switch-container product-switch">
        <div class="switch">
          <div class="switch-options">
            <span
              :class="{ active: isDeposit }"
              @click="selectProductType(true)"
            >예금</span>
            <span
              :class="{ active: !isDeposit }"
              @click="selectProductType(false)"
            >적금</span>
          </div>
          <div class="switch-toggle" :style="productToggleStyle"></div>
        </div>
      </div>

      <div class="switch-container term-switch">
        <div class="switch">
          <div class="switch-options">
            <span
              v-for="term in terms"
              :key="term"
              :class="{ active: selectedTerm === term }"
              @click="selectTerm(term)"
            >{{ term === 'all' ? '전체' : `${term}개월` }}</span>
          </div>
          <div class="switch-toggle" :style="termToggleStyle"></div>
        </div>
      </div>

      <div>
        <button @click="openCompareModal">비교하러 가기</button>
      </div>
    </div>

    <div class="search-container">
      <input 
        v-model="searchQuery" 
        type="text" 
        placeholder="검색어를 입력하세요..." 
        class="search-input" 
      />
    </div>

    <div v-if="isDeposit">
      <BankDepositList 
        :selectedTerm="selectedTerm" 
        :searchQuery="searchQuery" 
        :isDeposit="isDeposit" 
        @select-item="handleSelectItem" />
    </div>
    <div v-else>
      <BankSavingList 
        :selectedTerm="selectedTerm" 
        :searchQuery="searchQuery" 
        :isDeposit="isDeposit" 
        @select-item="handleSelectItem" />
    </div>

    <v-dialog v-model="isCompareModalOpen" max-width="800px">
      <ProductCompare 
        :selectedProducts="selectedProducts" 
        :selectedTerm="selectedTerm" 
        :userAmount="userAmount"
        :isDeposit="isDeposit"
        @close="closeCompareModal" 
      />
    </v-dialog>
  </div>
</template>

<script>
import { defineComponent, ref, computed, getCurrentInstance, watch } from 'vue'
import BankDepositList from '@/components/bank/BankDepositList.vue'
import BankSavingList from '@/components/bank/BankSavingList.vue'
import SelectProduct from '@/components/bank/SelectProduct.vue'
import ProductCompare from '@/components/bank/ProductCompare.vue'

export default defineComponent({
  name: 'BankView',
  components: {
    BankDepositList,
    BankSavingList,
    SelectProduct,
    ProductCompare
  },
  setup() {
    const { proxy } = getCurrentInstance()
    const isDeposit = ref(true); // 예금 상태 초기화
    const selectedTerm = ref('all')
    const searchQuery = ref('')  // 검색어 상태 추가
    const terms = ['all', 6, 12, 24, 36]
    const isCompareModalOpen = ref(false)
    const selectedProducts = ref([])
    const userAmount = ref(0)

    watch([isDeposit, selectedTerm], () => {
      selectedProducts.value = []
    })

    const selectProductType = (deposit) => {
      isDeposit.value = deposit
    }

    const selectTerm = (term) => {
      selectedTerm.value = term
    }

    const productToggleStyle = computed(() => {
      return {
        transform: `translateX(${isDeposit.value ? 0 : 100}%)`
      }
    })

    const termToggleStyle = computed(() => {
      const index = terms.indexOf(selectedTerm.value)
      return {
        transform: `translateX(${index * 500 / terms.length}%)`
      }
    })

    const handleSelectItem = (product) => {
      const selectProductComponent = proxy.$refs.selectProduct
      if (selectProductComponent) {
        selectProductComponent.addProduct(product, isDeposit.value, selectedTerm.value)
        selectedProducts.value = selectProductComponent.selectedProducts
      }
    }

    const openCompareModal = () => {
      isCompareModalOpen.value = true
    }

    const closeCompareModal = () => {
      isCompareModalOpen.value = false
    }

    return {
      isDeposit,
      selectedTerm,
      searchQuery, // 검색어 상태 리턴에 추가
      terms,
      isCompareModalOpen,
      selectedProducts,
      selectProductType,
      userAmount,
      selectTerm,
      productToggleStyle,
      termToggleStyle,
      handleSelectItem,
      openCompareModal,
      closeCompareModal
    }
  }
})
</script>

<style scoped>
.first {
  padding: 80px;
  width:80%
}

.switch-row {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 20px;
  margin: 20px 0;
}

.switch-container {
  display: flex;
  align-items: center;
}

.product-switch .switch {
  width: 95px;
  height: 35px;
}

.term-switch .switch {
  width: 300px;
  height: 35px;
}

.switch {
  position: relative;
  background-color: #f1f1f1;
  border-radius: 20px;
  display: flex;
  align-items: center;
}

.switch-options {
  display: flex;
  width: 100%;
  z-index: 1;
}

.product-switch .switch-options span {
  flex: 1;
  text-align: center;
  cursor: pointer;
  padding: 5px 0;
  user-select: none;
}

.term-switch .switch-options span {
  flex: 1;
  text-align: center;
  cursor: pointer;
  padding: 10px 0;
  user-select: none;
}

.switch-options span.active {
  font-weight: bold;
}

.product-switch .switch-toggle {
  width: 50%;
}

.term-switch .switch-toggle {
  width: 20%;
}

.switch-toggle {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  background-color: white;
  border-radius: 20px;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
  transition: transform 0.3s ease;
}

.search-container {
  margin: 20px 0;
}

.search-input {
  width: 100%;
  padding: 10px;
  font-size: 16px;
}
</style>
