<template>
  <q-card
    style="width: 550px; max-width: 100%"
    class="text-center shadow-1 q-py-md"
  >
    <q-card-section>
      <h2>Вход</h2>
    </q-card-section>
    <q-card-section class="q-px-lg">
<!--      Email input-->
      <q-input
        v-model="formData.email"
        label="Email"
        type="email"
        @keyup.enter.native="loginFormSubmit"
      >
        <template v-slot:prepend>
          <q-icon name="alternate_email" />
        </template>
      </q-input>
<!--      Password input-->
      <q-input
        v-model="formData.password"
        label="Пароль"
        :type="!passwordVisible ? 'password' : 'text'"
        @keyup.enter.native="loginFormSubmit"
      >
        <template v-slot:prepend>
          <q-icon name="vpn_key" />
        </template>
        <template v-slot:append>
          <q-icon
            :name="passwordVisible ?  'visibility_off' : 'visibility'"
            color="grey-5"
            @click.passive="passwordVisible = !passwordVisible"/>
        </template>
      </q-input>
<!--      Submit button-->
      <q-btn
        unelevated
        label="Вход"
        color="primary"
        class="full-width q-py-sm q-mt-lg"
        :loading="loading"
        @click="loginFormSubmit"
      />
      <div class="q-mt-lg">
        <p class="text-subtitle1">Нет аккаунта? <router-link to="/register">Регистрация</router-link></p>
      </div>
    </q-card-section>
  </q-card>
</template>

<script>
import utils from 'src/utils'
import { mapActions, mapState } from 'vuex'

export default {
  name: 'login-form',
  computed: {
    ...mapState('user', ['seller'])
  },
  data () {
    return {
      passwordVisible: false,
      formData: {
        email: '',
        password: ''
      },
      loading: false
    }
  },
  methods: {
    ...mapActions('user', ['login']),
    async loginFormSubmit () {
      this.loading = true
      const valid = !utils.emptyDataValidator(Object.values(this.formData))
      if (valid) {
        await this.login(this.formData)
        if (this.seller) {
          await this.$router.replace({
            path: '/'
          })
        }
      } else {
        utils.notifier('Не все поля формы заполнены.')
      }
      this.loading = false
    }
  }
}
</script>

<style scoped>

</style>
