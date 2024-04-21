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
					console.log('postStore data', response.data);
					this.posts = response.data;
				})
				.catch((error) => {
					console.log('error', error);
				});
		},
		updatePost(body) {
			console.log('body', body);
			this.posts.unshift(body);
		},
	},
});
