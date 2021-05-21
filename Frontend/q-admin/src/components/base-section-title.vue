<template>
<div>
  <h2>{{ title }}</h2>
</div>
</template>

<script>
export default {
  name: 'base-section-title',
  props: {
    title: {
      type: String,
      default: ''
    },
    subtitle: {
      type: String,
      default: ''
    }
  }
}
</script>

<style scoped>

</style>
