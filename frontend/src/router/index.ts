import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LivreView from '../views/LivreView.vue'
// import UserView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/livres',
      name: 'livres',
      component: LivreView
    },
    {
      path: '/utilisateurs',
      name: 'users',
      component: HomeView
    }
  ]
})

export default router