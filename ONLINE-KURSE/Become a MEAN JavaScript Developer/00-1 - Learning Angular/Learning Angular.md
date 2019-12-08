### 0 - Introduction
* Hier wird Bootstrap, JS, und npm benutzt
* Code ist auf https://github.com/planetoftheweb/learnangular5 -> Videos = Branch; (e = Ende)
* nodeJS installieren + git installieren
### 1 - Using the Angular CLI
#### 1 - What is Angular
* ist Framework um Apps zu bilden
    + AngulerJS
    + Angular (momentan 5)
* Prinzip:
    * Componenten erstellen
    * diese zusammenstellen
    * Jede Componente kann aus eigenen
        * Templates
        * Scripts
        * CSS
* ist Modulares Frames d.h man lädt nur die Module, die man braucht
* Features
    * Data binding = wie man Templates/Views und Modele/Daten zusammenstellen
    * Templates (HTML)
    * CLI 
#### 2 - Using the Angular CLI
* = Angular CLI installieren
* braucht Node.js und git
* `ng` - Angular-CLI aufrufen
    * `ng new NAME` - App/Project erstellen = Ordner erstellung + alle benötigten Dateien darein kopieren
    * `ng serve` - App in Dev-Modus starten
    * `ng build` - Dateien erstellen für Deployment, die man dann zum Server pushed
    * `ng g TYPE NAME` - Angular Code generieren
* Installieren:
    * `npm install -g @angular/cli`
    * `ng new myAppName`
        * `ng` dann im myAppName ausführen
    * `ng serve` - im myAppName ausführen
        * `ng server --open` - öffnent den Browser
    * `ng build` - es wird neues Ordner erstellt **dist**, denn man dann zum Server pushed
#### 3 - Understanding Angular CLI projects
* `angular-cli.json` - Config für CLI und Project
    * `root` 
    * `outDir` - **dist** umändern
    * `scripts` - hier dann eigene Scripts ablegen
* `editorconfig` - wie die Project-Dateien editiert werden (z.B. auch Editor)
* `src/app` - hier wird dann der eigene Code abgelegt
* `src/assets` - kann man eventuell löschen
* `src/environments` - Dateien für `ng server/build` + Dateien für Tests usw.
* `src/main.ts` - erste Datei, die dann geladen wird, die dann weitere Module lädt => muss geändert werden
#### 4 - Using CLI generated components
* `main.ts` - lädt alles in die App. Man sollte es so stehen lassen. Importiert wichtige Teile (Angular-Libs)
  * oben sind globale Imports
  * darunter sind di lockalen Imports
* `environent` - für Developement
* `import ...` - Module/Angular-Features importieren
    * `import {AppModule} from './app/app.module` lädt die Klasse/Funktioen/Modul aus **app/app.module.ts**
    * `platformBrowserDynamic().bootsrapModule(AppModule)`- steht in *main.ts* und die Funktion `bootstrapModule(AppModule)` lädt das Modul
* es gibt *Module* und *Componenten*
* app.module.ts - Parameter für App setzen + Logic für App. 
* `export` = Klasse public machen, damit sie von anderen Module benutzt werden kann.
#### 5 - Installing additional frameworks
* in `pacakges.json` steht alles was installiert ist
* Bootstrap + jQuery installieren
    * in myApp-Order gehen
    * `npm install jquery --save-dev` - als Dev Dependensy installieren
    * `npm install bootstrap@4.0.0-beta.2 --save-dev`
    * im *node_modules* wird bootstrap- und jquery-Order erscheinen
    * dann in **angular-cli.json* für Boostrap in `styles:` einfügen und Bootstrap + eventuell Popper.js (für Bootstrap) und jQuery in `scripts:` einfügen. (Pfad lokal)
        * `../node_modules/...`
### 2 - Getting Started
#### 1 - Understanding templates in Angular
* `templateUrl` im Decorator = Verweis auf 
* `template` - direkt html schreiben
```javascript
import { Component } form '@angular/core";
@Component({
    selector: 'app-root',
    templateUrl: './app.component.html', //oder template: '<h1>Lala</h1>' oder `<h1>Lala</h1>` für MultiLines
    styleUrls: ["./app.component.css"]
})
export class AppComponent{
    title = "my app";
}
```
```html
<div class="row justify-content-center">
  <div class="card mt-sm-3 col-md-8">
    <div class="card-body">
      <h3 class="mb-0">Artist Directory</h3>
      <div class="form-group">
        <div class="form-label"></div>
        <input class="form-control mt-2" type="text">
      </div><!-- form-group -->
    </div><!-- card-body -->
  </div><!-- card -->
</div><!-- row -->
```
* `styleUrls` oder `style` werden nur auf Code der Componente angewendet
#### 2 - Binding data to templates
* Data Binding Feature benutzen
    * {{ VAR }} - Ausdruck. Variable oder kompolexe Ausdrucke. 
    * Directiven = eigentlich Befehle
    * `constructor()` benutzen um Variablen im der Componente zu initialisieren
* 
```ts
import { Component } form '@angular/core";
@Component({
    selector: 'app-root',
    templateUrl: './app.component.html'
    styles: [
      `.list-group-item:first-child{
          border-top-left-radius: 0;
          border-top-right-radius: 0;
          border-top: 0;
        }
      `       `
    ]
})
export class AppComponent{
    query: string; //Varibble query vom Typ string
    artists: object; //oder any

    constructor(){
        this.query = "Barot";
        this.artists = [{"name": "Artist01, "shortname" : "Art01"}, {"name": "Artist02", "shortname": "Art02}]
    }
}
```
```html
<div class="position-relative container"> 
    <div class="row justify-content-center">
        <div class="card mt-sm-3 col-md-8">
            <div class="card-body">
            <h3 class="mb-0">Artist Directory</h3>
            <div class="form-group">
                <div class="form-label">
                    <strong>For:</strong>
                    {{ query + "--" }}
                </div>
                <input class="form-control mt-2" type="text">
            </div><!-- form-group -->
            </div><!-- card-body -->
        </div><!-- card -->
    </div><!-- row -->

    <div class="position-absolute container" style="left: 0; z-index:10">
    <div class="row justify-content-center">
      <div class="col-sm-10 col-md-8 col-lg-6 col-xl-5">
        <div class="list-group">
          <a href="#" class="list-group-item list-group-item-action flex-column align-items-start"
            *ngFor="let artist of artists"> <!-- das ist Angular Directive, Directiven beginnen mit * -->
              <div class="media">
                <div class="media-body align-self-center">
                  <h5 class="m-0">{{ artist.name }}</h5>
                  {{ artist.shortname }}
                </div><!-- media body -->
              </div><!-- media -->
          </a><!-- link -->
        </div><!-- list-group -->
      </div><!-- col -->
    </div><!-- row -->
  </div><!-- container -->


</div> <!-- position -->
```
* `*ngFor="let artist of artists"` - mit ngFor wird durch alle inner HTML-Elemente durchgelaufen und dort die Variable `artist` anwendet, bis `artists` keine Elemente mehr hat, wobei die artist-Var für das HTML-Element gespiechert wird und kann dann als Parameter übergeben werden.
#### 3 - Working with events
* Events an Componente bidnen
* `( EVT-Name )` 
* Dieses ENT dann an eine Methode der Componte binden
* `$event` - Variable, die dann Event-Info beeinhaltet => der Methode als Parameter übergeben
  * man kann auch weitere Parameter übergeben
```javascript
import { Component } form '@angular/core";
@Component({
    selector: 'app-root',
    templateUrl: './app.component.html'
    styles: [
      `
      .list-group-item:first-child {
          border-top-left-radius: 0;
          border-top-right-radius: 0;
          border-top: 0;
      }
      `       `
    ]
})
export class AppComponent{
    query: string; //Varibble query vom Typ string
    artists: object;

    showArtist(e, item){
        console.log(e);
        this.query = item.name;
    }

    constructor(){
        this.query = "Barot";
        this.artists = [{"name": "Artist01, "shortname" : "Art01"}, {"name": "Artist02", "shortname": "Art02}]
    }
}

```
```html
<div class="position-relative container"> 
    <div class="row justify-content-center">
        <div class="card mt-sm-3 col-md-8">
            <div class="card-body">
            <h3 class="mb-0">Artist Directory</h3>
            <div class="form-group">
                *ngIf="query"<div class="form-label"> <!--heißt wenn query-Var existiert und nicht leer ist, wird dieses HTML-Elem angezeigt  -->
                    <strong>For:</strong>
                    {{ query + "--" }}
                </div>
                <input class="form-control mt-2" type="text">
            </div><!-- form-group -->
            </div><!-- card-body -->
        </div><!-- card -->
    </div><!-- row -->

    <div class="position-absolute container" style="left: 0; z-index:10">
    <div class="row justify-content-center">
      <div class="col-sm-10 col-md-8 col-lg-6 col-xl-5">
        <div class="list-group">
          <a href="#" class="list-group-item list-group-item-action flex-column align-items-start"
            ngFor="let artist of artists" (click)="showArtist($event, artist)"> <!-- das ist Angular Directive, Directiven beginnen mit * -->
              <div class="media">
                <div class="media-body align-self-center">
                  <h5 class="m-0">{{ artist.name }}</h5>
                  {{ artist.shortname }}
                </div><!-- media body -->
              </div><!-- media -->
          </a><!-- link -->
        </div><!-- list-group -->
      </div><!-- col -->
    </div><!-- row -->
  </div><!-- container -->
</div> <!-- position -->
```
* `(click)="showArtist($event, artist)"` - Click-Event hinzufügen
#### 4 - Using properties
* Eigenschafte von HTML-Elem ändern
    * [ PROP-Name ] <- ist Angular - Derective
    * ähnlich wie Ausdrücke
* images kann dann in `assets/images` ablegen.
```
import { Component } form '@angular/core";
@Component({
    selector: 'app-root',
    templateUrl: './app.component.html'
    styles: [
        `
            .list-group-item:first-child {
                border-top-left-radius: 0;
                border-top-right-radius: 0;
                border-top: 0;
            }
        ``
    ]
})
export class AppComponent{
    query: string; //Varibble query vom Typ string
    artists: object;

    showArtist(e, item){
        console.log(e);
        this.query = item.name;
        item.highlight = !item.highligt
    }

    constructor(){
        this.query = "Barot";
        this.artists = [{"name": "Artist01, "shortname" : "Art01"}, {"name": "Artist02", "shortname": "Art02}]
    }
}
```

```html
<div class="position-relative container">
  <div class="row justify-content-center">
    <div class="card mt-sm-3 col-md-8">
      <div class="card-body">
        <h3 class="mb-0">Artist Directory</h3>
        <div class="form-group">
          <div class="form-label" *ngIf="query"><strong>For:</strong>
            {{ query }}
          </div>
          <input class="form-control mt-2" type="text">
        </div><!-- form-group -->
      </div><!-- card-body -->
    </div><!-- card -->
  </div><!-- row -->

  <div class="position-absolute container" style="left: 0; z-index:10">
    <div class="row justify-content-center">
      <div class="col-sm-10 col-md-8 col-lg-6 col-xl-5">
        <div class="list-group">
          <a href="#" class="list-group-item list-group-item-action flex-column align-items-start"
            *ngFor="let artist of artists"
            (click)="showArtist(artist)"
            [style.backgroundColor]="artist.highlight ? '#EEE' : '#FFF'"> <!-- mit dieser Property CSS per JS ändern; wird geändert, wenn artist gewählt wird. -->
              <div class="media">
                <img class="mr-3 rounded align-self-center img-fluid" 
                  style="width:70px;" [src]="'./assets/images/' + artist.shortname + '_tn.jpg'" alt="{{ 'Photo of ' + artist.name }}"> <!-- es wird mit [src] statt mit src benutzt = Benutzung von Properties -->
                <div class="media-body align-self-center">
                  <h5 class="m-0">{{ artist.name }}</h5>
                  {{ artist.reknown }}
                </div><!-- media body -->
              </div><!-- media -->
          </a><!-- link -->
        </div><!-- list-group -->
      </div><!-- col -->
    </div><!-- row -->
  </div><!-- container -->

</div><!-- position -->
```
#### 5 - Working with two-way data binding
* Binding Data + Property um HTML-Elem zu ändern
* bei Forms oft benutzt
    * `[( ngModel )]` - für Form-Teile, die sind `<input>`
    * `[( ngControl )] - für Form-Teile, die nicht `<input>` sind
* app.module.ts ändert umd ngModule einzufügen:
```ts
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';


@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule, FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
```
* app.component.html anpassen
```html
<div class="position-relative container">
  <div class="row justify-content-center">
    <div class="card mt-sm-3 col-md-8">
      <div class="card-body">
        <h3 class="mb-0">Artist Directory</h3>
        <div class="form-group">
          <div class="form-label" *ngIf="query"><strong>For:</strong>
            {{ query }}
          </div>
          <input class="form-control mt-2" type="text"
            [(ngModel)]="query">
        </div><!-- form-group -->
      </div><!-- card-body -->
    </div><!-- card -->
  </div><!-- row -->

  <div class="position-absolute container" style="left: 0; z-index:10">
    <div class="row justify-content-center">
      <div class="col-sm-10 col-md-8 col-lg-6 col-xl-5">
        <div class="list-group">
          <a href="#" class="list-group-item list-group-item-action flex-column align-items-start"
            *ngFor="let artist of artists"
            (click)="showArtist(artist)"
            [style.backgroundColor]="artist.highlight ? '#EEE' : '#FFF'">
              <div class="media">
                <img class="mr-3 rounded align-self-center img-fluid" 
                  style="width:70px;" [src]="'./assets/images/' + artist.shortname + '_tn.jpg'" alt="{{ 'Photo of ' + artist.name }}">
                <div class="media-body align-self-center">
                  <h5 class="m-0">{{ artist.name }}</h5>
                  {{ artist.reknown }}
                </div><!-- media body -->
              </div><!-- media -->
          </a><!-- link -->
        </div><!-- list-group -->
      </div><!-- col -->
    </div><!-- row -->
  </div><!-- container -->

</div><!-- position -->
```
### 3 - Working with Components
#### 1 - Using lifecycle methods
#### 2 - Creating subcomponents
#### 3 - Filtering content 
#### 4 - Adding subcomponents