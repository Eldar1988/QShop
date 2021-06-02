<template>
<div class="add-shop-card">
  <q-card
    class="flex flex-center cursor-pointer"
    style="height: 180px"
    @click="mutationAddShopDialog(true)"
  >
    <div class="text-center">
      <h3>Создать магазин</h3>
      <q-icon name="add_business" size="38px" color="primary"/>
    </div>
  </q-card>
</div>
</template>

<script>
import { mapMutations } from 'vuex'

export default {
  name: 'add-shop-card',
  data () {
    return {
      addShopDialog: true
    }
  },
  methods: {
    ...mapMutations('shops', ['mutationAddShopDialog'])
  }
}
</script>
