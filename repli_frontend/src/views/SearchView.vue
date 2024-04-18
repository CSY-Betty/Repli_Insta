<template>
	<div class="w-screen mt-6 flex flex-col">
		<div class="pb-2">
			<form class="max-w-md mx-auto">
				<label
					for="default-search"
					class="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white"
					>Search</label
				>
				<div class="relative">
					<div
						class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none"
					>
						<svg
							class="w-4 h-4 text-gray-500 dark:text-gray-400"
							aria-hidden="true"
							xmlns="http://www.w3.org/2000/svg"
							fill="none"
							viewBox="0 0 20 20"
						>
							<path
								stroke="currentColor"
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"
							/>
						</svg>
					</div>
					<input
						type="search"
						id="default-search"
						class="block w-full p-4 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-rose-500 focus:border-rose-500 outline-none"
						placeholder="Search"
						required
					/>
					<button
						type="submit"
						class="text-white absolute end-2.5 bottom-2.5 bg-rose-700 hover:bg-rose-800 focus:ring-4 focus:outline-none focus:ring-rose-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-rose-600 dark:hover:bg-rose-700 dark:focus:ring-rose-800"
					>
						Search
					</button>
				</div>
			</form>
		</div>
		<div
			class="container mx-auto overflow-y-auto flex flex-col items-center"
		>
			<button
				class="max-w-md px-10 py-2 w-full flex items-center cursor-pointer hover:bg-gray-50 bg-white text-black"
			>
				<img
					src="https://i.pravatar.cc/150?img=29"
					class="w-16 aspect-square rounded-full"
				/>
				<p class="ml-2 text-xl">Sara jen</p>
			</button>
			<button
				class="max-w-md px-10 py-2 w-full flex items-center cursor-pointer hover:bg-gray-50 bg-white text-black"
			>
				<img
					src="https://i.pravatar.cc/150?img=30"
					class="w-16 aspect-square rounded-full"
				/>
				<p class="ml-2 text-xl">Sara Vanila</p>
			</button>
		</div>
	</div>
</template>
