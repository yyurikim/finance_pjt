<template>
  <div>
    <h1>은행 상품 목록</h1>

    <!-- 스위치 컨테이너 -->
    <div class="switch-row">
      <!-- 예금/적금 스위치 -->
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

      <!-- 기간 스위치 -->
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
    </div>

    <div v-if="isDeposit">
      <BankDepositList :selectedTerm="selectedTerm" />
    </div>
    <div v-else>
      <BankSavingList :selectedTerm="selectedTerm" />
    </div>
  </div>
</template>

<script>
import { defineComponent, ref, computed } from 'vue'
import BankDepositList from '@/components/bank/BankDepositList.vue'
import BankSavingList from '@/components/bank/BankSavingList.vue'

export default defineComponent({
  name: 'BankView',
  components: {
    BankDepositList,
    BankSavingList
  },
  setup() {
    const isDeposit = ref(true)
    const selectedTerm = ref('all')
    const terms = ['all', 6, 12, 24, 36]

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

    return {
      isDeposit,
      selectedTerm,
      terms,
      selectProductType,
      selectTerm,
      productToggleStyle,
      termToggleStyle
    }
  }
})
</script>

<style scoped>
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
</style>
