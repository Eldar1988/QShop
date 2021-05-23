<template>
  <div id="q-app">
    <router-view />
  </div>
</template>
<script>
import configs from 'src/configs'
import firebase from 'firebase'
import { mapActions } from 'vuex'

export default {
  name: 'App',
  created () {
    configs.localStorageConfig()
    const uid = localStorage.getItem('uid')
    firebase.initializeApp(configs.firebaseConfig)
    if (localStorage.getItem('darkThemeIsActive') === 'true') {
      this.$q.dark.set(true)
    }
    if (!uid) {
      this.$router.replace({
        path: '/login'
      })
    } else {
      this.loadSeller(uid)
    }
  },
  methods: {
    ...mapActions('user', ['loadSeller'])
  }
}
</script>
