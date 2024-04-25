<script>
import { RouterLink } from 'vue-router';

export default {
	props: {
		comment: Object,
	},

	components: { RouterLink },
};
</script>

<template>
	<div class="flex items-center justify-between">
		<div class="flex items-center">
			<img
				class="rounded-full w-[38px] h-[38px]"
				src="https://picsum.photos/id/54/800/820"
			/>
			<div class="ml-4 font-extrabold text-[15px]">
				{{ comment.created_by.name }}
				<span class="font-light text-gray-700 text-sm">{{
					comment.created_at_formatted
				}}</span>
			</div>
		</div>
	</div>
	<div class="text-[13px] pl-[55px]">
		{{ comment.body }}
	</div>
</template>
