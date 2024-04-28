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
			let formData = new FormData();
			formData.append('image', this.$refs.file.files[0]);
			formData.append('body', this.body);

			axios
				.post('/api/posts/create/', formData, {
					headers: {
						'Content-Type': 'multipart/form-data',
					},
				})
				.then((response) => {
					console.log('post create success data: ', response.data);
					this.postStore.updatePost(response.data);
					this.body = '';
					this.TogglePopup();

					window.location.reload();
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
		class="fixed z-10 top-0 left-0 w-full h-screen bg-black bg-opacity-60 flex"
		@click="TogglePopup()"
	>
		<div class="absolute top-3 right-3">
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
		</div>
		<div
			class="w-6/12 h-3/6 bg-white rounded flex flex-col m-auto"
			@click.stop
		>
			<form
				v-on:submit.prevent="submitForm"
				method="post"
				class="flex flex-col items-center h-full"
			>
				<!-- upload  image-->
				<div class="flex flex-col w-9/12 h-full mt-4 gap-4">
					<label
						for="dropzone-file"
						class="flex flex-col items-center justify-center h-1/5 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 hover:bg-gray-100 mt-4"
					>
						<div
							class="flex flex-col items-center justify-center py-4"
						>
							<svg
								class="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400"
								aria-hidden="true"
								xmlns="http://www.w3.org/2000/svg"
								fill="none"
								viewBox="0 0 20 16"
							>
								<path
									stroke="currentColor"
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"
								/>
							</svg>
							<p class="text-sm text-gray-500 dark:text-gray-400">
								<span class="font-semibold"
									>Click to upload</span
								>
							</p>
						</div>
						<input
							id="dropzone-file"
							type="file"
							ref="file"
							class="hidden"
						/>
					</label>
					<!-- content -->
					<div class="flex flex-col items-center w-full">
						<label
							for="message"
							class="mt-6 block mb-2 text-sm font-medium text-gray-900 self-start"
							>Your message</label
						>
						<textarea
							v-model="body"
							id="message"
							rows="6"
							class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-rose-500 focus:border-rose-500"
							placeholder="Write your thoughts here..."
						></textarea>
					</div>
					<button
						type="submit"
						class="text-white bg-rose-300 hover:bg-rose-500 focus:ring-rose-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 self-end"
					>
						Add Post
					</button>
				</div>
			</form>
		</div>
	</div>
</template>
