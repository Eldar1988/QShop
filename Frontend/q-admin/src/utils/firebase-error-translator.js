export default function (errCode) {
  if (errCode === 'auth/invalid-email') return 'Вы ввели некорректный email.'
  if (errCode === 'auth/user-not-found') return 'Неверный логин или пароль. Пожалуйста, будьте внимательнее'
  return null
}
