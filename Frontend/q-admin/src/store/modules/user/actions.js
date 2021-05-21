import firebase from 'firebase/app'
import utils from 'src/utils'

export async function login ({ commit, dispatch }, payload) {
  try {
    await firebase.auth().signInWithEmailAndPassword(payload.email, payload.password)
    const currentUser = firebase.auth().currentUser
    if (currentUser) {
      commit('mutationsUser', currentUser)
      localStorage.setItem('uid', currentUser.uid)
      utils.notifier('Авторизация прошла успешно.', 'positive')
    }
  } catch (e) {
    utils.notifier(utils.firebaseErrorTranslator(e.code) || e.message)
  }
}

export async function register ({ commit, state }, payload) {
  try {
    await firebase.auth().createUserWithEmailAndPassword(payload.email, payload.password)
    const newUser = firebase.auth().currentUser
    if (newUser) {
      commit('mutationsUser', newUser)
      localStorage.setItem('uid', newUser.uid)
      utils.notifier('Регистрация прошла успешно.', 'positive')
    }
  } catch (e) {
    utils.notifier(utils.firebaseErrorTranslator(e.code) || e.message)
  }
}