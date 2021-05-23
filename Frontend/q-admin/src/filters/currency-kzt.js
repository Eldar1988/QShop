export default function currencyKZTFormatter (val) {
  return new Intl.NumberFormat('KZ-KZ', {
    style: 'currency',
    currency: 'KZT'
  }).format(val)
}
