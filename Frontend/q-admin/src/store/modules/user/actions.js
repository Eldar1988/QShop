import firebase from 'firebase/app'
import utils from 'src/utils'
import axios from 'axios'

export async function login ({ commit, dispatch }, payload) {
  try {
    await firebase.auth().signInWithEmailAndPassword(payload.email, payload.password)
    const currentUser = firebase.auth().currentUser
    if (currentUser) {
      localStorage.setItem('uid', currentUser.uid)
      utils.notifier('Авторизация прошла успешно.', 'positive')
      await dispatch('loadSeller', currentUser.uid)
    }
  } catch (e) {
    utils.notifier(utils.firebaseErrorTranslator(e.code) || e.message)
  }
}

export async function register ({ dispatch }, payload) {
  try {
    await firebase.auth().createUserWithEmailAndPassword(payload.email, payload.password)
    const newUser = firebase.auth().currentUser
    if (newUser) {
      localStorage.setItem('uid', newUser.uid)
      utils.notifier('Регистрация прошла успешно.', 'positive')
      await dispatch('createSeller', { uid: newUser.uid, email: newUser.email })
    }
  } catch (e) {
    utils.notifier(utils.firebaseErrorTranslator(e.code) || e.message)
  }
}

export async function createSeller ({ commit }, payload) {
  try {
    await axios.post(`${this.state.serverURL}/seller/create_seller/`, {
      email: payload.email,
      uid: payload.uid
    }).then(response => commit('mutationsSeller', response.data))
  } catch (e) {
    utils.notifier(e.message)
  }
}

export async function loadSeller ({ commit }, uid) {
  try {
    await axios.get(`${this.state.serverURL}/seller/get_seller/${uid}/`)
      .then(response => commit('mutationsSeller', response.data))
  } catch (e) {
    utils.notifier(e.message)
  }
}

export function logout ({ commit }) {
  utils.notifier('Вы вышли из аккаунта. Для продолжения работы необходимо войти.')
  commit('mutationsSeller', null)
  this.$router.replace('/login').then(() => {
    localStorage.setItem('uid', '')
  })
}

export async function updateSeller ({ commit }, payload) {
  try {
    await axios.patch(`${this.state.serverURL}/seller/update_seller/${payload.uid}/`, {
      name: payload.name,
      phone: payload.phone
    })
      .then(response => {
        commit('mutationsSeller', response.data)
        utils.notifier('Профиль изменен.', 'positive')
      })
  } catch (e) {
    utils.notifier(e.message)
  }
}

export async function loadSellerNotifications ({ commit }) {
  try {
    await axios.get(`${this.state.serverURL}/seller/notifications/`)
      .then(response => commit('mutationsSellerNotifications', response.data.results))
  } catch (e) {
    utils.notifier(e.message)
  }
}
