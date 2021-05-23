<template>
  <div class="q-gutter-sm row items-center no-wrap">
    <base-theme-toggle />
    <q-btn round dense flat color="grey-8" icon="notifications">
      <q-badge color="red" text-color="white" floating>
      </q-badge>
      <q-tooltip>Уведомления</q-tooltip>
    </q-btn>
    <profile />
  </div>
</template>

<script>
import Profile from 'components/header/right-panel/profile'
import BaseThemeToggle from 'components/base-theme-toggle'
export default {
  name: 'right-panel',
  components: { BaseThemeToggle, Profile }
}
</script>

<style scoped>

</style>
