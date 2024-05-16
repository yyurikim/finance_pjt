<template>
    <div class="post-form">
      <h1>게시글 작성</h1>
      <form @submit.prevent="submitPost">
        <div>
          <label for="title">제목:</label>
          <input type="text" id="title" v-model="post.title" required>
        </div>
        <div>
          <label for="content">내용:</label>
          <textarea id="content" v-model="post.content" required></textarea>
        </div>
        <button type="submit">게시글 작성</button>
      </form>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  import { useCommunityStore } from '@/stores/community';
  
  export default {
    setup() {
      const communityStore = useCommunityStore();
      const post = ref({
        title: '',
        content: ''
      });
  
      const submitPost = async () => {
        if (post.value.title && post.value.content) {
          try {
            await communityStore.addPost(post.value);
            alert("게시글이 성공적으로 등록되었습니다.");
            // 폼 초기화
            post.value.title = '';
            post.value.content = '';
          } catch (error) {
            console.error('게시글 등록 실패:', error);
            alert("게시글 등록에 실패했습니다.");
          }
        }
      };
  
      return {
        post,
        submitPost
      };
    }
  };
  </script>
  
  <style scoped>
  .post-form {
    max-width: 500px;
    margin: auto;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
  }
  
  label {
    display: block;
    margin-bottom: 5px;
  }
  
  input[type="text"], textarea {
    width: 100%;
    padding: 8px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  button {
    padding: 10px 20px;
    background-color: #007BFF;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  </style>
  