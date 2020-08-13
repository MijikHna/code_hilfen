# 4 - Angular Grundkurs - Dependency Injection, Directiven Bindungen

## 1

* die Übung ist in Branchens organisiert.
* <https://github.com/netTrek/LinkedIn_Angular_Vertiefung>
* eventuell bei Angular updates die Angular-Update-Seite besuchen und Hinweise durchlesen

## 2 - Grunlagen zu Direktiven

### 1 - Was ist Direktive

* Funktionserweiterung für HTML-Element
* werden in HTML-Elementen als HTML-Elemente eingetragen
* zwei Typen
  1. strukturelle Direktiven = manipuliert den DOM -> fangen mit `*` an. Bsp: `<img *ngIf="showImg">` - zeigt `<img>` nur an wenn `showImg=true` ist, wobei man statt `showImg` direkt einen Vergleich machen kann
  2. Attribut-Direktive = Aussehen + Verhalten des HTML-Elem manipulieren

### 2 - Wie wendet man Direktiven an
* Bsp1: `<input matInput>` = hier ist `matInput`-Attribut = Direktive
* Bsp2: `<textarea matAutosizeMinRows="2">` - Attr-Direktive mit Wertzuweisung. `matAutosizeMinRows`-Direktive von Material-Design = Textarea 2 Zeile groß sein soll.
* Bsp3: `<input [ngClass]="inputClass">` - Attr-Direktive mit gebundener Wertzuweisung = Wertzuweisung über eine Bindung. `[]` represäntieren eine Bindung einer Eigenschaft

## 3 - Hauseigene Direktiven nutzen

### 1 - ngIf

### 2 - ngTemplate mit ngIf

### 3 - ngifElse

### 4 - ngFor

### 5 - ngFor Variables

### 6 - ngTemplate mit ngFor

### 7 - ngSwitch

### 8 - ngContainer mit ngSwitch

### 9 - ngClass

### 10 - ngStyle

## 4 - Direktiven erstellen und nutzen

### 1 - Direktiven erzeugen

### 2 - Direktiven über CLI anlegen

### 3 - Elements mit Direktiven erweitern

### 4 - Direktiven-Werte übermitteln

### 5 - Direktiven mit HostBindings

### 6 - Strukturelle Direktiven erstellen

## 5 - Grundlagen zu Pipes

### 1 - Was ist eine Pipe

### 2 - Pipes in HTML anwenden

### 3 - Pipes via JS anwenden

### 6 - Lower-& UpperCasePipe
#### 1 - Lower- & UpperCasePipe
#### 2 - CurrencyPipe
#### 3 - Locale
#### 4 - DecimalPipe
#### 5 - PercentPipe
#### 6 - DatePipe
#### 7 - SlicePipe
#### 8 - JsonPipe

### 7 - Pipes erstellen und nutzen
#### 1 - Pipe erstellen
#### 2 - ReversePipe via CLI
#### 3 - pure

### 8 - Grundlagen zur Dependency Injection
#### 1 - Dependency Injection in der Angular-Welt
#### 2 - Vorhanden Services nutzen

### 9 - Provider nutzen
#### 1 - Eigene Services bereitstellen
#### 2 - Werte bereitstellen
#### 3 - Multi-Option
#### 4 - Klasseninstanz bereitstellen
#### 5 - Bereitstellung "konkatieren"
#### 6 - Bereitstellung über Factory-Methode
#### 7 - Injectable Decorator seit Angular 6

### 10 - Tipps zur Dependency Injection
#### 1 - Token Injection
#### 2 - Der LOCALE_ID-Token
#### 3 - Host-, Self- und Optional Decorator