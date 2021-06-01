<template>
  <div>
    <div class="row q-col-gutter-lg">
<!--      Balance-->
      <div class="col-md-6 col-12">
        <div class="text-subtitle1">
          Ваш баланс:
          <span class="text-bold" :class="balanceClass">{{ seller.balance|currencyKZTFormatter }}</span>
        </div>
        <div class="q-mt-sm text-subtitle1">
          Текущий тариф:
          <span class="text-bold">{{ seller.tariff|currencyKZTFormatter }}/день</span>
        </div>
        <div class="text-grey-7 q-mt-md">
          Тариф напрямую зависит от количества магазинов. Оплата за каждый магазин 130 тенге/день
          <div class="q-mt-sm text-warning">Дней до истечения баланса: {{ balanceDaysLeft }}</div>
        </div>
      </div>
<!--      Payment-->
      <div class="col-md-6 col-12 flex flex-center">
        <q-btn
          label="Пополнить баланс"
          color="primary"
          class="q-pa-sm"
          icon-right="account_balance_wallet"
          unelevated
        />
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import currencyKZTFormatter from 'src/filters/currency-kzt'

export default {
  name: 'profile-balance-tab-panel',
  filters: { currencyKZTFormatter },
  computed: {
    ...mapState('user', ['seller']),
    balanceClass () {
      if (this.seller.balance < 2000) return 'text-negative'
      return 'text-primary'
    },
    balanceDaysLeft () {
      return Math.floor(this.seller.balance / this.seller.tariff)
    }
  }
}
</script>

<style scoped>

</style>
