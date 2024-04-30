<script>
import axios from 'axios';
import PeopleYouMayKnow from '@/components/PeopleYouMayKnow.vue';
import { RouterLink } from 'vue-router';

export default {
	name: 'FriendsView',

	components: {
		PeopleYouMayKnow,
	},
	data() {
		return {
			user: {},
			friendshipRequests: [],
			friends: [],
		};
	},
	mounted() {
		this.getFriends();
	},
	methods: {
		getFriends() {
			axios
				.get(`/api/friends/${this.$route.params.id}/`)
				.then((response) => {
					this.friendshipRequests = response.data.requests;
					this.friends = response.data.friends;
					this.user = response.data.user;
				})
				.catch((error) => {
					console.log('Get friends error', error);
				});
		},
		handleRequest(status, pk) {
			axios
				.post(`/api/friends/${pk}/${status}/`)
				.then((response) => {})
				.catch((error) => {
					console.log('Get friends error', error);
				});
		},
	},
};
</script>

<template>
	<div class="w-screen mt-6 flex flex-col items-center">
		<div
			v-if="friendshipRequests.length"
			class="w-6/12 container mx-auto overflow-y-auto flex flex-col items-center"
		>
			<div class="flex flex-col text-lg font-semibold mb-2">
				Friendship Requests
			</div>

			<div
				v-for="friendshipRequest in friendshipRequests"
				class="flex flex-row my-4 w-full items-center border rounded"
			>
				<RouterLink
					v-bind:key="friendshipRequest.id"
					:to="{
						name: 'profile',
						params: { id: friendshipRequest.created_by.id },
					}"
					class="w-8/12 px-4 py-2 flex items-center cursor-pointer hover:bg-gray-50 bg-white text-black"
				>
					<img
						src="https://i.pravatar.cc/150?img=29"
						class="w-16 aspect-square rounded-full"
					/>
					<p class="ml-2 text-xl">
						{{ friendshipRequest.created_by.name }}
					</p>
				</RouterLink>
				<button
					@click="
						handleRequest(
							'acceptd',
							friendshipRequest.created_by.id
						)
					"
					class="w-2/12 px-8 mr-2 flex justify-center items-center cursor-pointer rounded bg-green-100 hover:bg-green-300 text-black"
				>
					Accept
				</button>
				<button
					@click="
						handleRequest(
							'rejected',
							friendshipRequest.created_by.id
						)
					"
					class="w-2/12 px-8 mr-2 flex justify-center items-center cursor-pointer rounded bg-red-100 hover:bg-red-300 text-black"
				>
					Reject
				</button>
			</div>

			<!-- <PeopleYouMayKnow /> -->
		</div>
		<hr />
		<div
			v-if="friends.length"
			class="container mx-auto overflow-y-auto flex flex-col items-center"
		>
			<RouterLink
				v-for="user in friends"
				v-bind:key="user.id"
				:to="{ name: 'profile', params: { id: user.id } }"
				class="max-w-md px-10 py-2 w-full flex items-center cursor-pointer hover:bg-gray-50 bg-white text-black"
			>
				<img
					src="https://i.pravatar.cc/150?img=29"
					class="w-16 aspect-square rounded-full"
				/>
				<p class="ml-2 text-xl">{{ user.name }}</p>
			</RouterLink>

			<!-- <PeopleYouMayKnow /> -->
		</div>
	</div>
</template>
