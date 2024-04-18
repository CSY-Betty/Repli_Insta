<script>
import PostsList from '@/components/PostsList.vue';

export default {
	name: 'ExploreView',
	components: {
		PostsList,
	},
};
</script>
<template>
	<div class="flex-col justify-center w-full mt-6 px-40 overflow-y-auto">
		<ul class="grid grid-cols-3 gap-1">
			<PostsList />
		</ul>
	</div>
</template>
