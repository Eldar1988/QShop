<template>
  <q-card
    style="width: 500px; max-width: 100%"
  >
    <q-toolbar class="bg-grey-7 text-white">
      <q-toolbar-title class="text-bold">Изменение профиля</q-toolbar-title>
      <q-btn v-close-popup dense flat icon="close"/>
    </q-toolbar>
    <q-card-section class="q-pa-lg">
      <q-input
        v-model="seller.name"
        label="Имя"
        autofocus
      />
      <q-input
        v-model="seller.phone"
        label="Телефон"
        prefix="+7"
        type="tel"
        mask="### ### ####"/>
      <div class="q-mt-xl text-right">
        <q-btn
          label="Отмена"
          unelevated no-caps
          color="grey-7"
          v-close-popup
        />
        <q-btn
          label="Изменить"
          color="primary"
          class="text-bold q-ml-md"
          icon-right="edit"
          unelevated no-caps
          :loading="loading"
          @click="updateSellerData"
          v-close-popup
        />
      </div>
    </q-card-section>
  </q-card>
</template>

<script>
import { mapActions, mapState } from 'vuex'

export default {
  name: 'change-profile-form',
  computed: {
    ...mapState('user', ['seller'])
  },
  data () {
    return {
      loading: false
    }
  },
  methods: {
    ...mapActions('user', ['updateSeller']),
    async updateSellerData () {
      const vm = this
      vm.loading = true
      await vm.updateSeller({ name: vm.seller.name, phone: vm.seller.phone, uid: vm.seller.uid })
      vm.loading = false
    }
  }
}
</script>

<style scoped>

</style>
