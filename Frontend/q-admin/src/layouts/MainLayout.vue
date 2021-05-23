<template>
  <q-layout view="hHh lpR fFf" class="">
    <q-header class="q-py-xs bg-transparent text-grey-8 shadow-3" height-hint="58">
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          @click="leftDrawerOpen = !leftDrawerOpen"
          aria-label="Menu"
          icon="menu"
        />
        <q-toolbar-title class="f-w-900">
          <span class="text-primary">Q</span>Shop
        </q-toolbar-title>
        <q-space/>
        <right-panel/>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      :width="240"
    >
      <base-drawer-content/>
    </q-drawer>

    <q-page-container>
      <div class="page-container q-bg">
        <transition
          appear
          enter-active-class="animated fadeIn"
          leave-active-class="animated fadeOut"
        >
        <router-view/>
        </transition>
      </div>
    </q-page-container>
  </q-layout>
</template>

<script>

import RightPanel from 'components/header/right-panel/right-panel'
import BaseDrawerContent from 'components/base-drawer/base-drawer-content'

export default {
  name: 'MainLayout',
  components: {
    BaseDrawerContent,
    RightPanel
  },
  data () {
    return {
      leftDrawerOpen: false
    }
  },
  created () {
    this.fabYoutube = 'fabYoutube'
  }
}
</script>

<style lang="sass">
.YL
  &__toolbar-input-container
    min-width: 100px
    width: 55%

  &__toolbar-input-btn
    border-radius: 0
    border-style: solid
    border-width: 1px 1px 1px 0
    border-color: rgba(0, 0, 0, .24)
    max-width: 60px
    width: 100%

  &__drawer-footer-link
    color: inherit
    text-decoration: none
    font-weight: 500
    font-size: .75rem

    &:hover
      color: #000
</style>
