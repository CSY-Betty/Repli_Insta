<script>
import axios from 'axios';
import { usePostStore } from '@/stores/post';

export default {
	setup() {
		const postStore = usePostStore();

		return {
			postStore,
		};
	},
	props: ['TogglePopup'],
	data() {
		return {
			body: '',
			posts: [],
		};
	},
	methods: {
		submitForm() {
			console.log('submit post', this.body);

			axios
				.post('/api/posts/create/', {
					body: this.body,
				})
				.then((response) => {
					console.log('post create success data: ', response.data);
					this.postStore.updatePost(response.data);
				})
				.catch((error) => {
					console.log('post create error: ', error);
				});
		},
	},
};
</script>

<template>
	<div
		class="bg-gray-500/50 w-screen h-screen z-10 fixed top-0 left-0 flex justify-center items-center"
	>
		<div class="w-6/12 h-3/6 bg-white rounded flex flex-col">
			<form v-on:submit.prevent="submitForm" method="post">
				<div>Post Content</div>
				<textarea
					v-model="body"
					class="border w-6/12"
					placeholder="Write Something...."
				></textarea>
				<button>Add Post</button>
				<button v-on:click="TogglePopup()">
					<svg
						xmlns="http://www.w3.org/2000/svg"
						viewBox="0 0 24 24"
						fill="currentColor"
						class="w-6 h-6"
					>
						<path
							fill-rule="evenodd"
							d="M5.47 5.47a.75.75 0 0 1 1.06 0L12 10.94l5.47-5.47a.75.75 0 1 1 1.06 1.06L13.06 12l5.47 5.47a.75.75 0 1 1-1.06 1.06L12 13.06l-5.47 5.47a.75.75 0 0 1-1.06-1.06L10.94 12 5.47 6.53a.75.75 0 0 1 0-1.06Z"
							clip-rule="evenodd"
						/>
					</svg>
				</button>
			</form>
		</div>
	</div>
</template>
