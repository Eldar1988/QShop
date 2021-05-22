export default function (errCode) {
  console.log(errCode)
  if (errCode === 'auth/invalid-email') return 'Вы ввели некорректный email.'
  if (errCode === 'auth/user-not-found') return 'Неверный логин или пароль. Пожалуйста, будьте внимательнее.'
  if (errCode === 'auth/email-already-in-use') return 'Пользователь с таким e-mail уже зарегистрирован.'
  if (errCode === 'auth/wrong-password') return 'Неверный логин или пароль. Пожалуйста, будьте внимательнее.'
  return null
}
