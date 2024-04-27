<script>
import axios from 'axios';
import { useUserStore } from '@/stores/user.js';

export default {
	setup() {
		const userStore = useUserStore();

		return {
			userStore,
		};
	},
	data() {
		return {
			form: {
				email: '',
				password: '',
			},
			errors: [],
		};
	},
	methods: {
		async submitForm() {
			this.errors = [];

			if (this.form.email === '') {
				console.log('Your email is missing.');

				this.errors.push('Your email is missing.');
			}

			if (this.form.password === '') {
				this.errors.push('Your password is missing.');
			}

			if (this.errors.length === 0) {
				await axios
					.post('/api/login/', this.form)
					.then((response) => {
						this.userStore.setToken(response.data);

						axios.defaults.headers.common['Authorization'] =
							'Bearer ' + response.data.access;
					})
					.catch((error) => {
						console.log('error', error);

						this.errors.push('The email or password is incorrect!');
					});
			}

			if (this.errors.length === 0) {
				await axios
					.get('/api/me/', this.form)
					.then((response) => {
						this.userStore.setUserInfo(response.data);

						this.$router.push('/explore');
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
			<!-- component -->
			<div
				class="min-h-screen flex items-center justify-center w-full dark:bg-gray-950"
			>
				<div
					class="bg-white dark:bg-gray-900 shadow-md rounded-lg px-8 py-6 max-w-md"
				>
					<h1
						class="text-2xl font-bold text-center mb-4 dark:text-gray-200"
					>
						Welcome Back!
					</h1>
					<form v-on:submit.prevent="submitForm">
						<div class="mb-4">
							<label
								for="email"
								class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2"
								>Email Address</label
							>
							<input
								type="email"
								id="email"
								v-model="form.email"
								class="shadow-sm rounded-md w-full px-3 py-2 border border-gray-300 focus:outline-none focus:ring-rose-300 focus:border-rose-300"
								placeholder="your@email.com"
								required
							/>
						</div>
						<div class="mb-4">
							<label
								for="password"
								class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2"
								>Password</label
							>
							<input
								type="password"
								id="password"
								v-model="form.password"
								class="shadow-sm rounded-md w-full px-3 py-2 border border-gray-300 focus:outline-none focus:ring-rose-300 focus:border-rose-300"
								value="repliinsta"
								required
							/>
							<a
								href="#"
								class="text-xs text-gray-600 hover:text-rose-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-rose-500"
								>Forgot Password?</a
							>
						</div>
						<div class="flex items-center justify-between mb-4">
							<div class="flex items-center">
								<input
									type="checkbox"
									id="remember"
									class="h-4 w-4 rounded border-gray-300 text-rose-600 focus:ring-rose-500 focus:outline-none"
									checked
								/>
								<label
									for="remember"
									class="ml-2 block text-sm text-gray-700 dark:text-gray-300"
									>Remember me</label
								>
							</div>
							<RouterLink
								to="/signup"
								class="text-xs text-black hover:text-rose-400 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-rose-500"
								>Create Account</RouterLink
							>
						</div>
						<button
							type="submit"
							class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-rose-500 hover:bg-rose-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-rose-500"
						>
							Login
						</button>
						<!-- Divider -->
						<div
							class="my-4 flex items-center before:mt-0.5 before:flex-1 before:border-t before:border-neutral-300 after:mt-0.5 after:flex-1 after:border-t after:border-neutral-300 dark:before:border-neutral-500 dark:after:border-neutral-500"
						>
							<p
								class="mx-4 mb-0 text-center font-semibold dark:text-neutral-200"
							>
								OR
							</p>
						</div>

						<!-- Social login buttons -->
						<a
							class="mb-3 flex w-full items-center justify-center rounded bg-primary px-7 pb-2.5 pt-3 text-center text-sm font-medium uppercase leading-normal text-white shadow-primary-3 transition duration-150 ease-in-out hover:bg-primary-accent-300 hover:shadow-primary-2 focus:bg-primary-accent-300 focus:shadow-primary-2 focus:outline-none focus:ring-0 active:bg-primary-600 active:shadow-primary-2 dark:shadow-black/30 dark:hover:shadow-dark-strong dark:focus:shadow-dark-strong dark:active:shadow-dark-strong"
							style="background-color: #3b5998"
							href="#!"
							role="button"
							data-twe-ripple-init
							data-twe-ripple-color="light"
						>
							<!-- Facebook -->
							<span
								class="me-2 fill-white [&>svg]:mx-auto [&>svg]:h-3.5 [&>svg]:w-3.5"
							>
								<svg
									xmlns="http://www.w3.org/2000/svg"
									viewBox="0 0 320 512"
								>
									<!--!Font Awesome Free 6.5.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc. -->
									<path
										d="M80 299.3V512H196V299.3h86.5l18-97.8H196V166.9c0-51.7 20.3-71.5 72.7-71.5c16.3 0 29.4 .4 37 1.2V7.9C291.4 4 256.4 0 236.2 0C129.3 0 80 50.5 80 159.4v42.1H14v97.8H80z"
									/>
								</svg>
							</span>
							Continue with Facebook
						</a>
						<a
							class="mb-3 flex w-full items-center justify-center rounded bg-info px-7 pb-2.5 pt-3 text-center text-sm font-medium uppercase leading-normal text-white shadow-info-3 transition duration-150 ease-in-out hover:bg-info-accent-300 hover:shadow-info-2 focus:bg-info-accent-300 focus:shadow-info-2 focus:outline-none focus:ring-0 active:bg-info-600 active:shadow-info-2 dark:shadow-black/30 dark:hover:shadow-dark-strong dark:focus:shadow-dark-strong dark:active:shadow-dark-strong"
							style="background-color: #e72929"
							href="#!"
							role="button"
							data-twe-ripple-init
							data-twe-ripple-color="light"
						>
							<!-- Google -->
							<span
								class="me-2 fill-white [&>svg]:h-3.5 [&>svg]:w-3.5"
							>
								<svg
									xmlns="http://www.w3.org/2000/svg"
									x="0px"
									y="0px"
									width="100"
									height="100"
									viewBox="0,0,256,256"
								>
									<g
										fill="#ffffff"
										fill-rule="nonzero"
										stroke="none"
										stroke-width="1"
										stroke-linecap="butt"
										stroke-linejoin="miter"
										stroke-miterlimit="10"
										stroke-dasharray=""
										stroke-dashoffset="0"
										font-family="none"
										font-weight="none"
										font-size="none"
										text-anchor="none"
										style="mix-blend-mode: normal"
									>
										<g transform="scale(5.12,5.12)">
											<path
												d="M25.99609,48c-12.68359,0 -23.00391,-10.31641 -23.00391,-23c0,-12.68359 10.32031,-23 23.00391,-23c5.74609,0 11.24609,2.12891 15.49219,5.99609l0.77344,0.70703l-7.58594,7.58594l-0.70312,-0.60156c-2.22656,-1.90625 -5.05859,-2.95703 -7.97656,-2.95703c-6.76562,0 -12.27344,5.50391 -12.27344,12.26953c0,6.76563 5.50781,12.26953 12.27344,12.26953c4.87891,0 8.73438,-2.49219 10.55078,-6.73828h-11.55078v-10.35547l22.55078,0.03125l0.16797,0.79297c1.17578,5.58203 0.23438,13.79297 -4.53125,19.66797c-3.94531,4.86328 -9.72656,7.33203 -17.1875,7.33203z"
											></path>
										</g>
									</g>
								</svg>
							</span>
							Continue with Google
						</a>
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
