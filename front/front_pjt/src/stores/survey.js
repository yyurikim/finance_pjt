import { reactive } from 'vue';

const state = reactive({
  answers: [],
  result: null,
});

const addAnswer = (answer) => {
  state.answers.push(answer);
};

const calculateResult = () => {
  let type1 = state.answers.slice(0, 3).filter(a => a).length >= 2 ? 'E' : 'F';
  let type2 = state.answers.slice(3, 6).filter(a => a).length >= 2 ? 'I' : 'R';
  let type3 = state.answers.slice(6, 9).filter(a => a).length >= 2 ? 'V' : 'G';
  state.result = `${type1}${type2}${type3}`;
};

const reset = () => {
  state.answers = [];
  state.result = null;
};

export default function survey() {
  return {
    state,
    addAnswer,
    calculateResult,
    reset,
  };
}
