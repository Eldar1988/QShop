<template>
  <q-scroll-area class="fit">
    <q-list padding>
      <q-item
        v-for="link in mainLinks"
        :key="link.text"
        :to="link.path"
        v-ripple clickable
      >
        <q-item-section avatar>
          <q-icon :name="link.icon"/>
        </q-item-section>
        <q-item-section>
          <q-item-label>{{ link.text }}</q-item-label>
        </q-item-section>
      </q-item>
      <q-separator class="q-my-md"/>
    </q-list>
  </q-scroll-area>
</template>

<script>
export default {
  name: 'base-drawer-content',
  data () {
    return {
      mainLinks: [
        {
          icon: 'home',
          text: 'Главная',
          path: '/'
        }
      ]
    }
  }
}
</script>

<style scoped>

</style>
