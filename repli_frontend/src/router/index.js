import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import ExploreView from '../views/ExploreView.vue';
import SignupView from '../views/SignupView.vue';
import SigninView from '../views/SigninView.vue';
import ProfileView from '../views/ProfileView.vue';
import MessagesView from '../views/MessagesView.vue';
import SearchView from '../views/SearchView.vue';
import FriendsView from '../views/FriendsView.vue';
import PostView from '../views/PostView.vue';
import EditProfileView from '../views/EditProfileView.vue';
import EditPasswordView from '../views/EditPasswordView.vue';

import ChatView from '../views/ChatView.vue';
import Chat from '@/components/Chat.vue';

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
			path: '/chat-room',
			name: 'chat-room',
			component: ChatView,
		},
		{
			path: '/chat-room/:id',
			name: 'Chat',
			component: Chat,
		},
		// {
		// 	path: '/messages',
		// 	name: 'messages',
		// 	component: MessagesView,
		// },
		// {
		// 	path: '/messages/:id',
		// 	name: 'message',
		// 	component: Message,
		// },
		{
			path: '/profile/edit',
			name: 'editprofile',
			component: EditProfileView,
		},
		{
			path: '/profile/edit/password',
			name: 'editpassword',
			component: EditPasswordView,
		},
		{
			path: '/profile/:id',
			name: 'profile',
			component: ProfileView,
		},

		{
			path: '/profile/:id/friends',
			name: 'friends',
			component: FriendsView,
		},
		{
			path: '/search',
			name: 'search',
			component: SearchView,
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
		{
			path: '/p/:id',
			name: 'post',
			component: PostView,
		},
	],
});

export default router;
