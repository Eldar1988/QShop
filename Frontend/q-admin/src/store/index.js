import Vue from 'vue'
import Vuex from 'vuex'
import user from './modules/user'
import shops from './modules/shops'

Vue.use(Vuex)

export default function (/* { ssrContext } */) {
  const Store = new Vuex.Store({
    state: {
      serverURL: 'http://192.168.0.199:8000'
      // serverURL: 'http://192.168.0.155:8000'
    },
    modules: {
      user,
      shops
    }
  })

  return Store
}
