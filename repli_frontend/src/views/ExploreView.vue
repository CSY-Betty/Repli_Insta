<script>
import axios from 'axios';

import PostsList from '@/components/PostsList.vue';

export default {
	name: 'ExploreView',
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
	</div>
</template>
