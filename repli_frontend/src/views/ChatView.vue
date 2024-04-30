<script>
import axios from 'axios';
import { useUserStore } from '@/stores/user';
import { RouterLink } from 'vue-router';

export default {
	name: 'ChatView',
	setup() {
		const userStore = useUserStore();
		return {
			userStore,
		};
	},
	data() {
		return {
			conversations: [],
			activeConversation: {},
			body: '',
		};
	},

	mounted() {
		this.getChatRoom();
	},
	methods: {
		getChatRoom() {
			axios
				.get('api/chat/get-room/')
				.then((response) => {
					console.log(response.data);
					// chatSocket = new WebSocket(
					// 	`ws://${window.location.host}/chat-room/${chatRoomUuid}`
					// );

					// chatSocket.onmessage = function (e) {
					// 	console.log('onMessage');
					// };

					// chatSocket.onopen = function (e) {
					// 	console.log('onopen - open');
					// };

					// chatSocket.onclose = function (e) {
					// 	console.log('onClose - chat');
					// };
				})
				.catch((error) => {
					console.log('error:', error);
				});
		},
	},
};
</script>
<template>
	<main class="w-1/5">
		<article
			class="col-span-1 justify-c enter pt-6 overflow-y-auto border-r h-screen"
		>
			<div
				v-for="conversation in conversations"
				v-bind:key="conversation.id"
				v-on:click="setActiveConversation(conversation.id)"
			>
				<template
					v-for="user in conversation.users"
					v-bind:key="user.id"
				>
					<RouterLink
						:to="{ name: 'Chat', params: { id: user.id } }"
						v-if="user.id !== userStore.user.id"
						class="px-10 py-2 w-full flex items-center cursor-pointer hover:bg-gray-50 bg-white text-black focus:bg-gray-100"
					>
						<img
							:src="user.get_avatar"
							class="w-16 aspect-square rounded-full"
						/>
						<p class="ml-2 text-xl">{{ user.name }}</p>
					</RouterLink>
				</template>
			</div>
		</article>
	</main>
</template>
