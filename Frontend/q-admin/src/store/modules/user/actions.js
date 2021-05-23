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
