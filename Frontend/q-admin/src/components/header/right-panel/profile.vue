<template>
  <div class="profile">
    <q-btn round flat>
      <q-avatar size="26px">
        <img src="https://cdn.quasar.dev/img/boy-avatar.png">
      </q-avatar>
      <q-tooltip>Профиль</q-tooltip>
      <q-menu max-width="100%" style="min-width: 500px !important"
              content-style="width: 300px; max-width: 70%; margin: auto" fit>
        <div class="q-pa-sm">
          <div class="col-6">
            <div class="q-mt-md">
            </div>
          </div>
          <div class="column flex justify-center full-width text-center">
            <!--            Profile-->
            <q-avatar size="72px" class="q-mx-auto">
              <img src="https://cdn.quasar.dev/img/avatar4.jpg">
            </q-avatar>
            <div class="q-mt-md q-mb-xs text-center text-bold">Эльдар Хайбулов</div>
            <!--            List-->
            <q-list separator padding class="rounded-borders text-primary text-left q-mt-md">
              <q-separator />
              <q-item
                clickable
                v-ripple
                to="/profile"
              >
                <q-item-section>Профиль</q-item-section>
              </q-item>
              <q-item
                clickable
                v-ripple
              >
                <q-item-section>Баланс</q-item-section>
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

export default {
  name: 'profile',
  components: { BaseThemeToggle }
}
</script>

<style scoped>

</style>
