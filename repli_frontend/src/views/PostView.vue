<script>
import axios from 'axios';
import { comment } from 'postcss';
import { RouterLink } from 'vue-router';
import CommentItem from '@/components/CommentItem.vue';

export default {
	name: 'PostView',
	components: {
		CommentItem,
	},
	data() {
		return {
			post: {},
			created_by: {},
			body: '',
			comments: [],
		};
	},

	mounted() {
		this.getPostDetail();
	},
	methods: {
		getPostDetail() {
			axios
				.get(`/api/posts/${this.$route.params.id}/`)
				.then((response) => {
					console.log('post data', response.data);
					this.post = response.data;
					this.created_by = response.data.created_by;
					this.comments = response.data.comments;
				})
				.catch((error) => {
					console.log('Get error', error);
				});
		},
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
		submitComment() {
			console.log('submitComment', this.body);

			axios
				.post(`/api/posts/${this.$route.params.id}/comment/`, {
					body: this.body,
				})
				.then((response) => {
					console.log('Comment data', response.data);

					this.comments.push(response.data);
					this.post.comments_count += 1;

					this.body = '';
				})
				.catch((error) => {
					console.log('Comment error', error);
				});
		},
		goBack() {
			this.$router.back();
		},
	},
};
</script>
<template>
	<div
		id="OverlaySection"
		class="fixed z-50 top-0 left-0 w-full h-screen bg-black bg-opacity-60"
		v-on:click="goBack"
	>
		<!-- close post -->
		<div class="absolute top-3 right-3">
			<svg
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
		</div>

		<div
			class="max-w-6xl h-[calc(100%-100px)] mx-auto mt-10 bg-white rounded-xl"
			@click.stop
		>
			<div class="w-full md:flex h-full overflow-auto rounded-xl">
				<div class="flex items-center bg-white w-full border-r">
					<img
						class="min-w-[400px] mx-auto h-full"
						alt="image"
						v-for="image in post.attachments"
						v-bind:key="image.id"
						:src="image.get_image"
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
						<div class="flex items-center justify-between p-3 mb-6">
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
						<div
							v-for="comment in comments"
							v-bind:key="comment.id"
							class="p-3"
						>
							<CommentItem v-bind:comment="comment" />
						</div>
						<!-- <div class="pb-16 md:hidden"></div> -->
					</div>
					<hr />
					<div class="flex my-2 items-center gap-4">
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
						<div class="flex flex-row gap-1 items-center">
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
									d="M8.625 12a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0H8.25m4.125 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0H12m4.125 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0h-.375M21 12c0 4.556-4.03 8.25-9 8.25a9.764 9.764 0 0 1-2.555-.337A5.972 5.972 0 0 1 5.41 20.97a5.969 5.969 0 0 1-.474-.065 4.48 4.48 0 0 0 .978-2.025c.09-.457-.133-.901-.467-1.226C3.93 16.178 3 14.189 3 12c0-4.556 4.03-8.25 9-8.25s9 3.694 9 8.25Z"
								/>
							</svg>

							<p class="text-black">
								{{ post.comments_count }} comments
							</p>
						</div>
					</div>
					<hr />
					<form
						v-on:submit.prevent="submitComment"
						method="post"
						class="flex"
					>
						<div class="px-4 w-11/12 bg-white">
							<label for="comment"></label>
							<textarea
								v-model="body"
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
