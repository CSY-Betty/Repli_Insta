<script>
import axios from 'axios';
import { useUserStore } from '@/stores/user';
import { RouterLink } from 'vue-router';
import ChatView from '@/views/ChatView.vue';

export default {
	components: { ChatView },
};
</script>

<template>
	<ChatView />
	<section class="pt-6 h-screen w-full">
		<div class="grid grid-rows-10 h-full">
			<div class="border-b">
				<div class="px-10 w-fit flex items-center bg-white text-black">
					<div class="flex items-center">
						<img
							src="https://i.pravatar.cc/150?img=45"
							class="w-16 aspect-square rounded-full"
						/>

						<p class="ml-6 text-xl">lalalalalala</p>
					</div>
				</div>
			</div>

			<div class="mt-2 row-span-8 overflow-y-auto">
				<template class="grid gap-2">
					<div class="flex items-end gap-2.5 px-4 py-2 justify-end">
						<div
							class="flex flex-col w-full max-w-[320px] leading-1.5 p-4 border-gray-200 bg-gray-100 rounded-s-xl rounded-se-xl dark:bg-gray-700"
						>
							<p
								class="text-sm font-normal py-2.5 text-gray-900 dark:text-white"
							>
								afkljalkdjflk
							</p>
						</div>
						<img
							class="w-8 h-8 rounded-full"
							src="https://i.pravatar.cc/150?img=45"
							alt="Jese image"
						/>
					</div>
					<div class="flex items-end gap-2.5 pl-4 py-2">
						<img
							class="w-8 h-8 rounded-full"
							src="https://i.pravatar.cc/150?img=45"
							alt="Jese image"
						/>
						<div
							class="flex flex-col w-full max-w-[320px] leading-1.5 p-4 border-gray-200 bg-gray-100 rounded-ss-xl rounded-e-xl dark:bg-gray-700"
						>
							<p
								class="text-sm font-normal py-2.5 text-gray-900 dark:text-white"
							>
								alalalalal
							</p>
						</div>
					</div>
				</template>
			</div>
			<div class="border-t pt-2">
				<form class="px-10">
					<div
						class="flex items-center border border-gray-300 py-2 px-2 rounded-full"
					>
						<textarea
							class="appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none"
							type="text"
							placeholder="Message..."
						></textarea>
						<button
							class="flex-shrink-0 bg-rose-400 hover:bg-rose-500 border-rose-400 hover:border-rose-500 text-sm border-4 text-white py-1 px-2 rounded-full"
							type="submit"
						>
							Send
						</button>
					</div>
				</form>
			</div>
		</div>
	</section>
</template>
