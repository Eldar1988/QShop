<template>
<div class="shop-cards">
  <div class="row q-col-gutter-md q-mt-sm">
    <add-shop-card class="col-12 col-sm-6 col-md-3"/>
  </div>
</div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import AddShopCard from 'components/shop/shop-cards/add-shop-card'

export default {
  name: 'shop-cards',
  components: { AddShopCard },
  computed: {
    ...mapState('shops', ['shops'])
  },
  methods: {
    ...mapActions('shops', ['loadShops'])
  },
  created () {
    const vm = this
    vm.loadShops({ uid: localStorage.getItem('uid') })
  }
}
</script>

<style lang="sass">

</style>
