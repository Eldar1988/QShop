<template>
  <q-page>
    <base-breadcumps current-page-label="Профиль"/>
    <section class="q-mt-lg">
      <div class="row column justify-center">
        <!--        Avatar-->
        <div class="q-mx-auto">
          <q-avatar size="150px">
            <img v-if="seller.avatar" :src="seller.avatar" style="object-fit: cover">
            <q-icon v-else name="person" color="grey-7"/>
          </q-avatar>
        </div>
      </div>
      <div class="text-center">
      <q-btn
        label="Изменить"
        no-caps dense size="sm" flat
        icon="edit"
        color="grey-7"
        @click="avatarUploaderDialog = true"
        class="q-mx-auto q-mt-sm"/>
      </div>
      <profile-info-tabs class="q-mt-xl"/>
    </section>
    <q-dialog v-model="avatarUploaderDialog">
      <profile-avatar-uploader />
    </q-dialog>
  </q-page>
</template>

<script>
import BaseBreadcumps from 'components/base-breadcumps'
import ProfileInfoTabs from 'components/profile/profile-info-tabs'
import { mapState } from 'vuex'
import currencyKZTFormatter from 'src/filters/currency-kzt'
import ProfileAvatarUploader from 'components/profile/profile-avatar-uploader'

export default {
  name: 'Profile',
  components: {
    ProfileAvatarUploader,
    ProfileInfoTabs,
    BaseBreadcumps
  },
  filters: { currencyKZTFormatter },
  computed: {
    ...mapState('user', ['seller'])
  },
  data () {
    return {
      avatarUploaderDialog: false
    }
  },
  beforeCreate () {
    if (!localStorage.getItem('uid')) {
      this.$router.replace('/login')
    }
  }
}
</script>

<style scoped>

</style>
