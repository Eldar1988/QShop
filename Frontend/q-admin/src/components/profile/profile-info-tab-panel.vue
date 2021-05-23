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
          <q-item-label caption>Хайбулов Эльдар Фаритович Кувцфвцс фцвцфвфц</q-item-label>
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
          <q-item-label caption>+7 707 855 3710</q-item-label>
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
          <q-item-label caption>TEst@mail.com</q-item-label>
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
export default {
  name: 'profile-info-tab-panel'
}
</script>

<style scoped>

</style>
