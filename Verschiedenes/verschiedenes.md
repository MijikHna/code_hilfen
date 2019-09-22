* Django-Admin Location - `/usr/local/bin/django-admin`

#### SVG nach PNG konvertieren:
* zuerst als .svg speichert, dann in Canvas als Image laden
```javascript
var canvas = document.querySelector("canvas"),
    context = canvas.getContext("2d");

var image = new Image;
image.src = "fallback.svg";
image.onload = function() {
  context.drawImage(image, 0, 0);

  var a = document.createElement("a");
  a.download = "fallback.png";
  a.href = canvas.toDataURL("image/png");
  a.click();
};
```