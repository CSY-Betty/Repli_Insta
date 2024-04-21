import { ref } from 'vue';
import { defineStore } from 'pinia';

export const usePostStore = defineStore({
	id: 'posts',
	state: () => ({
		posts: ref([]),
	}),
	actions: {
		updatePost(body) {
			console.log('body', body);
			this.posts.unshift(body);
		},
	},
});
