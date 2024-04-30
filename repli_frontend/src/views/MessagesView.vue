<script>
import axios from 'axios';
import { useUserStore } from '@/stores/user';

export default {
	name: 'MessagesView',
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
		this.getConversations();
	},
	methods: {
		setActiveConversation(id) {
			this.activeConversation = id;
			this.getMessages();
		},

		getConversations() {
			axios
				.get('/api/chat/')
				.then((response) => {
					this.conversations = response.data;

					if (this.conversations) {
						this.activeConversation = this.conversations[0].id;
					}

					this.getMessages();
				})
				.catch((error) => {
					console.log(error);
				});
		},
		getMessages() {
			axios
				.get(`/api/chat/${this.activeConversation}/`)
				.then((response) => {
					this.activeConversation = response.data;
				})
				.catch((error) => {
					console.log(error);
				});
		},
		sendMessage() {
			axios
				.post(`/api/chat/${this.activeConversation.id}/send/`, {
					body: this.body,
				})
				.then((response) => {
					this.activeConversation.messages.push(response.data);
					this.body = '';
				})
				.catch((error) => {
					console.log(error);
				});
		},
	},
};
</script>
<template>
	<main class="grid grid-cols-4 w-full">
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
					<button
						v-if="user.id !== userStore.user.id"
						class="px-10 py-2 w-full flex items-center cursor-pointer hover:bg-gray-50 bg-white text-black focus:bg-gray-100"
					>
						<img
							:src="user.get_avatar"
							class="w-16 aspect-square rounded-full"
						/>
						<p class="ml-2 text-xl">{{ user.name }}</p>
					</button>
				</template>
			</div>
		</article>
		<section class="col-span-3 pt-6 h-screen">
			<div class="grid grid-rows-10 h-full">
				<!-- Sender -->
				<div class="border-b">
					<div
						class="px-10 w-fit flex items-center bg-white text-black"
						v-for="user in activeConversation.users"
					>
						<div
							class="flex items-center"
							v-if="user.id !== userStore.user.id"
						>
							<img
								:src="user.get_avatar"
								class="w-16 aspect-square rounded-full"
							/>

							<p class="ml-6 text-xl">{{ user.name }}</p>
						</div>
					</div>
				</div>

				<!-- Chat bubble -->
				<div class="mt-2 row-span-8 overflow-y-auto">
					<template
						v-for="message in activeConversation.messages"
						v-bind:key="message.id"
						class="grid gap-2"
					>
						<!-- Chat bubble sender -->
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
								alt="Jese image"
							/>
						</div>
						<div v-else class="flex items-end gap-2.5 pl-4 py-2">
							<img
								class="w-8 h-8 rounded-full"
								:src="message.created_by.get_avatar"
								alt="Jese image"
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

						<!-- Chat bubble receiver -->
					</template>
				</div>
				<!-- Message box -->
				<div class="border-t pt-2">
					<form v-on:submit.prevent="sendMessage" class="px-10">
						<div
							class="flex items-center border border-gray-300 py-2 px-2 rounded-full"
						>
							<textarea
								v-model="body"
								class="appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none"
								type="text"
								placeholder="Message..."
							></textarea>
							<button
								class="flex-shrink-0 bg-rose-400 hover:bg-rose-500 border-rose-400 hover:border-rose-500 text-sm border-4 text-white py-1 px-2 rounded-full"
								type="submit"
							>
								Send
							</button>
						</div>
					</form>
				</div>
			</div>
		</section>
	</main>
</template>
