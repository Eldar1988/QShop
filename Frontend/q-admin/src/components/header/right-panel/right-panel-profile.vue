<template>
  <div v-if="seller" class="profile">
    <q-btn round flat>
      <q-avatar size="26px">
        <img v-if="seller.avatar" :src="seller.avatar" style="object-fit: cover" />
        <q-icon v-else name="person" color="grey-7"/>
      </q-avatar>
      <q-tooltip>Профиль</q-tooltip>
      <q-menu
        max-width="100%" style="min-width: 500px !important"
        content-style="width: 300px; max-width: 70%; margin: auto"
        fit
      >
        <div class="q-pa-sm">
          <div class="col-6">
            <div class="q-mt-md">
            </div>
          </div>
          <div class="column flex justify-center full-width text-center">
            <!--            Profile-->
            <q-avatar size="72px" class="q-mx-auto">
              <img v-if="seller.avatar" :src="seller.avatar" style="object-fit: cover">
              <q-icon v-else name="person" color="grey-7"/>
            </q-avatar>
            <div class="q-mt-md q-mb-xs text-center text-bold">{{ seller.name }}</div>
            <!--            List-->
            <q-list separator padding class="rounded-borders text-primary text-left q-mt-md">
              <q-separator/>
              <q-item
                clickable
                v-ripple
                to="/profile/info"
              >
                <q-item-section>Профиль</q-item-section>
              </q-item>
              <q-item
                clickable
                v-ripple
                to="/profile/balance"
              >
                <q-item-section>Баланс: <span class="text-bold">{{ seller.balance|currencyKZTFormatter }}</span>
                </q-item-section>
                <q-item-section>
                  <q-btn
                    label="Пополнить"
                    no-caps
                    size="sm"
                    unelevated
                    color="primary"
                  />
                </q-item-section>
              </q-item>
              <q-item
                clickable
                v-ripple
                to="/profile/notifications"
              >
                <q-item-section>Уведомления</q-item-section>
              </q-item>
            </q-list>
            <!--            Footer-->
            <div class="q-mt-md flex justify-between">
              <div class="">
                <base-theme-toggle label="Тема"/>
              </div>
              <q-btn
                outline
                label="Выход"
                no-caps
                unelevated
                size="sm"
                icon-right="logout"
                @click="logout"
                v-close-popup
              />
            </div>
          </div>
        </div>
      </q-menu>
    </q-btn>
  </div>

</template>

<script>
import BaseThemeToggle from 'components/base-theme-toggle'
import { mapActions, mapState } from 'vuex'
import currencyKZTFormatter from 'src/filters/currency-kzt'

export default {
  name: 'right-panel-profile',
  components: { BaseThemeToggle },
  filters: { currencyKZTFormatter },
  computed: {
    ...mapState('user', ['seller'])
  },
  methods: {
    ...mapActions('user', ['logout'])
  }
}
</script>

<style scoped>

</style>
