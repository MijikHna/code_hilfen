### 0 - Introduction
* npm, nodejs, 
* https://github.com/planetofweb/learnangular
* alle Branches vom git holen
    + `git clone --bare https://github...` - als bare-Repo ziehen = nur Git-Folder herunterladen
    * `git config --bool core.bare false` - von bare normale Repo machen
    * `git reset --hard` - damit holt man dann alle Branches
    * wenn man im master ist dann kann man
        * `npm install` - es wird alles installiert, was packages.json steht
    * `npm start` NodeJs-Server starten
    * zum Branch gehen
### 1 - Preparing for Angular 2
#### 1 - What is Angular JS
* Prinzip
    * Componente die dann mit Klassen erweitert werden
    * keine Contoller mehr
        * keine Scopes mehr
    * Sprachen: 
        * JS
        * Dart
        * TypoScript ist zu bevorzugen (hat ES6 Features)
            * ES6 classes
            * ES6 Templates
            * typisiert Variablen
            * Annotationen
            * eventuell muss man Build tools nutzen, da nicht alle Browser TypoScrip unterstützen
    * 
#### 2 - Working with out build tool
* da JS nicht weiß wie es Module behandeln soll
    * dafür wird **systemjs** verwendet (Code gibt es auf github)
* Struktur:
    * ./app
    * ./css
    * ./images
    * ./index.html
    * ./packages.json
    * ./tsconfig.json - wie TS in JS konvertiert wird
    * ./systemjs.config.js
* Installationen
    * alles von github holen
    * ins Ordner gehen
    * `npm install`
#### 3 - Setting up template
* man braucht 3 Dateien
    * app bootstrapen
        * systemjs.config.js schauen, wie die main-Dateie heißt
        * in /app **app.boot.ts** erstellen
        ```ts
        import { PlatformBrowserDynamic } from '@angular/platform-browser-dynamic'
        import { AppModule } from './app.modules'
        
        platformBrowserDynamic().bootstrapModule(AppModule);
        ```
        * in /app **app.modules.ts** erstellen
        ```ts
        import { NgModule } from '@angular/core';
        import { BrowserModule } form '@angular/platform-browser';

        import { AppComponent } form './component.app';

        @NgModule({
            imports: [BrowserModule], //importiert Module
            declarations: [AppComponent], //declarations = importiert Componenten
            bootstrap [AppComponent] //was gestartet werden soll
        })
        export class AppModule {}
        ```
        * in /app **app.component.app.ts** erstellen
        ```ts
        import { Component } form '@angular/core';

        @Component({
            selector: 'app',
            template: '<h1>Test</h1>'
        })
        export class AppComponent 
        * `npm start` ausführen
    * 
### 2 - Getting Started
#### 1 - Understanding Angular templates
* index.html
```html
<html>

<head>
  <title>Learning Angular</title>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <link rel="stylesheet" href="css/page.css">

  <script src="node_modules/core-js/client/shim.min.js"></script>
  <script src="node_modules/zone.js/dist/zone.js"></script>
  <script src="node_modules/reflect-metadata/Reflect.js"></script>
  <script src="node_modules/systemjs/dist/system.src.js"></script>
  
  <script src="systemjs.config.js"></script>

  <script>
        System.import('app').catch(function(err){ console.error(err); });
    </script>
</head>

<body>
  <app>Loading...</app>
</body>

</html>
```
* component.app.ts
```js
import { Component } from '@angular/core';

@Component({
  selector: 'app',
  templateUrl: './templates/app.html'
})

export class AppComponent {}
```
* /templates/app.html
```html
<div class="card search">
    <h1 class="search-headline">Artist Directory</h1>
    <label class="search-label">search</label>
  </div><!-- card search -->
```
#### 2 - Displaying data in templates
* templates/app.html
```html
<div class="card search">
  <h1 class="search-headline">Artist Directory</h1>
  <label class="search-label">search
    <span *ngIf="name">for: {{ name }}</span></label>
</div><!-- card search -->

<ul class="artistlist cf">
  <li class="artistlist-item cf" 
    *ngFor="let item of artists">
    <h2 class="artist-name">{{ item.name }}</h2>
    <h3 class="artist-reknown">{{ item.school }}</h3>
  </li>
</ul>
```
* `{{}}` - Interpolation
* MikroSyntax - sagt Angular welche WErte des Arrays in temp Variablen gespiechert sollen: `*ngFor="let item of artists"`: `item` = tempVar, `artists` kommpt aus Componente. Ähnlich der For-Schleife für Templates.
* component.app.ts
```js
import { Component } from '@angular/core';

@Component({
  selector: 'app',
  templateUrl: './partials/app.html' 
})

export class AppComponent {
  name: string;
  //artists: string[];
  artists: any;

  constructor() {
    this.name = 'Xhou Ta';
    this.artists = [
      {
        name: 'Barot Bellingham',
        school: 'Penn State'
      }, {
        name: 'Jonathan Ferrar',
        school: 'University of Illinois'
      }, {
        name: 'Hillary Post',
        school: 'University of Florida'
      } 
    ]
  }
}
```
* oben werden Eigenschaften deklariert
* Konstruktor initialisiert diese dann. Wird ausgeführt, wenn AppComponente erstellt wird.
* `any` - beliebiger typ
#### 3 - Working with events
* Events = Klickes usw.
* wird auch durch Angular-Templates gemacht
* templates/app.html
```html
<div class="card search">
  <h1 class="search-headline">Artist Directory</h1>
  <label class="search-label">search
    <span *ngIf="name">for: {{ name }}</span></label>
    <input class="search-input" #newArtist
      (keyup.enter)="addArtist(newArtist.value); newArtist.value=''"
      >
    <button class="btn"
      (click)="addArtist(newArtist.value); newArtist.value=''"
      >Add</button>
</div><!-- card search -->

<ul class="artistlist cf">
  <li class="artistlist-item cf"
    (click)="onClick($event)" 
    *ngFor="let item of artists">
    <h2 class="artist-name">{{ item.name }}</h2>
    <h3 class="artist-reknown">{{ item.school }}</h3>
  </li>
</ul>
```
* `(click)` - mit `()` Event angeben `=Funkt()` - welche Funktioen beim Event ausgeführt wird
* `#newArtist` - Temp Variable, die dann in Methoden bekannt ist, ist eigentlich der Variable, die das DOM-Element enthält
* `(keyup.enter)` - wenn man Enter klickt.
* component.app.ts
```js
import { Component } from '@angular/core';

@Component({
  selector: 'app',
  templateUrl: './partials/app.html' 
})

export class AppComponent {
  name: string;
  artists: any;

  onClick(e) {
      //console.log(e);
      //console.log(e.target);
      //console.log(e.target.innerHTML)
    this.name=e.target.innerHTML;
  }

  addArtist(value) {
    if (value!=='') {
      this.artists.push({
        name: value,
        school: 'Hard Knocks'
      });
    }
  }

  constructor() {
    this.name = 'Xhou Ta';
    this.artists = [
      {
        name: 'Barot Bellingham',
        school: 'Penn State'
      }, {
        name: 'Jonathan Ferrar',
        school: 'University of Illinois'
      }, {
        name: 'Hillary Post',
        school: 'University of Florida'
      } 
    ]
  }
}
```
#### 4 - Using properties
* component.app.ts
```ts

``import { Component } from '@angular/core';

@Component({
  selector: 'app',
  templateUrl: './partials/app.html' 
})

export class AppComponent {
  name: string;
  artists: any;

  onClick(myItem, myElement) {
    this.name=myItem.name;
    myElement.style.backgroundColor="#FECE4E";
  }

  addArtist(value) {
    if (value!=='') {
      this.artists.push({
        name: value,
        school: 'Hard Knocks'
      });
    }
  }

  constructor() {
    this.name = 'Xhou Ta';
    this.artists = [
      {
        name: 'Barot Bellingham',
        school: 'Penn State'
      }, {
        name: 'Jonathan Ferrar',
        school: 'University of Illinois'
      }, {
        name: 'Hillary Post',
        school: 'University of Florida'
      } 
    ]
  }
}
```

* templates/app.html
```html
<div class="card search">
  <h1 class="search-headline">Artist Directory</h1>
  <label class="search-label">search
    <span *ngIf="name"
      [innerHTML]="' for: ' +name"></span></label>
    <input class="search-input" #newArtist
      (keyup.enter)="addArtist(newArtist.value); newArtist.value=''"
      >
    <button class="btn"
      (click)="addArtist(newArtist.value); newArtist.value=''"
      >Add</button>
</div><!-- card search -->

<ul class="artistlist cf">
  <li class="artistlist-item cf"
    #artistContainer
    (click)="onClick(item, artistContainer)" 
    *ngFor="let item of artists">
    <h2 class="artist-name">{{ item.name }}</h2>
    <h3 class="artist-reknown">{{ item.school }}</h3>
  </li>
</ul>
```
* mit `[ ]` Eigenschaften an DOM-Element binden
+ mit `[innerHTML]` wird dem innerHTML von `<span>` der Wert von `comoponent.name` zugewiesen
* `[innerHTML]` = `bind-innerHTML`
#### 5 - Using two-way data binding
* templates/app.html


```html
<div class="card search">
  <h1 class="search-headline">Artist Directory</h1>
  <label class="search-label">search
    <span *ngIf="name"
      [innerHTML]="' for: ' +name"></span></label>
    <input class="search-input"
      #newArtist
      <!-- 
      [value]="name"
      (input)="name=$event.target.value"
      -->
      [(ngModel)]="name" 
      (keyup.enter)="addArtist(newArtist.value); newArtist.value=''"
      >
    <button class="btn"
      (click)="addArtist(newArtist.value); newArtist.value=''"
      >Add</button>
</div><!-- card search -->

<ul class="artistlist cf">
  <li class="artistlist-item cf"
    #artistContainer
    (click)="onClick(item, artistContainer)" 
    *ngFor="let item of artists">
    <h2 class="artist-name">{{ item.name }}</h2>
    <h3 class="artist-reknown">{{ item.school }}</h3>
  </li>
</ul>
```
* Element markieren, dass reagieren auf Events soll und Werte ändern soll
* nur Werte ändern`[value]="name"` - `<input value=""` wird geändert
* `(input)="name=$event.target.value"` - bei Event `input` wird `name=...` gesetzt <= auf Evnets reagieren 
* component.app.ts
* mit `([])` - doppelte Bindung realisieren = 1 (Tracking + Events) + Werte ändern
```ts
import { Component } from '@angular/core'; //

@Component({
  selector: 'app',
  templateUrl: './partials/app.html' 
})

export class AppComponent {
  name: string;
  artists: any;

  onClick(myItem, myElement) {
    this.name=myItem.name;
    myElement.style.backgroundColor="#FECE4E";
  }

  addArtist(value) {
    if (value!=='') {
      this.artists.push({
        name: value,
        school: 'Hard Knocks'
      });
    }
  }

  constructor() {
    this.name = 'Xhou Ta';
    this.artists = [
      {
        name: 'Barot Bellingham',
        school: 'Penn State'
      }, {
        name: 'Jonathan Ferrar',
        school: 'University of Illinois'
      }, {
        name: 'Hillary Post',
        school: 'University of Florida'
      } 
    ]
  }
}
```
* app.module.ts
```ts
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './component.app';

@NgModule({
  imports: [
    BrowserModule, FormsModule
  ],
  declarations: [
    AppComponent
  ],
  bootstrap: [
    AppComponent
  ]
})

export class AppModule {}
```
* FormsModule importieren
#### 6 - Adding CSS to a component
* component.app.ts
```ts
import { Component } from '@angular/core';

@Component({
  selector: 'app',
  templateUrl: './partials/app.html',
  // styles: [ ".btn {background-color: grenn;}"]
  /* styles: [ 
    ".btn {background-color: grenn;}",
    ".btn:hover {background-color: pink;}"
  ]
  */
  styleUrls: [ "./css/app.css" ] 
})

export class AppComponent {
  name: string;
  artists: any;

  onClick(myItem, myElement) {
    this.name=myItem.name;
    myElement.style.backgroundColor="#FECE4E";
  }

  addArtist(value) {
    if (value!=='') {
      this.artists.push({
        name: value,
        school: 'Hard Knocks'
      });
    }
  }

  constructor() {
    this.name = 'Xhou Ta';
    this.artists = [
      {
        name: 'Barot Bellingham',
        school: 'Penn State'
      }, {
        name: 'Jonathan Ferrar',
        school: 'University of Illinois'
      }, {
        name: 'Hillary Post',
        school: 'University of Florida'
      } 
    ]
  }
}
```
* templates/app.html
```html
<div class="card search">
  <h1 class="search-headline">Artist Directory</h1>
  <label class="search-label">search
    <span *ngIf="name"
      [innerHTML]="' for: ' +name"></span></label>
    <input class="search-input"
      #newArtist
      [(ngModel)]="name" 
      (keyup.enter)="addArtist(newArtist.value); newArtist.value=''"
      >
    <button class="btn"
      (click)="addArtist(newArtist.value); newArtist.value=''"
      >Add</button>
</div><!-- card search -->

<ul class="artistlist cf">
  <li class="artistlist-item cf"
    #artistContainer
    (click)="onClick(item, artistContainer)" 
    *ngFor="let item of artists">
    <h2 class="artist-name">{{ item.name }}</h2>
    <h3 class="artist-reknown">{{ item.school }}</h3>
  </li>
</ul>
```
* CSS-Styles hinzufügen -> in component.app.ts
* Vorteil: CSS-Style wird nur geladen, wenn Component gealden wird.
```ts
```
### 3 - Creating Modules
#### 1 - Using more complex data
* templates/app.html
```html
<div class="card search">
  <h1 class="search-headline">Artist Directory</h1>
  <label class="search-label">search
    <span *ngIf="query"
      [innerHTML]="' for: ' + query"></span></label>
    <input class="search-input"
      [(ngModel)]="query" placeholder="type in search term here">
</div><!-- card search -->

<ul class="artistlist cf">
  <li class="artistlist-item cf"
    *ngFor="let item of artists">
    <img class="artist-img" 
      src="images/{{item.shortname}}_tn.jpg"
      alt="{{item.name}} photo">
    <div class="artist-info">
      <h2 class="artist-name">{{ item.name }}</h2>
      <h3 class="artist-reknown">{{ item.reknown }}</h3>
    </div>
  </li>
</ul>
```
* 
* componente.app.ts
```ts
import { Component } from '@angular/core';

//Klasse für Komplexe Daten
export class Artist {
  name: string;
  shortname: string;
  reknown: string;
  bio: string;
}

@Component({
  selector: 'app',
  templateUrl: './partials/app.html',
  styleUrls: [ "./css/app.css" ] 
})

export class AppComponent {
  artists = ARTISTS; //die Konstante wird einer KlassenVar zugewiesen
  currentArtist: Artist;
}

//Konstante ARTISTS
var ARTISTS: Artist[] = [
  {
    "name":"Barot Bellingham",
    "shortname":"Barot_Bellingham",
    "reknown":"Royal Academy of Painting and Sculpture",
    "bio":"Barot has just finished his final year at The Royal Academy of Painting and Sculpture, where he excelled in glass etching paintings and portraiture. Hailed as one of the most diverse artists of his generation, Barot is equally as skilled with watercolors as he is with oils, and is just as well-balanced in different subject areas. Barot's collection entitled \"The Un-Collection\" will adorn the walls of Gilbert Hall, depicting his range of skills and sensibilities - all of them, uniquely Barot, yet undeniably different"
  }, {
    "name":"Jonathan G. Ferrar II",
    "shortname":"Jonathan_Ferrar",
    "reknown":"Artist to Watch in 2012",
    "bio":"The Artist to Watch in 2012 by the London Review, Johnathan has already sold one of the highest priced-commissions paid to an art student, ever on record. The piece, entitled Gratitude Resort, a work in oil and mixed media, was sold for $750,000 and Jonathan donated all the proceeds to Art for Peace, an organization that provides college art scholarships for creative children in developing nations"
  }, {
    "name":"Hillary Hewitt Goldwynn-Post",
    "shortname":"Hillary_Goldwynn",
    "reknown":"New York University",
    "bio":"Hillary is a sophomore art sculpture student at New York University, and has already won all the major international prizes for new sculptors, including the Divinity Circle, the International Sculptor's Medal, and the Academy of Paris Award. Hillary's CAC exhibit features 25 abstract watercolor paintings that contain only water images including waves, deep sea, and river."
  }
]
```
* die komplexen Daten werden per eine Klasse `Artist` festgelegt. 
  * wobie die Werte für als Konstante hier festgelegt werden.
#### 2 - Creating a subcomponent
* templates/app.html
```html
<div class="card search">
  <h1 class="search-headline">Artist Directory</h1>
  <label class="search-label">search
    <span *ngIf="query"
      [innerHTML]="' for: ' + query"></span></label>
    <input class="search-input"
      [(ngModel)]="query" placeholder="type in search term here">
</div><!-- card search -->

<ul class="artistlist cf">
  <li class="artistlist-item cf"
    *ngFor="let item of artists">
    <artist-item class="content" [artist]=item></artist-item>
  </li>
</ul>
```
* `<artist-item class="content" [artist]=item>` - hier wird Selektor für neue Komponente eingefügt
* `[artist]=item` - ist der input den component-item erwartet.
* templates/artist-item.html
```html
<img class="artist-img" 
  src="images/{{artist.shortname}}_tn.jpg"
  alt="{{artist.name}} photo">
<div class="artist-info">
  <h2 class="artist-name">{{ artist.name }}</h2>
  <h3 class="artist-reknown">{{ artist.reknown }}</h3>
</div>
```
* hier wird auch `artist` benutzt
* component.app.ts
```ts
import { Component } from '@angular/core';
import { ArtistItemComponent } from './component.artist-item';

export class Artist {
  name: string;
  shortname: string;
  reknown: string;
  bio: string;
}

@Component({
  selector: 'app',
  templateUrl: './templates/app.html',
  styleUrls: [ "./css/app.css" ] 
})

export class AppComponent {
  artists = ARTISTS;
  currentArtist: Artist;
}

var ARTISTS: Artist[] = [
  {
    //
  }
]
```
* component.artist-item.ts
```ts
import { Component } from '@angular/core';

@Component({
  selector: 'artist-item',
  templateUrl: 'templates/artist-item.html',
  styleUrls: ['css/artist-item.css'],
  inputs: ['artist']
})

export class ArtistItemComponent {}
```
* ArtistItem-Component in Root-Component einfügen 
* `selector: 'artist-item',` ist Selector-Tab in `index.html`
* `inputs: ['artist']` - wenn man neue Componente mit Eingaben/Info füttern, muss man es hier sagen
* <- macht eigentlich nichts, nur um HTML-Temlate und CSS zu servieren.
* app.modules.ts
```ts
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './component.app';
import { ArtistItemComponent } from './component.artist-item';

@NgModule({
  imports: [
    BrowserModule, FormsModule
  ],
  declarations: [
    AppComponent, ArtistItemComponent
  ],
  bootstrap: [
    AppComponent
  ]
})

export class AppModule {}
```
* die Componte bekannt machen
* diese Teilung in mehrere Component => leichter zu Maintainen
#### 3 - Using multiple subcomponents
* component.artist-details.ts
```ts
import { Component } from '@angular/core';

@Component({
  selector: 'artist-details',
  templateUrl: 'templates/artist-details.html',
  styleUrls: ['css/artist-details.css'],
  inputs: ['artist']
})

export class ArtistDetailsComponent {}
```

* app.module.ts - die Subcomponente einfügen
```ts
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './component.app';
import { ArtistItemComponent } from './component.artist-item';
import { ArtistDetailsComponent } from './component.artist-details';

@NgModule({
  imports: [
    BrowserModule, FormsModule
  ],
  declarations: [
    AppComponent, ArtistItemComponent, ArtistDetailsComponent
  ],
  bootstrap: [
    AppComponent
  ]
})

export class AppModule {}
```
* templates/artist-detail.html
```html
<section class="card artist-details">
    <h1 class="artist-name">{{artist.name}}</h1>
    <div class="info">
      <h3 class="artist-reknown">{{artist.reknown}}</h3>
      <img class="artist-img" src="images/{{artist.shortname}}_tn.jpg" alt="{{artist.name}}">
      <div class="artist-longbio">{{artist.bio}}</div>
    </div><!--info-->
</section><!--artistdetails-->
```
* templates/app.html - weiteren Selektor für artist-detail.html einfügen
```html
<div class="card search">
  <h1 class="search-headline">Artist Directory</h1>
  <label class="search-label">search
    <span *ngIf="query"
      [innerHTML]="' for: ' + query"></span></label>
    <input class="search-input"
      [(ngModel)]="query" placeholder="type in search term here">
</div><!-- card search -->

<ul class="artistlist cf"
  *ngIf="query">
  <li class="artistlist-item cf"
    (click)="showArtist(item); query=''"
    *ngFor="let item of artists">
    <artist-item class="content" [artist]=item></artist-item>
  </li>
</ul>

<artist-details 
  *ngIf="currentArtist"
  [artist]="currentArtist"></artist-details>
```
* <- mit `ngIf` sagt man nur wenn currentArtitst einen Wert hat den Wert dem `[artist]` zuweisen.
* <- `(click)="showArtist(item); query=''"` Klick-Event anlegen, damit artist-detail getriggert wird.
* component.app.ts
```ts
import { Component } from '@angular/core';
import { ArtistItemComponent } from './component.artist-item';

export class Artist {
  name: string;
  shortname: string;
  reknown: string;
  bio: string;
}

@Component({
  selector: 'app',
  templateUrl: './partials/app.html',
  styleUrls: [ "./css/app.css" ] 
})

export class AppComponent {
  artists = ARTISTS;
  currentArtist: Artist;

  showArtist(item) {
    this.currentArtist = item;
  }
}

var ARTISTS: Artist[] = [
  {
    //
  }
]
```
#### 4 - Filtering content through data pipes
* Filer = Pipes
* Pipe = nimmt Daten an als Input und modifizeirt sie
  * API Ref -> Pipes checken

* template/aritst-item.html
```html
<img class="artist-img" 
  src="images/{{artist.shortname}}_tn.jpg"
  alt="{{artist.name}} photo">
<div class="artist-info">
  <!-- <h2 class="artist-name">{{ artist.name | uppercase}}</h2> --> 
  <h2 class="artist-name">{{ artist.name }}</h2>
  <h3 class="artist-reknown">{{ artist.reknown }}</h3>
</div>
```
* `<h2 class="artist-name">{{ artist.name | uppercase}}</h2>` - uppercase-Pipe nutzen
* man kann eigene Pipes-Bilden
* pipe.search.ts
```ts
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'search'
})

export class SearchPipe implements PipeTransform {
  transform(pipeData, pipeModifier) {
    return  pipeData.filter((eachItem)=> {
    return  eachItem['name'].toLowerCase().includes(pipeModifier.toLowerCase()) ||
            eachItem['reknown'].toLowerCase().includes(pipeModifier.toLowerCase());
    });
  }
}
```
+ hier wird `@Pipe`-dekorator benutzt
  * `.filer()` ist JS-Methode
  * in `filter()` ist eigentlich JS.
* app.modules.ts - die eigene Pipe bekannt machen
```ts
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './component.app';
import { ArtistItemComponent } from './component.artist-item';
import { ArtistDetailsComponent } from './component.artist-details';

import { SearchPipe } from './pipe.search';

@NgModule({
  imports: [
    BrowserModule, FormsModule
  ],
  declarations: [
    AppComponent, ArtistItemComponent, ArtistDetailsComponent, SearchPipe
  ],
  bootstrap: [
    AppComponent
  ]
})

export class AppModule {}
```
* templates/app.html - die Pipe anwenden
```html
<div class="card search">
  <h1 class="search-headline">Artist Directory</h1>
  <label class="search-label">search
    <span *ngIf="query"
      [innerHTML]="' for: ' + query"></span></label>
    <input class="search-input"
      [(ngModel)]="query" placeholder="type in search term here">
</div><!-- card search -->

<ul class="artistlist cf"
  *ngIf="query">
  <li class="artistlist-item cf"
    (click)="showArtist(item); query=''"
    *ngFor="let item of (artists | search: query)">
    <artist-item class="content" [artist]=item></artist-item>
  </li>
</ul>

<artist-details 
  *ngIf="currentArtist"
  [artist]="currentArtist"></artist-details>
```
+ eventuell wurden die Angular-Pipes entfernt => muss man dann für alles eigene Pipe erstellen.