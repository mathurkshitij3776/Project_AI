import {createWebHistory, createRouter} from 'vue-router';
import Generatestrategy from './components/Generatestrategy.vue';

const routes = [
    {path:'/', component : Generatestrategy }
    
]


export const router = createRouter({
    history: createWebHistory(),
    routes
})

