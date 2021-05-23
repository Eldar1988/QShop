<template>
  <q-card
    style="width: 550px; max-width: 100%"
    class="text-center shadow-1 q-py-md"
  >
    <q-card-section>
      <h2>Регистрация</h2>
      <p>Мы рады, что вы решили к нам присоединиться!</p>
    </q-card-section>
    <q-card-section class="q-px-lg">
<!--      Email input-->
      <q-input
        v-model="formData.email"
        label="Email"
        type="email"
        @keyup.enter.native="registerFormSubmit"
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
        @keyup.enter.native="registerFormSubmit"
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
<!--      Password submit input-->
      <q-input
        v-model="formData.passwordConfirm"
        label="Пароль еще раз"
        :type="!passwordVisible ? 'password' : 'text'"
        @keyup.enter.native="registerFormSubmit"
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
        label="Регистрация"
        color="primary"
        class="full-width q-py-sm q-mt-lg"
        :loading="loading"
        @click="registerFormSubmit"
      />
      <div class="q-mt-lg">
        <p class="text-subtitle1">Есть аккаунт? <router-link to="/login">Вход</router-link></p>
      </div>
    </q-card-section>
  </q-card>
</template>

<script>
import utils from 'src/utils'
import { mapActions, mapState } from 'vuex'

export default {
  name: 'register-form',
  computed: {
    ...mapState('user', ['seller'])
  },
  data () {
    return {
      passwordVisible: false,
      formData: {
        email: '',
        password: '',
        passwordConfirm: ''
      },
      loading: false
    }
  },
  methods: {
    ...mapActions('user', ['register']),
    async registerFormSubmit () {
      const vm = this
      vm.loading = true
      const valid = !utils.emptyDataValidator(Object.values(this.formData))
      if (valid) {
        const passwordsEquality = utils.equalityTest(vm.formData.password, vm.formData.passwordConfirm)
        if (passwordsEquality) {
          await vm.register(vm.formData)
          if (vm.seller.uid) {
            await vm.$router.push({
              path: '/'
            })
          }
        } else {
          utils.notifier('Пароли не совпадают. Пожалуйста, будьте внимательнее.')
        }
      } else {
        utils.notifier('Не все поля формы заполнены.')
      }
      vm.loading = false
    }
  }
}
</script>

<style scoped>

</style>
