import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import ical from 'node-ical'

const app = createApp(App).use(VueAxios, axios, ical)
app.provide('axios', app.config.globalProperties.axios)
app.mount('#app')
