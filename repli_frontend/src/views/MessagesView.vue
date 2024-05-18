<script>
import axios from 'axios';
import { useUserStore } from '@/stores/user';
import { RouterLink } from 'vue-router';

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
			rooms: [],
		};
	},

	mounted() {
		this.getChatRoom();
	},
	methods: {
		getChatRoom() {
			axios
				.get('api/chat/list-rooms/')
				.then((response) => {
					// this.rooms = response.data.rooms;
					this.rooms = [...response.data.rooms];
				})
				.catch((error) => {
					console.log('error:', error);
				});
		},
	},
};
</script>
<template>
	<main class="w-56">
		<article
			class="col-span-1 justify-center pt-6 overflow-y-auto border-r h-screen w-56"
		>
			<div v-for="room in rooms" v-bind:key="room.id">
				<template v-if="room.participants1.id !== userStore.user.id">
					<RouterLink
						:to="{
							name: 'message',
							params: { id: room.id },
						}"
						class="px-10 py-2 w-full flex items-center cursor-pointer hover:bg-gray-50 bg-white text-black focus:bg-gray-100"
					>
						<img
							:src="room.participants1.get_avatar"
							class="w-10 aspect-square rounded-full"
						/>
						<p class="ml-2 text-xl">
							{{ room.participants1.name }}
						</p>
					</RouterLink>
				</template>
				<template v-if="room.participants2.id !== userStore.user.id">
					<RouterLink
						:to="{
							name: 'message',
							params: { id: room.id },
						}"
						class="px-10 py-2 w-full flex items-center cursor-pointer hover:bg-gray-50 bg-white text-black focus:bg-gray-100"
					>
						<img
							:src="room.participants2.get_avatar"
							class="w-10 aspect-square rounded-full"
						/>
						<p class="ml-2 text-xl">
							{{ room.participants2.name }}
						</p>
					</RouterLink>
				</template>
			</div>
		</article>
	</main>
	<router-view />
</template>
