<template>
  <div>
    <h2>적금 리스트</h2>
    <div v-if="loading">로딩 중...</div>
    <div v-else>
      <div v-for="(saving, index) in displayedSavings" :key="saving.saving_id" @click="selectItem(saving)" class="saving-item">
        <img :src="getBankLogo(saving.kor_co_nm)" :alt="saving.kor_co_nm" class="bank-logo" />
        <div class="saving-details">
          <h3>{{ saving.fin_prdt_nm }}</h3>
          <p>{{ saving.kor_co_nm }}</p>
        </div>
        <div class="interest-rate">
          <p>최고 {{ saving.intr_rate }}%</p>
        </div>
        <div class="action-buttons">
          <button @click.stop="viewDetails(saving.saving_id)">자세히 보기</button>
          <button @click.stop="openModal(saving)">옵션 보기</button>
        </div>
      </div>
      <div v-if="displayedSavings.length < filteredSavings.length" class="load-more">
        <button @click="loadMore" class="fa fa-plus"></button>
      </div>
    </div>

    <v-dialog v-model="isModalOpen" max-width="600px">
      <v-card>
        <v-card-title class="headline">옵션</v-card-title>
        <v-card-text>
          <div v-if="selectedSaving.options && selectedSaving.options.length">
            <table>
              <thead>
                <tr>
                  <th>옵션 금리</th>
                  <th>옵션 기간</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="option in selectedSaving.options" :key="option.saving_option_id">
                  <td>{{ option.intr_rate }}%</td>
                  <td>{{ option.save_trm }}개월</td>
                </tr>
              </tbody>
            </table>
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
import { defineComponent, ref, computed, onMounted, getCurrentInstance } from 'vue';

// 이미지 import
import nonghyupLogo from '@/assets/banklogo/nonghyup.png';
import kookminLogo from '@/assets/banklogo/kookmin.png';
import wooriLogo from '@/assets/banklogo/woori.png';
import shinhanLogo from '@/assets/banklogo/shinhan.png';
import standardLogo from '@/assets/banklogo/standard.png';
import daeguLogo from '@/assets/banklogo/daegu.png';
import bnkLogo from '@/assets/banklogo/bnk.png';
import gwangjuLogo from '@/assets/banklogo/gwangju.png';
import jejuLogo from '@/assets/banklogo/jeju.png';
import ibkLogo from '@/assets/banklogo/ibk.png';
import kdbLogo from '@/assets/banklogo/kdb.png';
import kbankLogo from '@/assets/banklogo/kbank.png';
import suhyupLogo from '@/assets/banklogo/suhyup.png';
import kakaoLogo from '@/assets/banklogo/kakao.png';
import hanaLogo from '@/assets/banklogo/hana.png';
import tossLogo from '@/assets/banklogo/toss.png';

export default defineComponent({
  name: 'BankSavingList',
  props: {
    selectedTerm: {
      type: [Number, String],
      required: true
    }
  },
  setup(props, { emit }) {
    const savings = ref([]);
    const savingOptions = ref([]);
    const combinedData = ref([]);
    const loading = ref(true);
    const isModalOpen = ref(false);
    const selectedSaving = ref({});
    const displayedSavingsCount = ref(10); // 한번에 보여줄 아이템 개수
    const { proxy } = getCurrentInstance();

    // 은행 로고 객체
    const bankLogos = {
      '농협은행주식회사': nonghyupLogo,
      '국민은행': kookminLogo,
      '우리은행': wooriLogo,
      '신한은행': shinhanLogo,
      '한국스탠다드차타드은행': standardLogo,
      '대구은행': daeguLogo,
      '부산은행': bnkLogo,
      '경남은행': bnkLogo,
      '광주은행': gwangjuLogo,
      '제주은행': jejuLogo,
      '전북은행': gwangjuLogo,
      '중소기업은행': ibkLogo,
      '한국산업은행': kdbLogo,
      '주식회사 케이뱅크': kbankLogo,
      '수협은행': suhyupLogo,
      '주식회사 카카오뱅크': kakaoLogo,
      '토스뱅크 주식회사': tossLogo,
      '하나은행': hanaLogo
    };

    const fetchSavings = async () => {
      try {
        const response = await proxy.$http.get('savings/');
        savings.value = response.data;
      } catch (error) {
        console.error('Failed to fetch savings:', error);
      }
    };

    const fetchSavingOptions = async () => {
      try {
        const response = await proxy.$http.get('saving-options/');
        savingOptions.value = response.data;
      } catch (error) {
        console.error('Failed to fetch saving options:', error);
      }
    };

    const combineData = () => {
      combinedData.value = savings.value.map(saving => {
        const options = savingOptions.value.filter(option => option.saving_product_id === saving.saving_id);
        return {
          ...saving,
          options: options,
          intr_rate: options.length > 0 ? Math.max(...options.map(option => option.intr_rate)) : null
        };
      });
      loading.value = false;
    };

    const filteredSavings = computed(() => {
      if (props.selectedTerm === 'all') {
        return combinedData.value;
      }
      return combinedData.value.map(saving => {
        const filteredOptions = saving.options.filter(option => option.save_trm == props.selectedTerm);
        return {
          ...saving,
          options: filteredOptions
        };
      }).filter(saving => saving.options.length > 0);
    });

    const displayedSavings = computed(() => {
      return filteredSavings.value.slice(0, displayedSavingsCount.value);
    });

    const loadMore = () => {
      displayedSavingsCount.value += 10; // 추가로 10개 항목을 표시
    };

    const openModal = (saving) => {
      selectedSaving.value = saving;
      isModalOpen.value = true;
    };

    const closeModal = () => {
      isModalOpen.value = false;
    };

    const viewDetails = (id) => {
      console.log(`View details for item ID: ${id}`);
    };

    const getBankLogo = (bankName) => {
      return bankLogos[bankName];
    };

    const selectItem = (saving) => {
      console.log('Selected item:', saving);
      const maxInterestRateOption = saving.options.reduce((max, option) => {
        return option.intr_rate > max.intr_rate ? option : max;
      }, saving.options[0]);
      emit('select-item', { ...saving, intr_rate: maxInterestRateOption.intr_rate });
    };

    onMounted(async () => {
      await fetchSavings();
      await fetchSavingOptions();
      combineData();
    });

    return {
      combinedData,
      isModalOpen,
      selectedSaving,
      filteredSavings,
      displayedSavings,
      loading,
      selectItem,
      getBankLogo,
      viewDetails,
      openModal,
      closeModal,
      loadMore,
      displayedSavingsCount
    };
  }
});
</script>

<style scoped>
div {
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

.bank-logo {
  width: 50px;
  height: 50px;
  margin-right: 10px;
  border-radius: 50%;
}

.saving-item {
  display: flex;
  align-items: center;
  border: 1px solid #ddd;
  padding: 10px;
  margin: 10px 0;
  cursor: pointer;
}

.saving-details {
  flex: 1;
}

.interest-rate {
  margin-left: auto;
  font-weight: bold;
  color: green;
}

.action-buttons {
  display: flex;
  flex-direction: column;
  margin-left: 10px;
}

button {
  margin-left: 10px;
}

.v-card-title.headline {
  margin: 25px 30px 0px;
}

.v-card-text {
  padding: 15px;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

th {
  background-color: #f2f2f2;
}
.action-buttons {
  display: flex;
  flex-direction: column;
  margin-left: 10px;
}

.load-more {
  text-align: center;
  margin-top: 10px;
}
</style>
