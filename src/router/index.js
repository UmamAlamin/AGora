import { createRouter, createWebHistory } from 'vue-router';
import Login from '../components/icons/Login.vue';
import Home from '../views/home.vue';
import Signup from '../components/icons/signup.vue';
import Detail from '../components/icons/detail.vue';  // Import the Detail component

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/event/:id',  // Route with dynamic parameter for event ID
    name: 'EventDetail',
    component: Detail,  // Map to the Detail component
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
