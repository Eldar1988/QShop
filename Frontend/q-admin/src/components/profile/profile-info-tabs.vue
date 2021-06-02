<template>
  <div class="profile-info-tabs">
    <q-tabs
      v-model="tab"
      dense no-caps
      class="text-grey"
      active-color="white"
      indicator-color="transparent"
      align="justify"
      active-bg-color="accent"
      style="height: 50px"
    >
      <q-tab name="info" label="Информация" class="rounded-borders f-w-700"/>
      <q-tab name="balance" label="Баланс" class="rounded-borders"/>
      <q-tab name="notifications" label="Уведомления" class="rounded-borders" />
    </q-tabs>
    <q-tab-panels
      v-model="tab"
      animated swipeable
      transition-prev="scale"
      transition-next="scale"
      class="q-mt-md rounded-borders q-card--bordered"
    >
      <q-tab-panel name="info">
        <profile-info-tab-panel/>
      </q-tab-panel>

      <q-tab-panel name="balance">
        <profile-balance-tab-panel/>
      </q-tab-panel>

      <q-tab-panel name="notifications">
        <profile-notifications-tab-panel />
      </q-tab-panel>
    </q-tab-panels>
  </div>
</template>

<script>
import ProfileInfoTabPanel from 'components/profile/profile-info-tab-panel'
import ProfileBalanceTabPanel from 'components/profile/profile-balance-tab-panel'
import ProfileNotificationsTabPanel from 'components/profile/profile-notifications-tab-panel'

export default {
  name: 'profile-info-tabs',
  components: {
    ProfileNotificationsTabPanel,
    ProfileBalanceTabPanel,
    ProfileInfoTabPanel
  },
  data () {
    return {
      tab: this.$route.params.tab
    }
  }
}
</script>

<style scoped>

</style>
