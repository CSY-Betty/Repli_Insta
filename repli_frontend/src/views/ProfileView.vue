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
			can_send_friendship_request: null,
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
				.get(`/api/posts/profile/${this.$route.params.id}/`)
				.then((response) => {
					console.log('data', response.data);
					this.posts = response.data.posts;
					this.user = response.data.user;
					this.can_send_friendship_request =
						response.data.can_send_friendship_request;
				})
				.catch((error) => {
					console.log('error', error);
				});
		},
		sendFriendshipRequest() {
			axios
				.post(`/api/friends/${this.$route.params.id}/request/`)
				.then((response) => {
					this.can_send_friendship_request = false;
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
						v-if="
							userStore.user.id !== user.id &&
							can_send_friendship_request
						"
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
			<PostsList
				v-for="post in posts"
				v-bind:key="post.id"
				v-bind:post="post"
				class="cursor-pointer relative group"
			/>
		</ul>
	</div>
</template>
