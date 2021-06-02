<template>
  <div>
    <q-list separator class="rounded-borders">
      <!--      Name-->
      <q-item>
        <q-item-section avatar top>
          <q-avatar icon="person" color="primary" text-color="white"/>
        </q-item-section>
        <q-item-section>
          <q-item-label caption>Имя</q-item-label>
          <q-item-label>{{ seller.name || 'Anonim' }}</q-item-label>
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
          <q-item-label caption>Номер телефона</q-item-label>
          <q-item-label>+7 {{ seller.phone }}</q-item-label>
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
          <q-item-label caption>E-mail</q-item-label>
          <q-item-label>{{ seller.email }}</q-item-label>
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
