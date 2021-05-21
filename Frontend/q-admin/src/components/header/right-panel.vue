<template>
  <div class="q-gutter-sm row items-center no-wrap">

    <q-toggle
      v-model="dark"
      :icon="dark ? 'dark_mode': 'light_mode'"
      color="grey-8"
      @input="darkToggle"
    />
    <q-btn round dense flat color="grey-8" icon="notifications">
      <q-badge color="red" text-color="white" floating>
      </q-badge>
      <q-tooltip>Уведомления</q-tooltip>
    </q-btn>
    <q-btn round flat>
      <q-avatar size="26px">
        <img src="https://cdn.quasar.dev/img/boy-avatar.png">
      </q-avatar>
      <q-tooltip>Account</q-tooltip>
    </q-btn>
  </div>
</template>

<script>
export default {
  name: 'right-panel',
  data () {
    return {
      dark: this.$q.dark.mode
    }
  },
  methods: {
    darkToggle () {
      this.$q.dark.toggle()
      localStorage.setItem('darkThemeIsActive', this.$q.dark.mode.toString())
    }
  }
}
</script>

<style scoped>

</style>
