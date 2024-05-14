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
			url: null,
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
					this.postStore.updatePost(response.data);
					this.body = '';
					this.url = null;
					this.TogglePopup();

					window.location.reload();
				})
				.catch((error) => {
					console.log('post create error: ', error);
				});
		},
		onFileChange(e) {
			const file = e.target.files[0];
			this.url = URL.createObjectURL(file);
		},
	},
};
</script>

<template>
	<div
		class="fixed z-30 top-0 left-0 w-full h-screen bg-black bg-opacity-60 flex"
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
			class="w-6/12 bg-white rounded flex flex-col mx-auto my-auto max-h-screen"
			@click.stop
		>
			<form
				v-on:submit.prevent="submitForm"
				method="post"
				class="flex flex-col items-center overflow-y-auto"
			>
				<!-- preview  image-->
				<div
					id="preview"
					v-if="url"
					class="flex justify-center w-6/12 mt-2"
				>
					<img :src="url" class="rounded-sm" />
				</div>

				<div class="flex flex-col w-9/12 h-full mt-2 gap-4">
					<!-- upload  image-->
					<label
						for="dropzone-file"
						class="flex flex-col items-center justify-center border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 hover:bg-gray-100 mt-4"
					>
						<div class="flex justify-center py-2 items-center">
							<svg
								class="w-8 h-8 text-gray-500 dark:text-gray-400"
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
							<p
								class="text-sm text-gray-500 dark:text-gray-400 ml-4"
							>
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
							@change="onFileChange"
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
