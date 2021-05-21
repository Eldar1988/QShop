<template>
  <div id="q-app">
    <router-view />
  </div>
</template>
<script>
import configs from 'src/configs'
import firebase from 'firebase'

export default {
  name: 'App',
  created () {
    firebase.initializeApp(configs.firebaseConfig)
    if (localStorage.getItem('darkThemeIsActive') === 'true') {
      this.$q.dark.set(true)
    }
    if (!localStorage.getItem('uid')) {
      this.$router.replace({
        path: '/login'
      })
    }
  },
  beforeCreate () {
    configs.localStorageConfig()
  }
}
</script>
