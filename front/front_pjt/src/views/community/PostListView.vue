<template>
    <div>
        <ul>
            <li v-for="post in posts" :key="post.id">
                {{ post.title }}
            </li>
        </ul>
    </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { useCommunityStore } from '@/stores/community';

export default {
    setup() {
        const posts = ref([]);
        const communityStore = useCommunityStore();
        const route = useRoute();
        const router = useRouter();

        onMounted(async () => {
            try {
                // Make an API call to fetch the posts
                const response = await communityStore.fetchPosts();
                posts.value = response.data; // Assuming the response contains an array of posts
            } catch (error) {
                console.error(error);
            }
        });

        return {
            posts,
        };
    },
};
</script>