<template>
  <div>
    <q-list separator class="rounded-borders">
      <!--      Name-->
      <q-item>
        <q-item-section avatar top>
          <q-avatar icon="person" color="primary" text-color="white"/>
        </q-item-section>
        <q-item-section>
          <q-item-label lines="1">Имя</q-item-label>
          <q-item-label caption>
            {{ seller.name || 'Anonim' }}
          </q-item-label>
        </q-item-section>
        <q-item-section side>
          <q-btn
            icon="edit"
            dense unelevated
            size="sm"
            color="grey-7"
            @click="changeProfileDialog = true"
          >
            <q-tooltip>Изменить</q-tooltip>
          </q-btn>
        </q-item-section>
      </q-item>
      <!--      Phone-->
      <q-item>
        <q-item-section avatar top>
          <q-avatar icon="phone" color="primary" text-color="white"/>
        </q-item-section>
        <q-item-section>
          <q-item-label lines="1">Номер телефона</q-item-label>
          <q-item-label caption>+7 {{ seller.phone }}</q-item-label>
        </q-item-section>
        <q-item-section side>
          <q-btn
            icon="edit"
            dense unelevated
            size="sm"
            color="grey-7"
            @click="changeProfileDialog = true"
          >
            <q-tooltip>Изменить</q-tooltip>
          </q-btn>
        </q-item-section>
      </q-item>
      <!--      Email-->
      <q-item>
        <q-item-section avatar top>
          <q-avatar icon="email" color="primary" text-color="white"/>
        </q-item-section>
        <q-item-section>
          <q-item-label lines="1">E-mail</q-item-label>
          <q-item-label caption>{{ seller.email }}</q-item-label>
        </q-item-section>
      </q-item>
    </q-list>
<!--    Change profile dialog-->
    <q-dialog v-model="changeProfileDialog">
      <change-profile-form />
    </q-dialog>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import ChangeProfileForm from 'components/profile/change-profile-form'

export default {
  name: 'profile-info-tab-panel',
  components: { ChangeProfileForm },
  computed: {
    ...mapState('user', ['seller'])
  },
  data () {
    return {
      changeProfileDialog: false
    }
  }
}
</script>

<style scoped>

</style>
