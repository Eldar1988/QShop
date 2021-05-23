<template>
  <div class="q-gutter-sm row items-center no-wrap">
    <base-theme-toggle />
    <right-panel-profile />
  </div>
</template>

<script>
import RightPanelProfile from 'components/header/right-panel/right-panel-profile'
import BaseThemeToggle from 'components/base-theme-toggle'
export default {
  name: 'right-panel',
  components: { BaseThemeToggle, RightPanelProfile }
}
</script>

<style scoped>

</style>
