import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import ical from 'node-ical'
//import fs from "fs"
/*
import keys from "../keys.json"
console.log("res")

setInterval(() => {
    axios.get(keys.calendarLocation).then((res) => {
        console.log(res)
    })
}, 5500)
*/
const app = createApp(App).use(VueAxios, axios, ical)
app.provide('axios', app.config.globalProperties.axios)
app.mount('#app')
