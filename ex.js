<template>
  <div>
    <h2>적금 리스트</h2>
    <div v-if="loading">로딩 중...</div>
    <div v-else>
      <div v-for="saving in filteredSavings" :key="saving.saving_id" @click="selectItem(saving)">
        <div>
          <h3>{{ saving.fin_prdt_nm }}</h3>
          <p>은행: {{ saving.kor_co_nm }}</p>
          <button @click.stop="viewDetails(saving.saving_id)">자세히 보기</button>
          <button @click.stop="openModal(saving)">옵션 보기</button>
        </div>
      </div>
    </div>

    <v-dialog v-model="isModalOpen" max-width="600px">
      <v-card>
        <v-card-title class="headline">옵션</v-card-title>
        <v-card-text>
          <div v-if="selectedSaving.options && selectedSaving.options.length">
            <div v-for="option in selectedSaving.options" :key="option.saving_option_id">
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

export default defineComponent({
  name: 'BankSavingList',
  props: {
    selectedTerm: {
      type: [Number, String],
      required: true
    }
  },
  setup(props, { emit }) {
    const savings = ref([])
    const savingOptions = ref([])
    const combinedData = ref([])
    const loading = ref(true)
    const isModalOpen = ref(false)
    const selectedSaving = ref({})
    const { proxy } = getCurrentInstance()

    const fetchSavings = async () => {
      try {
        const response = await proxy.$http.get('savings/')
        savings.value = response.data
      } catch (error) {
        console.error('Failed to fetch savings:', error)
      }
    }

    const fetchSavingOptions = async () => {
      try {
        const response = await proxy.$http.get('saving-options/')
        savingOptions.value = response.data
      } catch (error) {
        console.error('Failed to fetch saving options:', error)
      }
    }

    const combineData = () => {
      combinedData.value = savings.value.map(saving => {
        const options = savingOptions.value.filter(option => option.saving_product_id === saving.saving_id)
        return {
          ...saving,
          options: options
        }
      })
      loading.value = false
    }

    const filteredSavings = computed(() => {
      if (props.selectedTerm === 'all') {
        return combinedData.value
      }
      return combinedData.value.map(saving => {
        const filteredOptions = saving.options.filter(option => option.save_trm == props.selectedTerm)
        return {
          ...saving,
          options: filteredOptions
        }
      }).filter(saving => saving.options.length > 0)
    })

    const openModal = (saving) => {
      selectedSaving.value = saving
      isModalOpen.value = true
    }

    const closeModal = () => {
      isModalOpen.value = false
    }

    const viewDetails = (id) => {
      console.log(`View details for item ID: ${id}`)
    }

    const selectItem = (saving) => {
      console.log('Selected item:', saving)
      const maxInterestRateOption = saving.options.reduce((max, option) => {
        return option.intr_rate > max.intr_rate ? option : max
      }, saving.options[0])
      emit('select-item', { ...saving, intr_rate: maxInterestRateOption.intr_rate })
    }

    onMounted(async () => {
      await fetchSavings()
      await fetchSavingOptions()
      combineData()
    })

    return {
      combinedData,
      isModalOpen,
      selectedSaving,
      filteredSavings,
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