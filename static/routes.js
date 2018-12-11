import Importador from './pages/importador';

const baseName = '/';

const routes = () => [
  {
    iconClass: 'fa fa-dashboard',
    title: 'Ipsum',
    to: '/',
    component: Importador,
  },
  {
    iconClass: 'fa fa-star',
    title: 'Dolor',
    to: '/dolor',
    component: Usuarios
  }
];

export { baseName, routes };