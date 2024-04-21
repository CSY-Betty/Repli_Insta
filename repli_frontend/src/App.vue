<script>
import Toast from '@/components/Toast.vue';
import { useUserStore } from '@/stores/user.js';
import axios from 'axios';
import { ref } from 'vue';

// try to add PostCreae pop-up
import PostCreate from '@/components/PostCreate.vue';

export default {
	setup() {
		const userStore = useUserStore();
		const popupTriggers = ref({
			buttonTrigger: false,
		});

		const TogglePopup = (trigger) => {
			popupTriggers.value[trigger] = !popupTriggers.value[trigger];
		};

		return {
			userStore,
			PostCreate,
			popupTriggers,
			TogglePopup,
		};
	},
	components: {
		Toast,
		PostCreate,
	},

	beforeCreate() {
		this.userStore.initStore();

		const token = this.userStore.user.access;

		if (token) {
			axios.defaults.headers.common['Authorization'] = 'Bearer ' + token;
		} else {
			axios.defaults.headers.common['Authorization'] = '';
		}
	},
};
</script>

<template>
	<nav class="bg-white w-56 flex-none border-r">
		<div
			class="container mx-auto flex items-center justify-between flex-col h-full"
		>
			<div class="flex items-center">
				<RouterLink
					to="/"
					class="text-rose-400 text-2xl font-semibold mt-8"
					>Repli Insta</RouterLink
				>
			</div>
			<div class="flex flex-col w-9/12 h-full mt-10 gap-10 px-8">
				<div class="flex">
					<svg
						xmlns="http://www.w3.org/2000/svg"
						fill="none"
						viewBox="0 0 24 24"
						stroke-width="1.5"
						stroke="currentColor"
						class="w-6 h-6"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z"
						/>
					</svg>

					<RouterLink
						to="/search"
						class="text-black ml-2 hover:text-rose-400"
						>Search</RouterLink
					>
				</div>
				<div class="flex">
					<svg
						xmlns="http://www.w3.org/2000/svg"
						fill="none"
						viewBox="0 0 24 24"
						stroke-width="1.5"
						stroke="currentColor"
						class="w-6 h-6"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							d="M12 21a9.004 9.004 0 0 0 8.716-6.747M12 21a9.004 9.004 0 0 1-8.716-6.747M12 21c2.485 0 4.5-4.03 4.5-9S14.485 3 12 3m0 18c-2.485 0-4.5-4.03-4.5-9S9.515 3 12 3m0 0a8.997 8.997 0 0 1 7.843 4.582M12 3a8.997 8.997 0 0 0-7.843 4.582m15.686 0A11.953 11.953 0 0 1 12 10.5c-2.998 0-5.74-1.1-7.843-2.918m15.686 0A8.959 8.959 0 0 1 21 12c0 .778-.099 1.533-.284 2.253m0 0A17.919 17.919 0 0 1 12 16.5c-3.162 0-6.133-.815-8.716-2.247m0 0A9.015 9.015 0 0 1 3 12c0-1.605.42-3.113 1.157-4.418"
						/>
					</svg>
					<RouterLink
						to="/explore"
						class="text-black ml-2 hover:text-rose-400"
						>Explore</RouterLink
					>
				</div>
				<div class="flex" v-if="userStore.user.isAuthenticated">
					<svg
						xmlns="http://www.w3.org/2000/svg"
						fill="none"
						viewBox="0 0 24 24"
						stroke-width="1.5"
						stroke="currentColor"
						class="w-6 h-6"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							d="M7.5 8.25h9m-9 3H12m-9.75 1.51c0 1.6 1.123 2.994 2.707 3.227 1.129.166 2.27.293 3.423.379.35.026.67.21.865.501L12 21l2.755-4.133a1.14 1.14 0 0 1 .865-.501 48.172 48.172 0 0 0 3.423-.379c1.584-.233 2.707-1.626 2.707-3.228V6.741c0-1.602-1.123-2.995-2.707-3.228A48.394 48.394 0 0 0 12 3c-2.392 0-4.744.175-7.043.513C3.373 3.746 2.25 5.14 2.25 6.741v6.018Z"
						/>
					</svg>

					<RouterLink
						to="/messages"
						class="text-black ml-2 hover:text-rose-400"
						>Messages</RouterLink
					>
				</div>
				<div class="flex" v-if="userStore.user.isAuthenticated">
					<svg
						xmlns="http://www.w3.org/2000/svg"
						fill="none"
						viewBox="0 0 24 24"
						stroke-width="1.5"
						stroke="currentColor"
						class="w-6 h-6"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							d="M12 9v6m3-3H9m12 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"
						/>
					</svg>

					<button
						class="text-black ml-2 hover:text-rose-400"
						v-on:click="() => TogglePopup('buttonTrigger')"
					>
						Create
					</button>
				</div>
				<div
					class="flex items-center"
					v-if="userStore.user.isAuthenticated"
				>
					<img
						src="https://i.pravatar.cc/30?img=29"
						class="w-6 h-6 rounded-full"
					/>

					<RouterLink
						to="/profile"
						class="text-black ml-2 hover:text-rose-400"
						>Profile</RouterLink
					>
				</div>
				<PostCreate
					v-if="popupTriggers.buttonTrigger"
					v-bind:TogglePopup="() => TogglePopup('buttonTrigger')"
				/>
			</div>
			<div class="flex items-center relative flex-col mb-10">
				<!-- <RouterLink
					to="/signup"
					class="text-black ml-6 hover:text-rose-400 mt-8"
					>Sign up</RouterLink
				> -->
				<RouterLink
					to="/signin"
					v-if="!userStore.user.isAuthenticated"
					class="text-black ml-6 hover:text-rose-400 mt-8"
					>Sign in</RouterLink
				>
				<RouterLink
					to="#"
					v-else="!userStore.user.isAuthenticated"
					class="text-black ml-6 hover:text-rose-400 mt-8"
					>Sign out</RouterLink
				>
			</div>
		</div>
	</nav>
	<RouterView />

	<Toast />
</template>
