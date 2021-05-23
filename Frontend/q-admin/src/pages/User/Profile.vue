<template>
  <q-page>
    <base-breadcumps current-page-label="Профиль"/>
    <section class="q-mt-lg">
      <div class="row column justify-center">
        <!--        Avatar-->
        <div class="q-mx-auto">
          <q-avatar size="150px">
            <q-img v-if="seller.avatar" :src="seller.avatar">
              <template v-slot:loading>
                <q-skeleton class="fit"/>
              </template>
            </q-img>
            <q-icon v-else name="person" color="grey-7" />
          </q-avatar>
        </div>
      </div>
      <profile-info-tabs class="q-mt-xl"/>
    </section>
  </q-page>
</template>

<script>
import BaseBreadcumps from 'components/base-breadcumps'
import ProfileInfoTabs from 'components/profile/profile-info-tabs'
import { mapState } from 'vuex'
import currencyKZTFormatter from 'src/filters/currency-kzt'

export default {
  name: 'Profile',
  components: {
    ProfileInfoTabs,
    BaseBreadcumps
  },
  filters: { currencyKZTFormatter },
  computed: {
    ...mapState('user', ['seller'])
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
