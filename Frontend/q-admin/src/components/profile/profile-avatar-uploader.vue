<template>
  <q-uploader
    style="max-width: 300px"
    :url="`${this.$store.state.serverURL}/seller/update_seller_avatar/${seller.uid}/`"
    label="Загрузите фото"
    method="PATCH"
    field-name="avatar"
    accept=".jpg, image/*"
    @uploaded="rejected"
  />
</template>

<script>
import { mapActions, mapState } from 'vuex'
import notifier from 'src/utils/notifier'

export default {
  name: 'profile-avatar-uploader',
  computed: {
    ...mapState('user', ['seller'])
  },
  methods: {
    ...mapActions('user', ['loadSeller']),
    async rejected () {
      const vm = this
      await vm.loadSeller(vm.seller.uid)
      notifier('Фото загружено')
    }
  }
}
</script>

<style scoped>

</style>
