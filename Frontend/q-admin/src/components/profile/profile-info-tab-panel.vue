<template>
  <div>
    <q-list separator class="rounded-borders">
      <!--      Name-->
      <q-item clickable v-ripple>
        <q-item-section avatar top>
          <q-avatar icon="person" color="primary" text-color="white"/>
        </q-item-section>
        <q-item-section>
          <q-item-label lines="1">Имя</q-item-label>
          <q-item-label caption>
            <q-input
              v-model="seller.name"
              :disable="nameInputDisable"
              borderless dense
              maxlength="255"
              class=""
              style="max-height: 30px; margin-top: -10px"
              @click="nameInputDisable = !nameInputDisable"
            />
          </q-item-label>
        </q-item-section>
        <q-item-section side>
          <q-btn
            icon="edit"
            dense unelevated
            size="sm"
            color="grey-7"
          >
            <q-tooltip>Изменить</q-tooltip>
          </q-btn>
        </q-item-section>
      </q-item>
      <!--      Phone-->
      <q-item clickable v-ripple>
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
          >
            <q-tooltip>Изменить</q-tooltip>
          </q-btn>
        </q-item-section>
      </q-item>
      <!--      Email-->
      <q-item clickable v-ripple>
        <q-item-section avatar top>
          <q-avatar icon="email" color="primary" text-color="white"/>
        </q-item-section>
        <q-item-section>
          <q-item-label lines="1">Email</q-item-label>
          <q-item-label caption>{{ seller.email }}</q-item-label>
        </q-item-section>
        <q-item-section side>
          <q-btn
            icon="edit"
            dense unelevated
            size="sm"
            color="grey-7"
          >
            <q-tooltip>Изменить</q-tooltip>
          </q-btn>
        </q-item-section>
      </q-item>
    </q-list>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'profile-info-tab-panel',
  computed: {
    ...mapState('user', ['seller'])
  },
  data () {
    return {
      nameInputDisable: false,
      name: this.seller.name
    }
  }
}
</script>

<style scoped>

</style>
