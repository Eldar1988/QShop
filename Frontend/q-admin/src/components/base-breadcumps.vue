<template>
<div class="base-bread-cumps">
  <q-breadcrumbs>
    <q-breadcrumbs>
      <q-breadcrumbs-el icon="home" to="/"/>
      <q-breadcrumbs-el
        v-for="(page, index) in pathPages"
        :key="index"
        :label="page.label"
        :to="page.path"
      />
      <q-breadcrumbs-el :label="currentPageLabel" />
    </q-breadcrumbs>
  </q-breadcrumbs>
</div>
</template>

<script>
export default {
  name: 'base-breadcumps',
  props: {
    currentPageLabel: {
      type: String,
      default: ''
    },
    pathPages: {
      type: Array,
      default: () => []
    }
  }
}
</script>

<style scoped>

</style>
