<template>
  <q-toggle
    v-model="dark"
    :icon="dark ? 'dark_mode': 'light_mode'"
    color="grey-8"
    @input="darkToggle"
    :label="label"
  />
</template>

<script>
export default {
  name: 'base-theme-toggle',
  props: {
    label: {
      type: String,
      default: ''
    }
  },
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
