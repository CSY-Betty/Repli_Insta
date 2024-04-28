<script>
import axios from 'axios';
import PostsList from '@/components/PostsList.vue';
import { useUserStore } from '@/stores/user';
import { RouterLink } from 'vue-router';
import { useToastStore } from '@/stores/toast';

export default {
	name: 'ProfileView',
	setup() {
		const userStore = useUserStore();
		const toastStore = useToastStore();
		return {
			userStore,
			toastStore,
		};
	},
	components: {
		PostsList,
	},
	data() {
		return {
			posts: [],
			user: {
				id: '',
			},
		};
	},
	mounted() {
		this.getPost();
	},
	watch: {
		'$route.params.id': {
			handler: function () {
				this.getPost();
			},
			deep: true,
			immediate: true,
		},
	},
	methods: {
		getPost() {
			axios
				.get(`/api/posts/profile/${this.$route.params.id}`)
				.then((response) => {
					console.log('data', response.data.posts);
					this.posts = response.data.posts;
					this.user = response.data.user;
				})
				.catch((error) => {
					console.log('error', error);
				});
		},
		sendFriendshipRequest() {
			axios
				.post(`/api/friends/${this.$route.params.id}/request/`)
				.then((response) => {
					if (response.data.message == 'request already sent') {
						this.toastStore.showToast(
							5000,
							'The request has already been sent!',
							'bg-red-300'
						);
					} else {
						this.toastStore.showToast(
							5000,
							'The request was sent!',
							'bg-emerald-300'
						);
					}
				})
				.catch((error) => {
					console.log('error', error);
				});
		},
		sendDirectMessage() {
			console.log('sendDirectMessage');
			axios
				.get(`/api/chat/${this.$route.params.id}/get-or-create/`)
				.then((response) => {
					console.log(response.data);
					this.$router.push('/messages');
				})
				.catch((error) => {
					console.log('send error', error);
				});
		},
	},
};
</script>

<template>
	<div class="flex-col justify-center w-full mt-6 px-40 overflow-y-auto">
		<header class="w-8/12 h-40 flex justify-around">
			<img :src="user.get_avatar" class="w-40 h-40 rounded-full mx-8" />
			<div class="my-8 flex flex-col justify-around">
				<div class="flex gap-6 items-center justify-between">
					<p>
						<strong>{{ user.name }}</strong>
					</p>
					<RouterLink
						to="/profile/edit/"
						v-if="userStore.user.id === user.id"
						class="bg-gray-300 hover:bg-gray-400 text-white font-bold py-2 px-4 rounded"
					>
						Edit profile
					</RouterLink>

					<button
						v-if="userStore.user.id !== user.id"
						@click="sendFriendshipRequest"
						class="bg-gray-300 hover:bg-gray-400 text-white font-bold py-2 px-4 rounded"
					>
						Invite friends
					</button>

					<button
						v-if="userStore.user.id !== user.id"
						@click="sendDirectMessage"
						class="bg-gray-300 hover:bg-gray-400 text-white font-bold py-2 px-4 rounded"
					>
						send Messages
					</button>
				</div>

				<div class="flex gap-6 mt-4" v-if="user.id">
					<p>{{ user.posts_count }} posts</p>
					<RouterLink
						:to="{ name: 'friends', params: { id: user.id } }"
						>{{ user.friends_count }} friends</RouterLink
					>
				</div>
			</div>
		</header>
		<hr class="border-1 dark:bg-gray-700 my-8" />
		<ul class="grid grid-cols-3 gap-1">
			<li
				v-for="post in posts"
				v-bind:key="post.id"
				class="cursor-pointer relative group"
			>
				<RouterLink :to="{ name: 'post', params: { id: post.id } }">
					<img
						alt="galary1"
						class="rounded-sm object-center object-cover aspect-square"
						v-for="image in post.attachments"
						v-bind:key="image.id"
						:src="image.get_image"
					/>

					<!-- image hover -->
					<div
						class="flex justify-center items-center opacity-0 bg-gradient-to-t from-gray-800 via-gray-800 to-opacity-30 group-hover:opacity-50 absolute top-0 left-0 h-full w-full"
					></div>
					<div
						class="absolute top-0 left-0 w-full h-full flex justify-center items-center opacity-0 hover:opacity-100"
					>
						<div class="flex flex-row text-center gap-6">
							<div class="flex flex-row gap-1">
								<svg
									xmlns="http://www.w3.org/2000/svg"
									viewBox="0 0 24 24"
									fill="white"
									class="w-6 h-6"
								>
									<path
										d="m11.645 20.91-.007-.003-.022-.012a15.247 15.247 0 0 1-.383-.218 25.18 25.18 0 0 1-4.244-3.17C4.688 15.36 2.25 12.174 2.25 8.25 2.25 5.322 4.714 3 7.688 3A5.5 5.5 0 0 1 12 5.052 5.5 5.5 0 0 1 16.313 3c2.973 0 5.437 2.322 5.437 5.25 0 3.925-2.438 7.111-4.739 9.256a25.175 25.175 0 0 1-4.244 3.17 15.247 15.247 0 0 1-.383.219l-.022.012-.007.004-.003.001a.752.752 0 0 1-.704 0l-.003-.001Z"
									/>
								</svg>
								<p class="text-white">
									<strong>{{ post.likes_count }}</strong>
								</p>
							</div>
							<div class="flex flex-row gap-1">
								<svg
									xmlns="http://www.w3.org/2000/svg"
									viewBox="0 0 24 24"
									fill="white"
									class="w-6 h-6"
								>
									<path
										fill-rule="evenodd"
										d="M5.337 21.718a6.707 6.707 0 0 1-.533-.074.75.75 0 0 1-.44-1.223 3.73 3.73 0 0 0 .814-1.686c.023-.115-.022-.317-.254-.543C3.274 16.587 2.25 14.41 2.25 12c0-5.03 4.428-9 9.75-9s9.75 3.97 9.75 9c0 5.03-4.428 9-9.75 9-.833 0-1.643-.097-2.417-.279a6.721 6.721 0 0 1-4.246.997Z"
										clip-rule="evenodd"
									/>
								</svg>
								<p class="text-white">
									<strong>{{ post.comments_count }}</strong>
								</p>
							</div>
						</div>
					</div>
				</RouterLink>
			</li>
		</ul>
	</div>
</template>
