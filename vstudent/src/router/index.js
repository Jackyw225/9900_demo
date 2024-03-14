import { createRouter, createWebHistory } from 'vue-router'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: '/',
      component: () => import('../views/index.vue'),
      children:[
        
        {
          path: '',
          name: '',
      
          component: () => import('../views/dashboard.vue')
        },
        {
          path: 'home/:id',
          name: 'home',
          component: () => import('../views/home.vue')
        },
        {
          path: 'user',
          name: 'user',
          component: () => import('../views/user.vue')
        },
        {
          path: '/course',
          name: 'course',
        
          component: () => import('../views/course management.vue')
        },
        {
          path: '/createcourse/:id',
          name: 'createcourse',
        
          component: () => import('../views/create course.vue')
        },
        {
          path: '/student',
          name: 'student',
        
          component: () => import('../views/student management.vue')
        },
        {
          path: '/student/:id',
          name: 'student',
        
          component: () => import('../views/student management.vue')
        },
      ]
    },
    {
      path: '/login',
      name: 'login',
  
      component: () => import('../views/login.vue')
    },
    {
      path: '/forgot',
      name: 'forgot',
  
      component: () => import('../views/forgot.vue')
    },
    {
      path: '/register',
      name: 'register',
  
      component: () => import('../views/register.vue')
    },
   
   
    
  ]
   
 
})

export default router
