### Teil 1: How to install your first App with Angular CLI
* https://www.freecodecamp.org/news/angular-9-for-beginners-how-to-install-your-first-app-with-angular-cli/

* Framework von Google
* muss man kennen:
    1. HTML, CSS
    2. JS/ES6
    3. TS
* Framework = hat eigne Funktionalität und Bibliotheken, hat eigene Reglen => bietet wenig Flexibilität an.
* Angular CLI = für automatische Operationen im Angular Projekt. Benutzt für:
    1. Configurations, Environment Setup
    2. Components, Services, Routing System bilden
    3. Start, Test, Deployment des Projekts 
    4. 3rd party Libs installieren
* Vorgehen:
    1. NPM installieren
    2. Angular CLI installieren `npm install -g @angular/cli` + `ng v`
    3. Angular Proj. erstellen: `ng new proj-name`
    4. App starten: `ng serve -- open`

### Teil 2: Angular Components and String Interpolatin
* https://www.freecodecamp.org/news/angular-9-for-beginners-components-and-string-interpolation/

Momentan werden UIs der Webseites mit component-based Rangehensweise erstellt. Fast alle modernen Framework bieten es an. 
* Was ist Component: Basis Building Block von Angular App (LEGO). Also man kann Komponente ein Mal erstellen und in verschiedenen Teilen des Proj. benutzen.
    * Angular Komponente besteht aus drei Teilen:
        1. HTML Template = View
        2. TS File = Model
        3. CSS File = Styling 
* Componenten teilen UI in kleinere Teile:
    1. View Data
    2. Render Data
* Componente sollte nicht in Task wie HTML-Requests, Service Operationen, Routing usw. involviert werden => Code clean, + View von andreren Teilen getrennt + Code ist kleiener und reusable
* Vorgehen:
    1. Angular Componente erstellen: `ng g c component-name` = erstellt neue Componente (= HTML, CSS, TS-File)
    ```ts
    // ...
    import { AppComponent } from './app.component';

    @NgModule({
        declarations: [
            AppComponent
        ],
        imports: [
            BrowserModule
        ],
        providers: [],
        bootstrap: [AppComponent]
    })

    export class AppModule{}
    ```
    2. In Angular muss man jedes **Serivce**, **Component** und **Module** im **Module**-Datei registrieren.
    ```ts
    import { Component } from '@angualar/core';

    @Component({ // Decorator markiert Klasse als Component + erlaubt weitere Metadaten hinzuzufügen
        selector: 'app-root',
        templateUrl: './app.component.html',
        styleUrls: ['./app.component.css'] 
    })

    export class AppComponent{

    }
    ```

* String Interpolation: `{{ data }}` = Component Render Data

### Teil 3: Angular Directives & Pipes
* https://youtu.be/3-eJ-A9rFEU
### Teil 4: One-Way Data Binding in Angular
* https://youtu.be/x_vtX3vvE8k

### Teil 5: Angular Two-Way Data Binding with ngModel
* https://youtu.be/bKfbzpANUFE