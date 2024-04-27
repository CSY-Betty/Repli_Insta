<script>
import axios from 'axios';
import { useToastStore } from '@/stores/toast';
import { useUserStore } from '@/stores/user';

export default {
	setup() {
		const toastStore = useToastStore();
		const userStore = useUserStore();

		return {
			toastStore,
			userStore,
		};
	},

	data() {
		return {
			form: {
				email: this.userStore.user.email,
				name: this.userStore.user.name,
			},
			errors: [],
		};
	},

	methods: {
		submitForm() {
			this.errors = [];

			if (this.form.name === '') {
				console.log('Your name is missing.');
				this.errors.push('Your name is missing.');
			}

			if (this.form.email === '') {
				console.log('Your email is missing.');

				this.errors.push('Your email is missing.');
			}

			if (this.errors.length === 0) {
				let formData = new FormData();
				formData.append('avatar', this.$refs.file.files[0]);
				formData.append('name', this.form.name);
				formData.append('email', this.form.email);

				axios
					.post('/api/editprofile/', formData, {
						headers: {
							'Content-Type': 'multipart/form-data',
						},
					})
					.then((response) => {
						if (response.data.message === 'information updated.') {
							console.log('success');
							this.toastStore.showToast(
								5000,
								'The information was saved.',
								'bg-emerald-500'
							);

							// update the us er store in the browser
							this.userStore.setUserInfo({
								id: this.userStore.user.id,
								name: this.form.name,
								email: this.form.email,
								avatar: response.data.user.get_avatar,
							});

							this.$router.back();
						} else {
							console.log(
								'response.data.message: ',
								response.data.message
							);
							this.toastStore.showToast(
								5000,
								`${response.data.message}. Please try again`,
								'bg-red-300'
							);
						}
					})
					.catch((error) => {
						console.log('error', error);
					});
			}
		},
	},
};
</script>

<template>
	<section class="flex-1 min-w-0 overflow-auto">
		<div class="flex items-center justify-center">
			<div
				class="min-h-screen flex items-center justify-center w-full dark:bg-gray-950"
			>
				<div
					class="bg-white dark:bg-gray-900 shadow-md rounded-lg px-8 py-6 max-w-md"
				>
					<h1
						class="text-2xl font-bold text-center mb-4 dark:text-gray-200"
					>
						Edit Profile
					</h1>

					<!-- signup form -->
					<form v-on:submit.prevent="submitForm">
						<div class="mb-4">
							<label
								for="avatar"
								class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2"
								>Avatar</label
							>
							<input
								type="file"
								id="avatar"
								ref="file"
								class="shadow-sm rounded-md w-full px-3 py-2 border border-gray-300 focus:outline-none focus:ring-rose-300 focus:border-rose-300"
							/>
						</div>
						<div class="mb-4">
							<label
								for="name"
								class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2"
								>Name</label
							>
							<input
								type="text"
								v-model="form.name"
								id="name"
								class="shadow-sm rounded-md w-full px-3 py-2 border border-gray-300 focus:outline-none focus:ring-rose-300 focus:border-rose-300"
								placeholder="your name"
								required
							/>
						</div>
						<div class="mb-4">
							<label
								for="email"
								class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2"
								>Email Address</label
							>
							<input
								type="email"
								v-model="form.email"
								id="email"
								class="shadow-sm rounded-md w-full px-3 py-2 border border-gray-300 focus:outline-none focus:ring-rose-300 focus:border-rose-300"
								placeholder="your@email.com"
								required
							/>
						</div>

						<button
							class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-rose-500 hover:bg-rose-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-rose-500"
						>
							Save changes
						</button>

						<!-- error handling -->
						<template v-if="errors.length > 0">
							<div class="bg-red-300 text-white rounded-lg p-6">
								<p v-for="error in errors" v-bind:key="error">
									{{ error }}
								</p>
							</div>
						</template>
					</form>
				</div>
			</div>
		</div>
	</section>
</template>
