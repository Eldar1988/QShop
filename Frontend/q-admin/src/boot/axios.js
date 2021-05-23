import Vue from 'vue'
import axios from 'axios'

const axiosConfig = {
  baseURL: 'http://192.168.0.199:8000',
  timeout: 30000
}

Vue.prototype.$axios = axios.create(axiosConfig)
