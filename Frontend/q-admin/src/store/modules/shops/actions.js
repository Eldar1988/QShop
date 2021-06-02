import utils from 'src/utils'
import axios from 'axios'

export async function loadShops ({ commit }, { uid }) {
  try {
    await axios.get(`${this.state.serverURL}/seller/shops/?uid=${uid}`)
      .then(response => commit('mutationShops', response.data.results))
  } catch (e) {
    utils.notifier(e.message())
  }
}
