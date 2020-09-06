Alterntiven zu IF in JS
1. Ternärer Ausdruck
2. Switch-Case
3. && oder ||
    1. &&  z.B `user && user.name` wenn erster Ausruck (`user`) ist False => wird dieser Returnt, wenn erster Ausdruck ist true wird rechter Teil returnt `user.name`
    2. || z.B `username || "Test"`, wenn linke Seite ist true wird diese returnt `username`, wenn linke Seite ist false wird rechter Teil returnt `"Test"`
4. `Карты сопоставлений` - 
```js
function getStatusColor (status) {
  if (status === 'success') {
    return 'green'
  }
  if (status === 'warning') {
    return 'yellow'
  }
  if (status === 'info') {
    return 'blue'
  }
  if (status === 'error') {
    return 'red'
  }
}
```
```js
function getStatusColor (status) {
  return {
    success: 'green',
    warning: 'yellow',
    info: 'blue',
    error: 'red'
  }[status]
}
```