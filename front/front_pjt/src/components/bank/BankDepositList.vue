<template>
  <div>
    <SelectProduct/>
    
    <h2>예적금 리스트</h2>
    <div v-if="loading">로딩 중...</div>
    <div v-else>
      <div v-for="deposit in filteredDeposits" :key="deposit.deposit_id" @click="selectItem(deposit)">
        <h3>{{ deposit.fin_prdt_nm }}</h3>
        <p>은행: {{ deposit.kor_co_nm }}</p>
        <button @click.stop="viewDetails(deposit.deposit_id)">자세히 보기</button>
        <button @click.stop="openModal(deposit)">옵션 보기</button>
      </div>
    </div>

    <v-dialog v-model="isModalOpen" max-width="600px">
      <v-card>
        <v-card-title class="headline">옵션</v-card-title>
        <v-card-text>
          <div v-if="selectedDeposit.options && selectedDeposit.options.length">
            <div v-for="option in selectedDeposit.options" :key="option.deposit_option_id">
              <p>옵션 금리: {{ option.intr_rate }}%</p>
              <p>옵션 기간: {{ option.save_trm }}개월</p>
            </div>
          </div>
          <div v-else>
            <p>옵션이 없습니다.</p>
          </div>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="closeModal">닫기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { defineComponent, ref, computed, onMounted, getCurrentInstance } from 'vue'
import SelectProduct from '@/components/bank/SelectProduct.vue'

export default defineComponent({
  name: 'BankDepositList',
  components:{
    SelectProduct
  },
  props: {
    selectedTerm: {
      type: [Number, String],
      required: true
    }
  },
  setup(props, { emit }) {
    const deposits = ref([])
    const depositOptions = ref([])
    const combinedData = ref([])
    const loading = ref(true)
    const isModalOpen = ref(false)
    const selectedDeposit = ref({})
    const { proxy } = getCurrentInstance()

    const fetchDeposits = async () => {
      try {
        const response = await proxy.$http.get('deposits/')
        deposits.value = response.data
      } catch (error) {
        console.error('Failed to fetch deposits:', error)
      }
    }

    const fetchDepositOptions = async () => {
      try {
        const response = await proxy.$http.get('deposit-options/')
        depositOptions.value = response.data
      } catch (error) {
        console.error('Failed to fetch deposit options:', error)
      }
    }

    const combineData = () => {
      combinedData.value = deposits.value.map(deposit => {
        const options = depositOptions.value.filter(option => option.deposit_product_id === deposit.deposit_id)
        return {
          ...deposit,
          options: options
        }
      })
      loading.value = false
    }

    const filteredDeposits = computed(() => {
      if (props.selectedTerm === 'all') {
        return combinedData.value
      }
      return combinedData.value.map(deposit => {
        const filteredOptions = deposit.options.filter(option => option.save_trm == props.selectedTerm)
        return {
          ...deposit,
          options: filteredOptions
        }
      }).filter(deposit => deposit.options.length > 0)
    })

    const openModal = (deposit) => {
      selectedDeposit.value = deposit
      isModalOpen.value = true
    }

    const closeModal = () => {
      isModalOpen.value = false
    }

    const viewDetails = (id) => {
      console.log(`View details for item ID: ${id}`)
    }

    const selectItem = (deposit) => {
      console.log('Selected item:', deposit)
      emit('select-item', deposit)
    }

    onMounted(async () => {
      await fetchDeposits()
      await fetchDepositOptions()
      combineData()
    })

    return {
      combinedData,
      isModalOpen,
      selectedDeposit,
      filteredDeposits,
      loading,
      selectItem,
      viewDetails,
      openModal,
      closeModal
    }
  }
})
</script>

<style scoped>
div {
  border: 1px solid #ddd;
  padding: 2px;
  margin: 2px;
  cursor: pointer;
}

h3 {
  margin: 0;
  font-size: 1.2em;
}

.options {
  margin-top: 10px;
  padding-left: 20px;
}
</style>
