import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import GuestUser from '../views/GuestUser.vue';
import HostUser from '../views/HostUser.vue';
import Ping from '../components/Ping.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/GuestUser',
    name: 'Guest User Interface',
    component: GuestUser,
  },
  {
    path: '/HostUser',
    name: 'Host User Interface',
    component: HostUser,
  },
  {
    path: '/ping',
    name: 'Ping',
    component: Ping,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
