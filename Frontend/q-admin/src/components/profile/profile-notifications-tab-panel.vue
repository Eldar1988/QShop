<template>
  <div>
    <q-list separator>
      <q-item
        v-for="notification in notifications"
        :key="notification.id"
      >
        <q-item-section avatar top>
          <q-avatar icon="circle_notifications" />
        </q-item-section>
        <q-item-section>
          <q-item-label lines="1" class="text-bold">{{ notification.title }}</q-item-label>
          <q-item-label caption>{{ notification.text }}</q-item-label>
          <small class="q-pt-md">{{ notification.date|dateFormatter }}</small>
        </q-item-section>
      </q-item>
    </q-list>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import dateFormatter from 'src/filters/date-formatter'

export default {
  name: 'profile-notifications-tab-panel',
  filters: { dateFormatter },
  computed: {
    ...mapState('user', ['notifications'])
  },
  methods: {
    ...mapActions('user', ['loadSellerNotifications'])
  },
  created () {
    const vm = this
    vm.loadSellerNotifications()
  }
}
</script>
