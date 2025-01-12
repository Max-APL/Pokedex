import { createRouter, createWebHistory } from 'vue-router';
import App from '@/App.vue'; // Asegúrate de que la ruta es correcta

const routes = [
  {
    path: '/',
    name: 'Home',
    component: App,
  },
  // Puedes agregar más rutas aquí si decides tener más componentes en el futuro
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
