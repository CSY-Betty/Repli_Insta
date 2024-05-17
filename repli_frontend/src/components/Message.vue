<script>
import axios from 'axios';
import { useUserStore } from '@/stores/user';
import { RouterLink } from 'vue-router';
import ChatView from '@/views/ChatListView.vue';
import ParticipantItem from './ParticipantItem.vue';

export default {
	setup() {
		const userStore = useUserStore();
		return {
			userStore,
		};
	},
	components: { ChatView, ParticipantItem },
	data() {
		return {
			chatSocket: null,
			newMessage: '',
			activeConversation: [],
			roomId: this.$route.params.id,
			room: {},
			messages: [],
		};
	},
	mounted() {
		this.chats();
		this.getMessages();
	},
	methods: {
		getMessages() {
			axios
				.get(`api/chat/room/${this.roomId}`)
				.then((response) => {
					console.log(response.data);
					this.messages = response.data.messages;
					this.room = response.data.room;
				})
				.catch((error) => {
					console.log('error:', error);
				});
		},
		chats() {
			// console.log(this.userStore.user.id);
			// console.log(this.roomId);

			this.chatSocket = new WebSocket(
				`ws://localhost:8000/ws/${this.roomId}/`
			);

			// get message from backend
			this.chatSocket.onmessage = (e) => {
				console.log('onMessage');
				console.log(e.data);
				console.log(JSON.parse(e.data));

				const newMessage = JSON.parse(e.data);
				this.activeConversation.push(newMessage);

				// this.activeConversation = JSON.parse(e.data);

				console.log(this.activeConversation);
			};

			this.chatSocket.onerror = function (error) {
				console.error('WebSocket error: ', error);
			};

			this.chatSocket.onopen = function (e) {
				console.log('onopen - open');
			};

			this.chatSocket.onclose = function (e) {
				console.log('onClose - chat');
			};
		},
		sendMessage() {
			this.chatSocket.send(
				JSON.stringify({
					type: 'message',
					message: this.newMessage,
					name: this.userStore.user.id,
				})
			);
			this.message = '';
		},
	},
};
</script>

<template>
	<!-- <ChatView /> -->
	<section class="pt-6 h-screen w-full">
		<div class="grid grid-rows-10 h-full">
			<div v-if="room.participants1 && room.participants2">
				<ParticipantItem
					v-if="room.participants1.id != userStore.user.id"
					:participant="room.participants1"
				/>
				<ParticipantItem
					v-if="room.participants2.id != userStore.user.id"
					:participant="room.participants2"
				/>
			</div>
			<div class="mt-2 row-span-8 overflow-y-auto pt-10">
				<div v-for="message in messages" :key="message.id">
					<div
						v-if="message.created_by.id == userStore.user.id"
						class="flex items-end gap-2.5 px-4 py-2 justify-end"
					>
						<div
							class="flex flex-col w-full max-w-[320px] leading-1.5 p-4 border-gray-200 bg-gray-100 rounded-s-xl rounded-se-xl dark:bg-gray-700"
						>
							<p
								class="text-sm font-normal py-2.5 text-gray-900 dark:text-white"
							>
								{{ message.body }}
							</p>
						</div>
						<img
							class="w-8 h-8 rounded-full"
							:src="message.created_by.get_avatar"
							alt="avatar"
						/>
					</div>
					<div v-else class="flex items-end gap-2.5 pl-4 py-2">
						<img
							class="w-8 h-8 rounded-full"
							:src="message.created_by.get_avatar"
							alt="avatar"
						/>
						<div
							class="flex flex-col w-full max-w-[320px] leading-1.5 p-4 border-gray-200 bg-gray-100 rounded-ss-xl rounded-e-xl dark:bg-gray-700"
						>
							<p
								class="text-sm font-normal py-2.5 text-gray-900 dark:text-white"
							>
								{{ message.body }}
							</p>
						</div>
					</div>
				</div>

				<div
					v-for="conversation in activeConversation"
					:key="conversation.id"
				>
					<div
						v-if="conversation.name.id == userStore.user.id"
						class="flex items-end gap-2.5 px-4 py-2 justify-end"
					>
						<div
							class="flex flex-col w-full max-w-[320px] leading-1.5 p-4 border-gray-200 bg-gray-100 rounded-s-xl rounded-se-xl dark:bg-gray-700"
						>
							<p
								class="text-sm font-normal py-2.5 text-gray-900 dark:text-white"
							>
								{{ conversation.message }}
							</p>
						</div>
						<img
							class="w-8 h-8 rounded-full"
							:src="conversation.name.get_avatar"
							alt="Myavatar"
						/>
					</div>
					<div v-else class="flex items-end gap-2.5 pl-4 py-2">
						<img
							class="w-8 h-8 rounded-full"
							:src="conversation.name.get_avatar"
							alt="Jese image"
						/>
						<div
							class="flex flex-col w-full max-w-[320px] leading-1.5 p-4 border-gray-200 bg-gray-100 rounded-ss-xl rounded-e-xl dark:bg-gray-700"
						>
							<p
								class="text-sm font-normal py-2.5 text-gray-900 dark:text-white"
							>
								{{ conversation.message }}
							</p>
						</div>
					</div>
				</div>
			</div>

			<div class="border-t pt-2">
				<form class="px-10">
					<div
						class="flex items-center border border-gray-300 py-2 px-2 rounded-full"
					>
						<textarea
							class="appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none"
							type="text"
							placeholder="Message..."
							v-model="newMessage"
						></textarea>
						<button
							class="flex-shrink-0 bg-rose-400 hover:bg-rose-500 border-rose-400 hover:border-rose-500 text-sm border-4 text-white py-1 px-2 rounded-full"
							type="submit"
							v-on:click.prevent="sendMessage"
						>
							Send
						</button>
					</div>
				</form>
			</div>
		</div>
	</section>
</template>
