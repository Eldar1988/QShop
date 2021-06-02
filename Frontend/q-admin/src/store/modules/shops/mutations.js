export function mutationShops (state, data) {
  state.shops = data
}

export function mutationAddShopDialog (state, status) {
  state.showAddShopDialog = status
}
