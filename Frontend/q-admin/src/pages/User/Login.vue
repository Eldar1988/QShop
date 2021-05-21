<template>
  <q-page class="flex-center flex">
    <login-form/>
  </q-page>
</template>

<script>
import LoginForm from 'components/user/login-form'

export default {
  name: 'Login',
  components: { LoginForm }
}
</script>

<style scoped>

</style>
