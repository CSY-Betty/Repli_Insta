<script>
import axios from 'axios';

import PostsList from '@/components/PostsList.vue';
import { usePostStore } from '@/stores/post';

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
				.get('/api/posts')
				.then((response) => {
					console.log('data', response.data);
					this.posts = response.data;
				})
				.catch((error) => {
					console.log('error', error);
				});
		},
	},
	beforeCreate() {
		this.postStore.initStore();
	},
};
</script>
<template>
	<div class="flex-col justify-center w-full mt-6 px-40 overflow-y-auto">
		<div v-for="post in posts" v-bind:key="post.id">
			{{ post.body }}
			{{ post.created_by.name }}
			{{ post.created_at_formatted }} ago
		</div>
		<ul class="grid grid-cols-3 gap-1">
			<PostsList />
		</ul>
		<ul class="grid grid-cols-3 gap-1">
			<div v-for="post in postStore.posts">{{ post.body }}</div>
		</ul>
	</div>
</template>
