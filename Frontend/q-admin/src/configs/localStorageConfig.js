export default function () {
  if (!localStorage.getItem('uid') || localStorage.getItem('uid') === '') {
    localStorage.setItem('uid', '')
  }
  if (!localStorage.getItem('darkThemeIsActive')) {
    localStorage.setItem('darkThemeIsActive', 'false')
  }
}
