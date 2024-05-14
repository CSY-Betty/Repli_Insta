import { ref } from 'vue';
import { defineStore } from 'pinia';
import axios from 'axios';

export const usePostStore = defineStore({
	id: 'posts',
	state: () => ({
		posts: ref([]),
	}),
	actions: {
		initStore() {
			axios
				.get('/api/posts')
				.then((response) => {
					this.posts = response.data;
				})
				.catch((error) => {
					console.log('error', error);
				});
		},
		updatePost(body) {
			this.posts.unshift(body);
		},
	},
});
