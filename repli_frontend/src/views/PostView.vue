<script>
import axios from 'axios';
import CommentItem from '@/components/CommentItem.vue';
import { useUserStore } from '@/stores/user';
import { ref } from 'vue';
import PostEdit from '@/components/PostEdit.vue';

export default {
	name: 'PostView',

	setup() {
		const userStore = useUserStore();
		const popupTriggers = ref({
			buttonTrigger: false,
		});

		const TogglePopup = (trigger) => {
			popupTriggers.value[trigger] = !popupTriggers.value[trigger];
		};

		return {
			userStore,
			popupTriggers,
			TogglePopup,
		};
	},

	components: {
		CommentItem,
		PostEdit,
	},
	data() {
		return {
			post: {},
			created_by: {},
			body: '',
			comments: [],
			showExtraModal: false,
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
			axios
				.post(`/api/posts/${this.$route.params.id}/comment/`, {
					body: this.body,
				})
				.then((response) => {
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
		toggleExtraModal() {
			this.showExtraModal = !this.showExtraModal;
		},
		deletePost() {
			axios
				.delete(`/api/posts/${this.post.id}/delete/`)
				.then((response) => {
					this.$router.back();
				})
				.catch((error) => {
					console.log('Comment error', error);
				});
		},
	},
};
</script>
<template>
	<!-- close post -->
	<div
		id="OverlaySection"
		class="fixed z-10 top-0 left-0 w-full h-screen bg-black bg-opacity-60"
		v-on:click="goBack"
	>
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
			<!-- center content -->
			<div class="w-full md:flex h-full overflow-auto rounded-xl">
				<!-- left:post image -->
				<div class="flex items-center bg-white w-full border-r">
					<img
						class="min-w-[400px] mx-auto h-full object-cover"
						alt="image"
						v-for="image in post.attachments"
						v-bind:key="image.id"
						:src="image.get_image"
					/>
				</div>
				<!-- right -->
				<div class="md:max-w-[500px] w-full relative">
					<!-- top: post created_by -->
					<div class="flex items-center justify-between p-3 border-b">
						<div class="flex items-center">
							<RouterLink
								:to="{
									name: 'profile',
									params: { id: created_by.id },
								}"
								class="flex items-center"
							>
								<img
									class="rounded-full w-[38px] h-[38px]"
									:src="created_by.get_avatar"
								/>
								<div class="ml-4 font-extrabold text-[15px]">
									{{ created_by.name }}
								</div>
							</RouterLink>
							<div
								class="flex items-center text-[15px] text-gray-500"
							>
								<span class="-mt-5 ml-2 mr-[5px] text-[35px]"
									>.</span
								>
								<div>{{ post.created_at_formatted }} ago</div>
							</div>
						</div>

						<div
							v-if="created_by.id == userStore.user.id"
							@click="toggleExtraModal"
						>
							<svg
								xmlns="http://www.w3.org/2000/svg"
								fill="none"
								viewBox="0 0 24 24"
								stroke-width="1.5"
								stroke="currentColor"
								class="w-6 h-6"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									d="M6.75 12a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0ZM12.75 12a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0ZM18.75 12a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0Z"
								/>
							</svg>
						</div>
					</div>

					<!-- center: post comment -->
					<div class="overflow-y-auto h-[calc(100%-170px)]">
						<div class="flex items-center justify-between p-3 mb-6">
							<div class="flex items-center relative">
								<img
									class="absolute -top-1 rounded-full w-[38px] h-[38px]"
									:src="created_by.get_avatar"
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

					<!-- bottom: post like and comment count-->
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

					<!-- bottom: create comment -->
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
	<div
		v-if="showExtraModal"
		v-on:click="toggleExtraModal()"
		class="fixed z-20 top-0 left-0 w-full h-screen bg-black bg-opacity-30 flex items-center justify-center"
	>
		<div
			class="max-w-xl w-1/4 h-1/6 mx-auto bg-white rounded-xl flex flex-col justify-around items-center"
			@click.stop
		>
			<button
				v-on:click="() => TogglePopup('buttonTrigger')"
				class="rounded-t-xl w-full h-1/2 flex justify-center items-center cursor-pointer hover:bg-gray-100 focus:bg-gray-200 focus:outline-none space-x-2 text-black"
			>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					fill="none"
					viewBox="0 0 24 24"
					stroke-width="1.5"
					stroke="currentColor"
					class="w-6 h-6"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						d="m16.862 4.487 1.687-1.688a1.875 1.875 0 1 1 2.652 2.652L6.832 19.82a4.5 4.5 0 0 1-1.897 1.13l-2.685.8.8-2.685a4.5 4.5 0 0 1 1.13-1.897L16.863 4.487Zm0 0L19.5 7.125"
					/>
				</svg>
				<span>EDIT</span>
			</button>

			<hr class="w-full" />

			<button
				@click="deletePost"
				class="rounded-b-xl w-full h-1/2 flex justify-center items-center cursor-pointer hover:bg-gray-100 focus:bg-gray-200 focus:outline-none space-x-2 text-red-500"
			>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					fill="none"
					viewBox="0 0 24 24"
					stroke-width="1.5"
					stroke="currentColor"
					class="w-6 h-6"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						d="m20.25 7.5-.625 10.632a2.25 2.25 0 0 1-2.247 2.118H6.622a2.25 2.25 0 0 1-2.247-2.118L3.75 7.5m6 4.125 2.25 2.25m0 0 2.25 2.25M12 13.875l2.25-2.25M12 13.875l-2.25 2.25M3.375 7.5h17.25c.621 0 1.125-.504 1.125-1.125v-1.5c0-.621-.504-1.125-1.125-1.125H3.375c-.621 0-1.125.504-1.125 1.125v1.5c0 .621.504 1.125 1.125 1.125Z"
					/>
				</svg>

				<span>DELETE</span>
			</button>
		</div>
	</div>
	<PostEdit
		v-if="popupTriggers.buttonTrigger"
		v-bind:TogglePopup="() => TogglePopup('buttonTrigger')"
		v-bind:post="post"
	/>
</template>
