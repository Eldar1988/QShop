import { Notify } from 'quasar'

export default function (message, color = 'dark', position = 'top') {
  Notify.create({
    message: message,
    position: position,
    color: color,
    multiLine: true,
    actions: [
      { label: 'Ok', color: 'white', handler: () => { /* ... */ } }
    ]
  })
}
