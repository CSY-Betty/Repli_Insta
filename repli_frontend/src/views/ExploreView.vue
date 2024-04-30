<script>
import axios from 'axios';

import PostsList from '@/components/PostsList.vue';
import { usePostStore } from '@/stores/post';
import { RouterLink } from 'vue-router';

export default {
	name: 'ExploreView',
	setup() {
		const postStore = usePostStore();

		return {
			postStore,
		};
	},
	components: {
		PostsList,
	},
	data() {
		return {
			posts: [],
		};
	},
	mounted() {
		this.getPost();
	},
	methods: {
		getPost() {
			axios
				.get('/api/posts/')
				.then((response) => {
					this.posts = response.data;
				})
				.catch((error) => {
					console.log('error', error);
				});
		},
	},
};
</script>
<template>
	<div class="flex-col justify-center w-full mt-6 px-40 overflow-y-auto">
		<ul class="grid grid-cols-3 gap-1">
			<PostsList
				v-for="post in posts"
				v-bind:key="post.id"
				v-bind:post="post"
				class="cursor-pointer relative group"
			/>
		</ul>
	</div>
</template>
