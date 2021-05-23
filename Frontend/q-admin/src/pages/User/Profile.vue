<template>
  <q-page>
    <base-breadcumps current-page-label="Профиль"/>
    <section class="q-mt-lg">
      <div class="row column justify-center">
        <!--        Avatar-->
        <div class="q-mx-auto">
          <q-avatar size="150px">
            <q-img src="https://cdn.quasar.dev/img/avatar4.jpg">
              <template v-slot:loading>
                <q-skeleton class="fit"/>
              </template>
            </q-img>
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

export default {
  name: 'Profile',
  components: {
    ProfileInfoTabs,
    BaseBreadcumps
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
