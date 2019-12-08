import { NgModule } from '@angular/core'; //NgModul importieren aus angular/core, mit Komma kann man mehrere Module einfügen 
import { BrowserModule } from '@angular/platform-browser'; //um mit DOM arbeiten zu können
import { AppComponent } from './app.component'; //wird die StartComponente, muss noch erstellt werden

//@NgModule-Decorator = man sagt damit das folgende Klasse ein Angular-Modul ist
@NgModule({
    imports: [ //weitere Module/Imports, das dann mein Modul (AppModul) bracht
        BrowserModule
    ],
    declarations: [ //Direktiven, Componenten, Pipes available für eigenen Modul/AppModul machen 
        AppComponent
    ],
    bootstrap: [
        AppComponent
    ] //für Root-Modul
}) //was auf den Code danach angewendent werden soll; imports, declarations, bootstrap = Eigenschaften die AppModule benutzt werden sollen
export class AppModule { } //export = sowas wie public