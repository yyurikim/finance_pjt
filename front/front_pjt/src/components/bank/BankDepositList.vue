<template>
  <div>
    <h2>예금 리스트</h2>
    <div v-if="loading">로딩 중...</div>
    <div v-else>
      <div v-for="(deposit, index) in displayedDeposits" :key="deposit.deposit_id" class="deposit-item">
        <img :src="getBankLogo(deposit.kor_co_nm)" :alt="deposit.kor_co_nm" class="bank-logo" />
        <div class="deposit-details" @click="selectItem(deposit)">
          <h3>{{ deposit.fin_prdt_nm }}</h3>
          <p>{{ deposit.kor_co_nm }}</p>
        </div>
        <div class="interest-rate">
          <p>최고 {{ deposit.intr_rate }}%</p>
        </div>
        <div class="action-buttons">
          <i
            :class="['fa-heart', counter.heartStatus[deposit.deposit_id] ? 'fa-solid' : 'fa-regular']"
            @click="toggleLike(deposit)"
          ></i>
          <button @click.stop="viewDetails(deposit.deposit_id)">자세히 보기</button>
          <button @click.stop="openModal(deposit)">옵션 보기</button>
        </div>
      </div>
      <div v-if="displayedDeposits.length < filteredDeposits.length" class="load-more">
        <button @click="loadMore" class="fa fa-plus load-more-button"></button>
      </div>
    </div>

    <v-dialog v-model="isModalOpen" max-width="600px">
      <v-card>
        <v-card-title class="headline">옵션</v-card-title>
        <v-card-text>
          <div v-if="selectedDeposit.options && selectedDeposit.options.length">
            <table>
              <thead>
                <tr>
                  <th>옵션 금리</th>
                  <th>옵션 기간</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="option in selectedDeposit.options" :key="option.deposit_option_id">
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
import axios from 'axios';  // axios import
import { useCounterStore } from '@/stores/counter';

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
  name: 'BankDepositList',
  props: {
    selectedTerm: {
      type: [Number, String],
      required: true
    }
  },
  setup(props, { emit }) {
    const counter = useCounterStore();
    const deposits = ref([]);
    const depositOptions = ref([]);
    const combinedData = ref([]);
    const loading = ref(true);
    const isModalOpen = ref(false);
    const selectedDeposit = ref({});
    const displayedDepositsCount = ref(10); // 한번에 보여줄 아이템 개수
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

    const fetchDeposits = async () => {
      try {
        const response = await proxy.$http.get('deposits/');
        deposits.value = response.data;
      } catch (error) {
        console.error('Failed to fetch deposits:', error);
      }
    };

    const fetchDepositOptions = async () => {
      try {
        const response = await proxy.$http.get('deposit-options/');
        depositOptions.value = response.data;
      } catch (error) {
        console.error('Failed to fetch deposit options:', error);
      }
    };

    const combineData = () => {
      combinedData.value = deposits.value.map(deposit => {
        const options = depositOptions.value.filter(option => option.deposit_product_id === deposit.deposit_id);
        return {
          ...deposit,
          options: options,
          intr_rate: options.length > 0 ? Math.max(...options.map(option => option.intr_rate)) : null
        };
      });
      loading.value = false;
    };

    const filteredDeposits = computed(() => {
      if (props.selectedTerm === 'all') {
        return combinedData.value;
      }
      return combinedData.value.map(deposit => {
        const filteredOptions = deposit.options.filter(option => option.save_trm == props.selectedTerm);
        return {
          ...deposit,
          options: filteredOptions
        };
      }).filter(deposit => deposit.options.length > 0);
    });

    const displayedDeposits = computed(() => {
      return filteredDeposits.value.slice(0, displayedDepositsCount.value);
    });

    const loadMore = () => {
      displayedDepositsCount.value += 10; // 추가로 10개 항목을 표시
    };

    const openModal = (deposit) => {
      selectedDeposit.value = deposit;
      isModalOpen.value = true;
    };

    const closeModal = () => {
      isModalOpen.value = false;
    };

    const viewDetails = (id) => {
      console.log(`View details for item ID: ${id}`);
    };

    const getBankLogo = (bankName) => {
      return bankLogos[bankName] || '';
    };

    const selectItem = (deposit) => {
      console.log('Selected item:', deposit);
      const maxInterestRateOption = deposit.options.reduce((max, option) => {
        return option.intr_rate > max.intr_rate ? option : max;
      }, deposit.options[0]);
      emit('select-item', { ...deposit, intr_rate: maxInterestRateOption.intr_rate });
    };

    // const toggleLike = async (deposit) => {
    //   try {
    //     const url = `${counter.API_URL}/banks/like-deposit/${deposit.deposit_id}/`;
    //     console.log('Token!!!', counter.token);
    //     const response = await axios.post(url, {}, {
    //       headers: {
    //         Authorization: `Token ${counter.token}`
    //       }
    //     });
    //     deposit.liked = response.data.liked; // Update the liked status
    //     console.log(response.data);
    //   } catch (error) {
    //     console.error(error);
    //   }
    // };

    const toggleLike = async (deposit) => {
      await counter.toggleLike(deposit);
    };

    onMounted(async () => {
      await fetchDeposits();
      await fetchDepositOptions();
      combineData();
    });

    return {
      counter,
      combinedData,
      isModalOpen,
      selectedDeposit,
      filteredDeposits,
      displayedDeposits,
      loading,
      bankLogos,
      selectItem,
      getBankLogo,
      viewDetails,
      openModal,
      closeModal,
      loadMore,
      toggleLike,
      displayedDepositsCount
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

.deposit-item {
  display: flex;
  align-items: center;
  border: 1px solid #ddd;
  padding: 10px;
  margin: 10px 0;
  cursor: pointer;
}

.deposit-details {
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
  margin-bottom: 5px;
}

.load-more {
  text-align: center;
  margin-top: 10px;
}

.load-more-button {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 24px;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 20px auto;
}

.fa-heart {
  cursor: pointer;
}
.fa-solid {
  color: red;
}
.fa-regular {
  color: gray;
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
</style>
