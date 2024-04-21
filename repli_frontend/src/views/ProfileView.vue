<script>
import axios from 'axios';
import PostsList from '@/components/PostsList.vue';

export default {
	name: 'ProfileView',
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
		<header class="w-8/12 h-40 flex justify-around">
			<img
				src="https://i.pravatar.cc/100?img=29"
				class="w-40 h-40 rounded-full mx-8"
			/>
			<div class="my-8 flex flex-col justify-around">
				<div class="flex gap-6 items-center justify-between">
					<p>
						<strong>Fack Name</strong>
					</p>
					<button
						class="bg-gray-300 hover:bg-gray-400 text-white font-bold py-2 px-4 rounded"
					>
						Edit profile
					</button>
				</div>

				<div class="flex gap-6 mt-4">
					<p>17 posts</p>
					<p>17 followers</p>
					<p>17 following</p>
				</div>
			</div>
		</header>
		<hr class="border-1 dark:bg-gray-700 my-8" />
		<ul class="grid grid-cols-3 gap-1">
			<div v-for="post in posts" v-bind:key="post.id">
				{{ post.body }}
				{{ post.created_by.name }}
				{{ post.created_at_formatted }} ago
			</div>
			<PostsList />
		</ul>
	</div>
</template>
