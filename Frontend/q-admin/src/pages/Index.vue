<template>
  <q-page class="">
    <base-section-title title="Ваши магазины" />
    <shop-cards />
    <add-shop-dialog />
  </q-page>
</template>

<script>
import BaseSectionTitle from 'components/base-section-title'
import ShopCards from 'components/shop/shop-cards/shop-cards'
import AddShopDialog from 'components/shop/dialogs/add-shop-dialog'
export default {
  name: 'PageIndex',
  components: { AddShopDialog, ShopCards, BaseSectionTitle }
}
</script>
