<script>
import axios from 'axios';
import { RouterLink } from 'vue-router';

export default {
	name: 'PostView',
	data() {
		return {
			post: {},
			created_by: {},
		};
	},

	mounted() {
		axios
			.get(`/api/posts/post/${this.$route.params.id}/`)
			.then((response) => {
				console.log('post data', response.data);
				this.post = response.data;
				this.created_by = response.data.created_by;
			})
			.catch((error) => {
				console.log('Get error', error);
			});
	},
	methods: {
		likePost(id) {
			axios
				.post(`/api/posts/${id}/like/`)
				.then((response) => {
					if (response.data.message == 'like created') {
						this.post.likes_count += 1;
					}
				})
				.catch((error) => {
					console.log('Like error', error);
				});
		},
	},
};
</script>
<template>
	<div
		id="OverlaySection"
		class="fixed z-50 top-0 left-0 w-full h-screen bg-black bg-opacity-60"
	>
		<RouterLink to="/explore" class="absolute top-3 right-3"
			><svg
				xmlns="http://www.w3.org/2000/svg"
				viewBox="0 0 24 24"
				fill="currentColor"
				class="w-8 h-8"
			>
				<path
					fill-rule="evenodd"
					d="M5.47 5.47a.75.75 0 0 1 1.06 0L12 10.94l5.47-5.47a.75.75 0 1 1 1.06 1.06L13.06 12l5.47 5.47a.75.75 0 1 1-1.06 1.06L12 13.06l-5.47 5.47a.75.75 0 0 1-1.06-1.06L10.94 12 5.47 6.53a.75.75 0 0 1 0-1.06Z"
					clip-rule="evenodd"
				/>
			</svg>
		</RouterLink>

		<div
			class="max-w-6xl h-[calc(100%-100px)] mx-auto mt-10 bg-white rounded-xl"
		>
			<div class="w-full md:flex h-full overflow-auto rounded-xl">
				<div class="flex items-center bg-black w-full">
					<img
						class="min-w-[400px] mx-auto h-full"
						alt="image"
						src="https://picsum.photos/id/54/800/820"
					/>
				</div>
				<div class="md:max-w-[500px] w-full relative">
					<div class="flex items-center justify-between p-3 border-b">
						<div class="flex items-center">
							<img
								class="rounded-full w-[38px] h-[38px]"
								src="https://picsum.photos/id/54/800/820"
							/>
							<div class="ml-4 font-extrabold text-[15px]">
								{{ created_by.name }}
							</div>
							<div
								class="flex items-center text-[15px] text-gray-500"
							>
								<span class="-mt-5 ml-2 mr-[5px] text-[35px]"
									>.</span
								>
								<div>{{ post.created_at_formatted }} ago</div>
							</div>
						</div>
						<button>...</button>
					</div>
					<div class="overflow-y-auto h-[calc(100%-170px)]">
						<div class="flex items-center justify-between p-3">
							<div class="flex items-center relative">
								<img
									class="absolute -top-1 rounded-full w-[38px] h-[38px]"
									src="https://picsum.photos/id/54/800/820"
								/>
								<div class="ml-14">
									<span
										class="font-extrabold text-[15px] mr-2"
									>
										{{ created_by.name }}
									</span>
									<span class="text-[15px] text-gray-900">
										{{ post.body }}
									</span>
								</div>
							</div>
						</div>
						<div class="p-3">
							<div class="flex items-center justify-between">
								<div class="flex items-center">
									<img
										class="rounded-full w-[38px] h-[38px]"
										src="https://picsum.photos/id/54/800/820"
									/>
									<div
										class="ml-4 font-extrabold text-[15px]"
									>
										Name Here
										<span
											class="font-light text-gray-700 text-sm"
											>Date here</span
										>
									</div>
								</div>
								<button>...</button>
							</div>
							<div class="text-[13px] pl-[55px]">
								THIS COMMENT SECTION
							</div>
						</div>
						<!-- <div class="pb-16 md:hidden"></div> -->
					</div>
					<hr />
					<div class="flex my-2 items-center justify-between">
						<div class="flex items-center">
							<button @click="likePost(post.id)" class="ml-4">
								<svg
									xmlns="http://www.w3.org/2000/svg"
									fill="none"
									viewBox="0 0 24 24"
									stroke-width="1.5"
									stroke="currentColor"
									class="w-8 h-8"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z"
									/>
								</svg>
							</button>
							<span class="ml-2"
								>{{ post.likes_count }} likes</span
							>
						</div>
					</div>
					<hr />
					<form class="flex">
						<div class="px-4 w-11/12 bg-white">
							<label for="comment"></label>
							<textarea
								id="comment"
								class="mt-2 px-0 w-full text-sm text-gray-900 border-0 focus:ring-0 focus:outline-none"
								placeholder="Write a comment..."
								required
							></textarea>
						</div>
						<button
							type="submit"
							class="inline-flex items-center py-2.5 px-4 text-xs font-medium text-center text-rose-500"
						>
							Post
						</button>
					</form>
				</div>
			</div>
		</div>
	</div>
</template>
