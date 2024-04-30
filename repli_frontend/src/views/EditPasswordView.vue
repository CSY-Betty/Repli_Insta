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
				old_password: '',
				new_password1: '',
				new_password2: '',
			},
			errors: [],
		};
	},

	methods: {
		submitForm() {
			this.errors = [];

			if (this.form.new_password1 === '') {
				this.errors.push('Your password is missing.');
			}

			if (this.form.new_password1 !== this.form.new_password2) {
				this.errors.push('The password does not match');
			}

			if (this.errors.length === 0) {
				let formData = new FormData();
				formData.append('old_password', this.form.old_password);
				formData.append('new_password1', this.form.new_password1);
				formData.append('new_password2', this.form.new_password2);

				axios
					.post('/api/editpassword/', formData, {
						headers: {
							'Content-Type': 'multipart/form-data',
						},
					})
					.then((response) => {
						if (response.data.message === 'success') {
							this.toastStore.showToast(
								5000,
								'The information was saved.',
								'bg-emerald-500'
							);

							this.$router.push(
								`/profile/${this.userStore.user.id}`
							);
						} else {
							const data = JSON.parse(response.data.message);

							for (const key in data) {
								this.errors.push(data[key][0].message);
							}
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
					class="bg-white dark:bg-gray-900 shadow-md rounded-lg px-8 py-6 max-w-md flex flex-col gap-2"
				>
					<h1
						class="text-2xl font-bold text-center mb-4 dark:text-gray-200"
					>
						Edit Password
					</h1>

					<!-- signup form -->
					<form v-on:submit.prevent="submitForm">
						<div class="mb-4">
							<label
								for="name"
								class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2"
								>Old Password</label
							>
							<input
								type="password"
								v-model="form.old_password"
								id="name"
								class="shadow-sm rounded-md w-full px-3 py-2 border border-gray-300 focus:outline-none focus:ring-rose-300 focus:border-rose-300"
								placeholder="Your old password"
								required
							/>
						</div>

						<div class="mb-4">
							<label
								for="name"
								class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2"
								>New Password</label
							>
							<input
								type="password"
								v-model="form.new_password1"
								id="name"
								class="shadow-sm rounded-md w-full px-3 py-2 border border-gray-300 focus:outline-none focus:ring-rose-300 focus:border-rose-300"
								placeholder="Your new password"
								required
							/>
						</div>

						<div class="mb-4">
							<label
								for="name"
								class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2"
								>Repeat Password</label
							>
							<input
								type="password"
								v-model="form.new_password2"
								id="name"
								class="shadow-sm rounded-md w-full px-3 py-2 border border-gray-300 focus:outline-none focus:ring-rose-300 focus:border-rose-300"
								placeholder="Repeat password"
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
							<div
								class="bg-red-300 text-white rounded-lg p-6 mt-6"
							>
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
