<template>
  <div class="profile-info-tabs">
    <q-card
      class="shadow-0"
      bordered
    >
      <q-tabs
        v-model="tab"
        dense no-caps
        class="text-grey"
        active-color="white"
        indicator-color="transparent"
        align="justify"
        active-bg-color="grey-7"
        style="height: 50px"
      >
        <q-tab name="info" label="Информация"/>
        <q-tab name="balance" label="Баланс" />
        <q-tab name="story" label="История" />
      </q-tabs>

      <q-separator />

      <q-tab-panels v-model="tab" animated>
        <q-tab-panel name="info">
          <profile-info-tab-panel />
        </q-tab-panel>

        <q-tab-panel name="balance">
          <profile-balance-tab-panel />
        </q-tab-panel>

        <q-tab-panel name="story">
          <profile-story-tab-panel />
        </q-tab-panel>
      </q-tab-panels>
    </q-card>
  </div>
</template>

<script>
import ProfileInfoTabPanel from 'components/profile/profile-info-tab-panel'
import ProfileBalanceTabPanel from 'components/profile/profile-balance-tab-panel'
import ProfileStoryTabPanel from 'components/profile/profile-story-tab-panel'
export default {
  name: 'profile-info-tabs',
  components: { ProfileStoryTabPanel, ProfileBalanceTabPanel, ProfileInfoTabPanel },
  data () {
    return {
      tab: this.$route.params.tab
    }
  }
}
</script>

<style scoped>

</style>
