import Vue from 'vue'
import Router from 'vue-router'
import Login from './views/Login'
import Dashboard from './views/Dashboard'
import Menu from './views/Menu'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      redirect: '/login'
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: Dashboard
    },
    {
      path: '/menu',
      name: 'menu',
      component: Menu
    }
  ]
})
