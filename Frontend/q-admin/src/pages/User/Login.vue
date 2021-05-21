<template>
<q-page class="flex-center flex">
  <q-card
    style="width: 550px; max-width: 100%"
    class="text-center shadow-1 q-py-md"
  >
    <q-card-section>
      <h2>Вход</h2>
    </q-card-section>
    <q-card-section class="q-px-lg">
      <q-input
        v-model="formData.email"
        label="Email"
        type="email">
        <template v-slot:prepend>
          <q-icon name="alternate_email" />
        </template>
      </q-input>
      <q-input
        v-model="formData.password"
        label="Пароль"
        :type="!passwordVisible ? 'password' : 'text'">
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
      <q-btn
        label="Вход"
        color="primary"
        class="full-width q-py-sm q-mt-lg"
      />

      <div class="q-mt-lg">
        <p class="text-subtitle1">Нет аккаунта? <router-link to="/register">Регистрация</router-link></p>
      </div>
    </q-card-section>
    <q-card-section class="q-px-lg">

    </q-card-section>
  </q-card>
</q-page>
</template>

<script>
export default {
  name: 'Login',
  data () {
    return {
      passwordVisible: false,
      formData: {
        email: '',
        password: ''
      }
    }
  }
}
</script>

<style scoped>

</style>
