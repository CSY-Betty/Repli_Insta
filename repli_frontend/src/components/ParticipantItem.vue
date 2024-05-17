<script>
export default {
	props: {
		participant: Object,
	},
};
</script>

<template>
	<div class="border-b">
		<div class="px-10 py-4 w-fit flex items-center bg-white text-black">
			<div class="flex items-center">
				<img
					:src="participant.get_avatar"
					class="w-16 aspect-square rounded-full"
				/>
				<p class="ml-6 text-xl">{{ participant.name }}</p>
			</div>
		</div>
	</div>
</template>
