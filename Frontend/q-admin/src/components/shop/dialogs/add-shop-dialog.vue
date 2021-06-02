<template>
  <q-dialog v-model="showAddShopDialog" maximized>
    <q-card>
      <!--      Toolbar-->
      <q-toolbar class="bg-grey-8 text-white">
        <q-toolbar-title class="f-w-700">
          Новый магазин
        </q-toolbar-title>
        <q-btn
          class="text-center"
          icon-right="close"
          flat dense
          @click="mutationAddShopDialog(false)"
        />
      </q-toolbar>
      <!--      Content-->
      <q-card-section style="width: 500px; max-width: 100%; margin: auto">
        <p class="q-py-md text-subtitle1 text-center f-w-700 q-mt-lg">Для создания магазина необходимо заполнить форму
          ниже.</p>
        <div class="add-shop-form">
          <!--          Title-->
          <q-input v-model="formData.title" label="Название магазина" maxlength="100" counter>
            <template v-slot:prepend>
              <q-icon name="store"/>
            </template>
          </q-input>
          <!--          URL-->
          <q-input v-model="formData.url" label="URL адрес" prefix="https://" maxlength="100" counter>
            <template v-slot:prepend>
              <q-icon name="language"/>
            </template>
            <template v-slot:append>
              <q-icon
                name="help_outline"
                color="grey-5"
              >
                <q-tooltip content-class="fontsize-12">Название домена магазина или адрес вашего магазина в сети
                  интернет.<br>Если вы еще не приобрели домен, оставьте это поле пустым, это можно сделать позже.
                </q-tooltip>
              </q-icon>
            </template>
          </q-input>
          <!--          Description-->
          <q-input v-model="formData.description" label="Короткое описание" type="textarea" maxlength="200" counter/>
        </div>
        <!--        Submit-->
        <q-btn
          label="Создать"
          color="positive"
          unelevated
          class="q-mt-lg full-width q-py-sm"
        />
        <div class="text-right">
          <q-btn
            label="Отменить"
            icon-right="close"
            color="grey-5"
            outline no-caps
            class="q-mt-lg"
            @click="mutationAddShopDialog(false)"
          />
        </div>
      </q-card-section>
    </q-card>
  </q-dialog>
</template>

<script>
import { mapMutations, mapState } from 'vuex'

export default {
  name: 'add-shop-dialog',
  computed: {
    ...mapState('shops', ['showAddShopDialog']),
    ...mapState('user', ['seller']),
    sellerId () {
      return this.seller.id
    }
  },
  methods: {
    ...mapMutations('shops', ['mutationAddShopDialog'])
  },
  data () {
    return {
      formData: {
        uid: localStorage.getItem('uid'),
        seller: this.sellerId,
        title: '',
        description: '',
        url: ''
      }
    }
  }
}
</script>
