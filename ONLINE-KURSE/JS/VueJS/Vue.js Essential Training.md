# Vue.js Essential Training

* [https://github.com/planetoftheweb/vue-essentials]

## 1 - Vue.js Overview

### 1 - Basic installation

* hier wurde mit CDN-Link eingefügt

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Vue App</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
</head>
<body class="container mt-4">
  
  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

  <div id='app'>
    <h2>{{ name }}</h2>
  </div>


  <script>
    var app = new Vue({
      el: '#app',
      data: {
        name: 'Lala'
      }
    })
  </scipt>
</body>
</html>
```

### 2 - Reactive data

* Code in Vue ist reactive d.h. reagiert auf Veränderungen

```html
<div id='app'>
  <h2>{{name}}</h2>
  <p>{{desctiption}}</p>
  <div class="h3">${{price}}</div>
</div>

```

```js
let data = {
  'name': 'Lala',
  'description': 'Lala Text',
  'image': 'https://lala.img',
  'prise': 99,

}

let app = new Vue({
  el: '#app',
  data: data
})
```

### 3 - Binding data to attributes

```html
<div id='app'>
  <h2>{{name}}</h2>
  <!-- hier Variable zum HTML-Attr binden: src-->
  <img class="img-fluid" v-bind:src="image" v-bind:alt="name">
  <img class="img-fluid" :src="image" :alt="name">
  <p>{{desctiption}}</p>
  <div class="h3">${{price}}</div>
</div>
```

```js
let data = {
  'name': 'Lala',
  'description': 'Lala Text',
  'image': 'https://lala.img',
  'prise': 99,

}

let app = new Vue({
  el: '#app',
  data: data
})
```

### 4 - Looping through data

```html
<div class="container" id="app">
  <!-- mit v-for durch Arrays gehen-->
  <div class="row d-flex mb-3 align-items-center" v-for="item in products">
   <div class="col-sm-4">
     <!-- hier Binding -->
    <img class="img-fluid d-block" :src="item.image" :alt="item.name">
   </div>
   <div class="col">
     <h3 class="text-info">{{ item.ame }}</h3>
     <p class="mb-0">{{ item.description }}</p>
     <div class="h5 float-right">${{item.price}}</div>
    </div>
  </div>
</div>

```

```js
let data = {
  products: {
    {
      'id': '1',
      'name': 'lala1',
      'description': 'lala1'
      'image': 'lala.png',
    },
    {
      'id': '1',
      'name': 'lala1',
      'description': 'lala1'
      'image': 'lala.png',
    },
  }
}

let app = new Vue({
  el: '#app',
  data: data
})
```

### 5 - Condition data

```html
<!-- boolean oder Ausdruck  Number() um auf jeden Fall zu int zu konvertieren-->
<div v-if="item.price<=Number(maximum)">
  ...
</div>

<div class="col-sm-4"
  v-for="item in products"
  v-if="item.price<=Number(maximum)">
  ...
</div>

```

* man kann `v-for` und `v-if` im gleichen Element haben

```js
let data = {
  maximum: 99,
  products: {
    {
      'id': '1',
      'name': 'lala1',
      'description': 'lala1'
      'image': 'lala.png',
    },
    {
      'id': '1',
      'name': 'lala1',
      'description': 'lala1'
      'image': 'lala.png',
    },
  }
}

let app = new Vue({
  el: '#app',
  data: data
})
```

### 6 - Handling user input

```html
<div id='app'>


  <div class="form-inline mr-auto">
    <label class="font-weight-bold mr-2" form="formMax">max</label>
    <input type="text" id="formMax" class="form-control w-25" v->
  </div>

  <div>
    <!-- hier nur one-way-Binding-->
    <input type="text", class="form-control w-25" v-model="maximum">
    <!-- two-way-Binding -->
    <input type="text", class="form-control w-25" :value="maximum">

    <div class="form-inline mr-auto">
      <label class="font-weight-bold mr-2" form="formMax">max</label>
      <input type="text" id="formMax" class="form-control w-25" v-model="maximum">

      <input type="range" class="custom-range" min="0" max="200" v-model="maximum">
    </div>
  </div>

</div>

```

```js
let data = {
  'name': 'Lala',
  'description': 'Lala Text',
  'image': 'https://lala.img',
  'prise': 99,

}
```

### 7 - Lifecycle hooks

```html
<div id='app'>
  ...
</div>
```

```js
let app = new Vue({
  el: '#app',
  data: {
    maximum: 99,
    // hier ist null wichtig, damit der constructor products anlegt
    products: null,
  },

  //LifeCycle-Methoden (hier mounted() sowas wie init)
  mounted: function(){
    fetch('https://lala/lalaX')
      .then(response => {
        response.json();
      })
      .then(data => {
        this.products = data;
      });
  }
  //ODER SO
  mounted() => {
    //..
  }
});
```

### 8 - Events and methods

```html
<div id="app">
<!-- für cart:-->
<nav class="navbar navbar-light bg-light fixed-top"
  v-if="cart.lenght>0">

  <div class="navbar-text ml-auto">
    <b>cart:</b>
     <span class="badge badge-pill badge-success">{{cart.length}}</span>
  </div>
</nav>

 <div class="form-inline mr-auto mt-5">
  <label class="font-weight-bold mr-2" for="formMax">max</label>
   <input type="text" id="formMax" class="form-control w-25" v-model="maximum">  
 </div>
 <input type="range" class="custom-range" min="0" max="200" v-model="maximum">
  <div class="row d-flex mb-3 align-items-center"
       v-for="item in products"
       v-if="item.price<=Number(maximum)">
   <div class="col-1 m-auto">
     <!--Event binden-->
    <button class="btn btn-info"
      v-on:click="cart.push(item)">+</button>
    <button class="btn btn-info"
    v-on:click="addItem(item)">+</button>
   </div>
   <div class="col-4">
    <img class="img-fluid d-block" :src="item.image" :alt="item.name">
   </div>
   <div class="col">
     <h3 class="text-info">{{ item.name }}</h3>
     <p class="mb-0">{{ item.description }}</p>
     <div class="h5 float-right">${{ Number(item.price) }}</div>
    </div>
  </div>
</div>
```

```js
var app = new Vue({
  el: '#app',
  data: {
    maximum: 99,
    products: null
    cart: []
  },
  mounted: function() {
    fetch('https://lala/lala')
    .then(response => response.json())
    .then(data => {
      this.products = data;
    })
  }
  //hier werden die Methoden der Componente definiert
  methods: {
    addItem: function(product){
      this.cart.push(product);
    }
 }
});
```

## 2 - Working with Templates

### 1 - Templates interpolations

```html
<div class="container" id="app">

 <p>
  <strong>Bound:</strong><br>
  <!-- Beweis der interpolation-->
  <span>{{name}}</span>
 </p>

 <p>
  <strong>Parsed:</strong><br>
  <!-- damit kann man auch HTML-Syntax realisieren. Ist aber gefährlich, da hier jemand den Malicous Code einfügen kann -->
  <!-- + weiteren String-->
  <span v-html="name + 'XYZ'"></span>
 </p>

  <!--gejt auch hier-->
 <p v-once>
  <strong>Unchangeable:</strong><br>
  <!-- nur Ein Mal inerpolation/Rendering, also wird nicht upgedatet-->
  <span v-once>{{name}}</span>
 </p>

 <h5>Text</h5>
 <textarea class="form-control" rows="3"
   v-model="name"></textarea>
</div>
```

```js
var app = new Vue({
  el: '#app',
  data: {
   name: "Fluffy Ski Coat"
  }
})
```

### 2 - Binding attributes with v-bind

```html
<div id='app'>
  <!-- hier in '' da ein String und nicht Teild von data-->
  <img :class="'ing-fluid'" v-bind:src="products[0].image" :alt="products[0].name">

  <img :class="ingClass + ' ' + 'w-25'"
    v-bind:src="products[0].image"
    :alt="products[0].name">

  <!-- weiter Möglichkeit zu binden !! Object-Syntax -->
  <img v-bind="{
    class: ingClass + ' ' + 'w-25',
    src: products[1].image,
    alt: products[1].name,
  }">
</div>
```

```js
let data = {
  products: {
    {
      'id': '1',
      'name': 'lala1',
      'description': 'lala1'
      'image': 'lala.png',
    },
    {
      'id': '1',
      'name': 'lala1',
      'description': 'lala1'
      'image': 'lala.png',
    },

    ingClass='ing-fluid'
  }
}

let app = new Vue({
  el: '#app',
  data: data
})
```

### 3 - Using Computed properties

* einfache Transformationen reusable + werden gecached

```html
<div class="container" id="app">
  <h3>Slugetize</h3>
  <input class="form-control" types="text" v-model="slugtText">
  <div class="font-weight-bold text-danger">
    {{slugText
      .toLowerCase()
      .replace(/[^\w ]+/g, '')
      .replace(/ +/g, '-')}}
  </div>

  <div class="font-weight-bold text-danger">
    {{slugetize()}}
  </div>
</div>
```

```js
let app = new Vue({
  el: '#app',
  data: {
    slugText: 'Text'
  }

  computed: {
    slugetize: function(){
      return this.slugText
        .toLowerCase()
        .replace(/[^\w ]+/g, '')
        .replace(/ +/g, '-')
    }
  }
});
```

### 4 - Using methods

* computed vs methods: methods cachen nicht d.h. werden jedes Mal neu aufgerufen

```html
<div class="container" id="app">
  <h3>Slugetize</h3>
  <input class="form-control" types="text" v-model="slugtText">
  <div class="font-weight-bold text-danger">

  <div class="font-weight-bold text-danger">
    {{slugetize()}}
  </div>
</div>

```

```js
let data = {
  'name': 'Lala',
  'description': 'Lala Text',
  'image': 'https://lala.img',
  'prise': 99,

}

let app = new Vue({
  el: '#app',
  data: {
    slugText: 'Text'
  }

  // sind nicht reacitive. Da hier 
  computed: {
    // ist nicht reacitive. Da hier keine Variable aus data benutzt wird => wird nur ein Mal beim Erstellen der Componente aufgerufen und gecached und wird eigentlich wie Attribut behandelt
    now: function () {
      var date = new Date();
      return (
        Strig(date.getHours()) +
        Strign(data.getMinutes()) +
        data.getSeconds()
      );
    },

    slugetize: function(){
      return this.slugText
        .toLowerCase()
        .replace(/[^\w ]+/g, '')
        .replace(/ +/g, '-') + '--' + this.now + '--' this.now()
    },
  }

  methods: {
    now: function () {
      var date = new Date();
      return (
        Strig(date.getHours()) +
        Strign(data.getMinutes()) +
        data.getSeconds()
      );
    },
  }
});
```

## 3 - Managing CSS Styles

### 1 - Binding classes with objects and arrays

```html
<div id="app">
  <nav class="navbar navbar-light bg-light fixed-top"
      v-if="cart.length>0">
    <div class="navbar-text ml-auto">
      <b>cart:</b> 
      <span class="badge badge-pill badge-success">{{cart.length}}</span>
    </div>
  </nav>

  <h2>My Shop</h2>
  <div class="d-flex align-item-center">
    <!-- da man hier v-bind für classe benutz kann man hier JS-Expression (hier Array) benutzen-->
    <label v-bind:class="['font-weight-bold', 'mr-2']" for="formMax">max</label>
    <label v-bind:class="labelArray" for="formMax">max</label>
    <!-- als Array aus Vue-Obj-->
    <input type="text" id="formMax" class="form-control w-25" v-model="maximum">  

    <input type="text" id="formMax" class="form-control mx-2" style="width: 60px; text-align: center" v-model="maximum">
    <!-- Style bidnen  als JS-Obj-->
    <input type="text" id="formMax" class="form-control mx-2" :style="{'width': '60px'; 'text-align' :'center'}" v-model="maximum">

    <input type="range" class="custom-range" min="0" max="200" v-model="maximum">
  </div>

  <div class="row d-flex mb-3 align-items-center"
       v-for="item in products"
       v-if="item.price<=Number(maximum)">
   <div class="col-1 m-auto">
    <button class="btn btn-info"
            v-on:click="addItem(item)">+</button>
   </div>
   <div class="col-4">
    <img class="img-fluid d-block" :src="item.image" :alt="item.name">
   </div>
   <div class="col">
     <h3 class="text-info">{{ item.name }}</h3>
     <p class="mb-0">{{ item.description }}</p>
     <div class="h5 float-right">${{ Number(item.price) }}</div>
    </div>
  </div>
</div>
```

```js
var app = new Vue({
 el: '#app',
 data: {
  maximum: 99,
  products: null,
  cart: [],
  labelArray = ['font-weight-bold', 'mr-2'],
 },
 methods: {
  addItem: function(product) {
   this.cart.push(product);
  }
 },
 mounted: function() {
  fetch('https://hplussport.com/api/products/order/price')
  .then(response => response.json())
  .then(data => {
    this.products = data;
  })
 }
});

```

### 2 - Expressions and computed classes

```html
 <input type="text" id="formMax" class="form-control mx-2" style="width': inputWidth; text-align: center" v-model="maximum">

  <input type="text" id="formMax" class="form-control mx-2" style="width': inputWidth2 + 'px'; text-align: center" v-model="maximum">
  <!-- geht auch JS-Syntax für Styles-Attr-->
  <input type="text" id="formMax" class="form-control mx-2" style="width': inputWidth2 + 'px'; textAlign: center" v-model="maximum">

  <!-- Classen bei Bedinung anzeigen-->
  <div class="align-item-center" :class="siderState">
```

```js
var app = new Vue({
 el: '#app',
 data: {
  maximum: 99,
  products: null,
  cart: [],
  labelArray = ['font-weight-bold', 'mr-2'],
  inputWidth: '60px',
  inputWidth2: 60,
  sliderStatus: true,
 },

 computed: {
   sliderState: function(){
     return this.sliderStatus ? 'd-flex' : 'd-none'
   }
 }
 methods: {
  addItem: function(product) {
   this.cart.push(product);
  }
 },
 mounted: function() {
  fetch('https://hplussport.com/api/products/order/price')
  .then(response => response.json())
  .then(data => {
    this.products = data;
  })
 }
});
```

* in DevTools kann man aber auf das Vue-Obj zugreife z.B `app.sliderStatus=true`

### 3 - Toggling computed classes

* Font Awsome Lib benutzt

```html
<nav class="">
  <div class="">
    <!-- geht auch v-on = @. Also mit click-Event toggeln-->
    <button class="btn btn-sm btn-outline-success" v-on:click="sliderStatus = !sliderStatus"> <i class="fas fa-dollar-sign"></i></button>
    <div class="ml-2" v-if="cart.length>0">
      ...
    </div>
  </div>
</nav>

```

```js

```

### 4 - Creating transitions and animations

* Vue hat eignen Tag für Animantion: `transition`. Diese Transition Klassen kann man bei Vue-Doku finden.

```html

<transition name="fade">
  <div v-if="sliderStatus">
    ...
  </div>
</transition>

```

```js
var app = new Vue({
 el: '#app',
 data: {

 }

});
```

```css
/* Syntax nameVon<transition>-Event als Klasse

Faden wenn ein/ausgeschaltet. Diese Klasses werden injected/removed
*/
.fade-enter .fade-leave-to{
  opacity: 0;
}

.fade-enter-active .fade-leave-active{
  transition: all 1s ease-in-out;
}
```

### 5 - Using an animation framework

* hier wird die Lib: **Animate.css** verwendet. Bei Github über CDN "installieren"

```html
<!-- enter... ist für Animate.css
Syntax: enter-active-class="identifer animateAnimationFunktion"
-->
<transition name="custom" enter-active-class="animated fadeInDown" leave-active-class="animated slideOutRight">
  enter-active
</transition>
```

```js

```

### 6 - Working with transition groups

* Also: die Animation auf ganze Gruppe von HTML-Elementen anwenden

```html
...
<transition-group name="myStyleClass" name="fade" tag="div" enter-active-class="animated fadeInRight"> <!-- mit tag=XXX angeben, in welches Elemente  die Items  gewrappt werden soll.  enter-active-class="animated" für Animate.css-Lib--> 
  <div
    v-for="(item, index) in products" :key="item.id"
    v-if="..."
  >
  <!-- hier wird key und index benötigt-->

  </div>
</transition-group>
...
```

```js

```

```css
.fade-enter .fade-leave-to{
  opacity: 0;
}

.fade-enter-active .fade-leave-active{
  transition: all 1s ease-in-out;
}
```

### 7 - Managing styles with JS

* Animation mit JS kontrollireen

```html
<transition-group name="myStyleClass" name="fade" tag="div" 
  @beforeEnter="beforeEnter()"
  @enter="enter()"
  @leave="leave()">
  
  <!-- mit tag=XXX angeben, in welches Elemente  die Items  gewrappt werden soll.  enter-active-class="animated" für Animate.css-Lib--> 
  <div
    v-for="(item, index) in products" :key="item.id"
    v-if="..."
    :data-index="index"> <!-- data-index binden mit index bzw. i LaufVar -->
  >
  <!-- hier wird key und index benötigt-->

  </div>
</transition-group>
```

```js

...
  methods:{
    beforeEnter: function(el){ //erstellten Element übergeben
      el.className='d-none';
    }

    enter: function(el){
      let delay = el.dataset.index * 100; //mit dataset.XXX kann man auf data-XXX zugreifen
      setTimeoute(function() {
        el.className='row mb-3 align-items animated fadeInRight';
      }, delay)
    }

    leave: function(el){
      let delay = el.dataset.index * 100;
      setTimeoute(function() {
        el.className='row d-flex mb-3 align-items animated fadeOutRight';
      }, delay)
    }


  }
```

## 4 - Digging Deeper

### 1 - Creating filters

* Daten verarbeiten z.B floats zum richtigen Format für Währung

```js
var app = new Vue({
  el: '#app'
  data: {
    ..
  }
  filters: {
    currency: function(value){
      return '$' + Number.parseFloat(value).toFixed(2);
    }
  }
```

```html
  <div class="h5 float-right">{{ item.price | currency }} </div>
```

* man kann filters bzw. pipes verketten

* filters und methoden können auch außerhalb von Vue-Obj definiert werden + können in mehreren Vue-Instanzen benutzt werdenz.B 

```js
Vue.filter('currency', function(){
  currency: function(value){
      return '$' + Number.parseFloat(value).toFixed(2);
    }
})
```

### 2 - Toggling elements with a key

```html
<button class="btn btn-success btn-sm dropdown-toggle" 
  id="cartDropwDown" data-toggle="dropdown"
><b>cart:</b></button>

<div class="dropdown-menu dropdown-menu-right">
  <div v-for="(item, index) in cart" :key="index">
    <div class="dropdown-item-text text-nowrap text-right">
      <span class="badge badge-pill badge-warning align-text-top mr-1">{{item.qty}}</span>
      {{item.name}}
      <b>{{item.price | currency}}</b>
    </div>
  </div>
</div>
```

### 3 - Categorizing lists

* Idee hier in `cart` es folgendemaßen zu speichern: `cart: [{{product}, qty}, {{product}, qty}]`

```html
  <span class="badge badge-pill badge-warning align-text-top mr-1">{{item.qty}}</span>
  {{item.product.name}}
  <b>{{item.qty * item.product.price | currency}}</b>
```

```js
...

addItem: function(product){
  var whichProduct;
  var existing = this.cart.filter(function(item, index){
    if(item.product.id==Number(product.id)){
      whichProduct = index;
      return true;
    }
    else{
      return false;
    }
  });

  if(existing.length){
    this.cart[whichProduct].qty++;
  }
  else{
    this.cart.push({product: product, qty: 1})
  }
}

...
```

### 4 - Adding computed classes

```html
<span class="badge bagde-pill badge-light"> {{cartQty}}
  <i class="fas fa-shopping-cart mx-2"></i>
  {{cartTotal|currency}}
</span>

</div> 
```

```js
  computed: {
    carTotal: function(){
      let sum = 0;
      for (key in this.cart){
        sum = sum + this.cart[key].product.price)*this.cart[key].qty);
      }
      return sum;
    }

    carQty: function(){
      let qty = 0;
      for (key in this.cart){
        qty = qty + this.cart[key].qty);
      }
      return qty;
    }

  }
```

### 5 - Deleting items and modifiers

```html
  <a href="a" v-on:click.stop="deleteItem(index)" class="badge badge-danger text-white"></a>
  <!-- mit click.stop um bootsrap-Propagation zu stoppen-->
```

```js
...
  methods: {
    ...
    deleteItem: function(id){
      if(this.cart[id].qty > 1){
        this.cart[id].qty--;
      }
      else{
        this.cart.splice(id, 1);
      }
    }
  }
```

## 5 - Component Bases Vue

### 1 - Creating reusable components

```js
// price = Name des Obj. {} - die Componente
Vue.component('price', {
  // sollte eine Funktion sein
  data: function() {
    return {
      prefix: '$',
      value: 23.23,
      precision: 2,
    }
  },
  // HTML- in das die Componente gewrappt wird
  template: '<span>{{this.prefix + Number.parseFloat(this.value).toFixed(this.precision)}}</span>'
})

```

```html
  <!-- Vue-Componente als HTML-Tag einfügen-->
  <div><price></price></div>
```

### 2 - Using props

```js
Vue.component('price', {
  // sollte eine Funktion sein
  data: function() {
    return {
    }
  },
  // HTML- in das die Componente gewrappt wird
  template: '<span>{{this.prefix + Number.parseFloat(this.value * this.conversion).toFixed(this.precision)}}</span>',
  props: ['value', 'prefix', 'precision', 'conversion'],
})
```

```html
<!--Werte an die Componente übergeben/binden-->
<div><price value="item.price"></price></div>

<div><price v-bind:value="item.price"></price></div>

<div>
  <price 
    v-bind:value="item.price" 
    :prefix=="&euro;" 
    :precision="2" 
    convertion=".87"></price>
</div>
```

### 3 - Prop options

* auch als Obj übergeben. Dann ist möglich Default-Wert, Typ, ob requeired usw. setzen

```js
props: {
  value: Number, //Typ
  prefix: {
    type: String,
    default: '$' //Default-Wert
  },
  precision: {
    type: Number,
    default: 2
  },
  conversion: {
    type: Number,
    default: 2,
  }
}
```

* in html muss man eigentlich nichts ändern
* eventuell muss man bei prop-Übergabe in html mit `Number()` konvertieren

### 4 - Building compolex components

```js

```

```html
...
<price :value="item.price"></price>

<!-- mit :products und :maximum die Werte von Eltern-Comp and Kind-Comp übergeben-->
<product-list :products="products" :maximum="maximum"></product-list>
...
```

```js
Vue.component('product-list', {
  props: ['products', 'maximum'];

  template: `
    <transition-group name="fade" tag="div"
    @beforeEnter="beforeEnter"
    @enter="enter"
    @leave="leave">
      <div class="row d-none mb-3 align-items-center" 
          v-for="(item, index) in products" :key="item.id"
          v-if="item.price<=Number(maximum)"
          :data-index="index">
        <div class="col-1 m-auto">
          <button class="btn btn-info"
                  v-on:click="addItem(item)">+</button>
        </div>
        <div class="col-4">
          <img class="img-fluid d-block" :src="item.image" :alt="item.name">
        </div>
        <div class="col">
          <h3 class="text-info">{{ item.name }}</h3>
          <p class="mb-0">{{ item.description }}</p>
          <div class="h5 float-right">
            <price :value="Number(item.price)"></price></div>
        </div>
      </div>
    </transition-group>
  `,
  methods: {
    beforeEnter: function(el) {
      el.className='d-none'
    },
    enter: function(el) {
      var delay=el.dataset.index * 100;
      setTimeout(function() {
        el.className='row d-flex mb-3 align-items-center animated fadeInRight'
      }, delay);
    },
    leave: function(el) {
      var delay=el.dataset.index * 100;
      setTimeout(function() {
        el.className='row d-flex mb-3 align-items-center animated fadeOutRight'
      }, delay);
    },
  }
});
```

### 5 - Emitting events from within components

* = Events and Kind-Comp weitergeben
* Die Syntax vom ganzen ist etwas gewöhnungsbedürftig

```html

<!-- Also beim Catchen des Events add wird addItem() aufgerufen -->
<product-list :products="products" :maximum="maximum" @add="addItem"></product-list>


```

```js
template: `
    <transition-group name="fade" tag="div"
    @beforeEnter="beforeEnter"
    @enter="enter"
    @leave="leave">
      <div class="row d-none mb-3 align-items-center" 
          v-for="(item, index) in products" :key="item.id"
          v-if="item.price<=Number(maximum)"
          :data-index="index">
        <div class="col-1 m-auto">
          <button class="btn btn-info"
                  <!-- Name des Events in '' und weitere Params normal-->
                  v-on:click="$emit('add', item)>+</button>
        </div>
        <div class="col-4">
          <img class="img-fluid d-block" :src="item.image" :alt="item.name">
        </div>
        <div class="col">
          <h3 class="text-info">{{ item.name }}</h3>
          <p class="mb-0">{{ item.description }}</p>
          <div class="h5 float-right">
            <price :value="Number(item.price)"></price></div>
        </div>
      </div>
    </transition-group>
  `,
```

## 6 - Building with the CLI

### 1 - Installing projects using the Vue CLI

* also wie Angular-CLI
* Schritte:
  1. `npm install -g @vue/cli`
  2. `vue create PROJ-NAME` - Project erstellen
  3. `npm run server` - Dev-Version öffnen

### 2 - Understanding Vue CLI installations

* App.vue = Main Component
* in components-Ordner werden dann eigene Componenten erstellt
* in essets-Ordner werden CSS, Images, JSONs abgelegt
* in public-Ordner alles was nicht von Vue.js kontrolliert werden soll

### 3 - How CLI components load

* 

### 4 - Installing additional modules

### 5 - Testing your module installations

## 7 - Projects with the Build Tools

### 1 - Creating a component

### 2 - Managing complex child components

### 3 - Using the Chrome DevTools

### 4 - Emitting updates

### 5 - Adding navigation

### 6 - Fixing components issues

## 8 - Using the Vue Router

### 1 - Reorganizing hierarchy

### 2 - Creating a checkout page

### 3 - Building your routes

### 4 - Creating route links
