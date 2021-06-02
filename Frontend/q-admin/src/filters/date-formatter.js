export default function dateFormatter (dateToFormat) {
  const date = new Date(dateToFormat)
  return new Intl.DateTimeFormat('RU-RU').format(date)
}
