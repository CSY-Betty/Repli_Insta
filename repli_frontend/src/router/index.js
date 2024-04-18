import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import ExploreView from '../views/ExploreView.vue';
import SignupView from '../views/SignupView.vue';
import SigninView from '../views/SigninView.vue';
import ProfileView from '../views/ProfileView.vue';
import MessagesView from '../views/MessagesView.vue';

const router = createRouter({
	history: createWebHistory(import.meta.env.BASE_URL),
	routes: [
		{
			path: '/',
			name: 'home',
			component: HomeView,
		},
		{
			path: '/about',
			name: 'about',
			// route level code-splitting
			// this generates a separate chunk (About.[hash].js) for this route
			// which is lazy-loaded when the route is visited.
			component: () => import('../views/AboutView.vue'),
		},
		{
			path: '/explore',
			name: 'explore',
			component: ExploreView,
		},
		{
			path: '/messages',
			name: 'messages',
			component: MessagesView,
		},
		{
			path: '/profile',
			name: 'profile',
			component: ProfileView,
		},
		{
			path: '/signup',
			name: 'signup',
			component: SignupView,
		},
		{
			path: '/signin',
			name: 'signin',
			component: SigninView,
		},
	],
});

export default router;
