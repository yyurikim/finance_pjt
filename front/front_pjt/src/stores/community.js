// import { ref, computed } from 'vue'
// import { defineStore } from 'pinia'
// import axios from 'axios'
// import { useRouter } from 'vue-router'
// import { useCounterStore } from '@/stores/counter'

// export const useCommunityStore = defineStore('community', () => {
//     const posts = ref([])
    
//     const getPosts = function() {
//         const counterStore = useCounterStore()
//         const url = `${useCounterStore.API_URL}/community/`
//         axios({
//             method: 'get',
//             url: url,
//         }).then((response) => {
//             posts.value = response.data
//         }).catch((error) => {
//             console.error(error)
//         })
//     }
//     return { posts, getPosts}
// })

// stores/community.js
import { defineStore } from 'pinia';
import axios from 'axios';
import { useCounterStore } from '@/stores/counter';

export const useCommunityStore = defineStore('community', {
    state: () => ({
        posts: []
    }),
    actions: {
        async fetchPosts() {
            const counterStore = useCounterStore();
            const url = `${counterStore.API_URL}/community/`;
            try {
                const response = await axios.get(url);
                this.posts = response.data;
                return response;  // 이 부분은 선택적, 컴포넌트에서 response를 직접 다루기 원한다면 필요
            } catch (error) {
                console.error('Error fetching posts:', error);
                throw error;  // 오류를 던져 컴포넌트에서 catch 할 수 있도록 합니다.
            }
        },
        async addPost(postData) {
            const counterStore = useCounterStore();
            const url = `${counterStore.API_URL}/community/`;
            try {
              const response = await axios.post(url, postData);
              this.posts.push(response.data);  // 응답으로 받은 게시글 데이터를 posts 배열에 추가
              return response;
            } catch (error) {
              console.error('Error posting data:', error);
              throw error;
            }
          }
    }
});
