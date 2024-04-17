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
					<form action="#">
						<div class="mb-4">
							<label
								for="email"
								class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2"
								>Email Address</label
							>
							<input
								type="email"
								id="email"
								class="shadow-sm rounded-md w-full px-3 py-2 border border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
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
								class="shadow-sm rounded-md w-full px-3 py-2 border border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
								placeholder="Enter your password"
								required
							/>
							<a
								href="#"
								class="text-xs text-gray-600 hover:text-indigo-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
								>Forgot Password?</a
							>
						</div>
						<div class="flex items-center justify-between mb-4">
							<div class="flex items-center">
								<input
									type="checkbox"
									id="remember"
									class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500 focus:outline-none"
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
							onclick="alert('hello')"
							type="submit"
							class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-rose-600 hover:bg-rose-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-rose-500"
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
							style="background-color: #55acee"
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
									viewBox="0 0 512 512"
								>
									<!--!Font Awesome Free 6.5.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc. -->
									<path
										d="M389.2 48h70.6L305.6 224.2 487 464H345L233.7 318.6 106.5 464H35.8L200.7 275.5 26.8 48H172.4L272.9 180.9 389.2 48zM364.4 421.8h39.1L151.1 88h-42L364.4 421.8z"
									/>
								</svg>
							</span>
							Continue with Google
						</a>
					</form>
				</div>
			</div>
		</div>
	</section>
</template>
