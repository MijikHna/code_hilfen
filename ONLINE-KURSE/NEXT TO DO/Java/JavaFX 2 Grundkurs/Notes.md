### 1 Einleitung und Grundlagen
#### 1 - Die Welt von Java und JavaFX
* man kann in der Doku nach JavaFX-Architektur schauen.
#### 2 - Was benötigt wird
* Java JDK
* JavaFX SDK
* IDE
* SceneBuilder
#### 3 - Die JavaFX-Doku
* JavaFX Doku: https://www.oracle.com/technetwork/java/javase/documentation/javafx-docs-2159875.html
#### 4 - JavaFX-Standardbeispiele
#### 5 - Die erste JavaFX-app
* JavaFX-Projekt erstellen
    * wird ein Hello World - GUI-Projekt erstellt
#### 6 - Eine erste JavaFX mit FXML
* bei Projekt JavaFXML-Projekt auswählen
#### 7 - JavaFX mit Eclipse
* einfaches Java-Projekt
* Klasse erstellen `JavaFX-HelloWorld`
* Code copy-pasten, den Netbeans-JavaFX für main-Klasse erstellt
* eventuell Libraries einstellen d.h.
    * Add external JARs die jfxrt.jar hinzufügen
#### 8 - Das Deployment
* drei Techniken (JavaFX Laufumgebung muss installiert sein)
    1. Ordner `dist` nach Build wird erstellen
        1. in diesem Ordner gibt es dann .html Datei => man kann dann diese JavaFX-App über diese .html Datei im Browser öffnen
        2. .jnlp-Datei ausführen ist in xml-Sprache = Java-Web-Start
        3. .jar-Datei ausführen
### 2.1 - FXML und der JavaFX Scene Builder
#### 1 - Eine JavaFX-Applikation mit FXML
* Übung: **JavaFXFXMLTest**
* = ohne Java sonder mit XML-ähnlicher Sprache
* FXML-Datei wird von SceneBuilder befüllt
* man kann diese FXML-Datei auch mit IDE-Intellisence-Hilfe einigermaßen gut befüllen.
* diese FXML-Datei von Java-App mit `FXMLLoader.load(getClass().getResource('lala.fxml'));` geladen
* Vorgehen (Hier IDE: NetBeans)
    1. New Project
    2. JavaFX Datei
    3. Namen eingeben/anpassen
        1. xxx.fxml = Aussehen
        ```xml
        <?xml verion="1.0" enconding="UTF-8"?>

        <?import java.lang.*?>
        ...

        <AnchorPane id="AnchorPane" ...>
            <children> <!-- Kiner von AnchorPane -->
                <Button layoutX="125", ..., onAction="#handleButtonAction", fx:id="button" />
                ...
            </children>
        </AnchorPane>
        ```
        * IDE unterstützt etwas beim fxml erstellen
        * 
        2. xxxController.java = hier werden dann Events programmiert
        3. ProjectName.java = hier sind dann die Initialisierung + main für JavaFX-App
        ```java
        public class JavaFXFXMLTest extends Application {
            @Override
            public void start(Stage stage) throws Exception {
                Parent root = FXMLLoader.load(getClass().getResource("GUI.fxml"));
                
                Scene scene = new Scene(root);
                
                stage.setScene(scene);
                stage.show();
            }
        }
        ```
#### 2 - Der Scene Builder
* alle Properties/Layout in .fxml kann man in SceneBuilder einstellen
+ Layout eher mit Container in Verbindung
* Code = welche Methode wird aufgerufen wird, wenn z.B auf auf Button geklickt wird
* Library:
    1. Container
    2. Controls = eigentliche Elemente
    3. Menu Content
    4. Shapes -> sind an Canvas-Technologie orientiert
    5. Charts
#### 3 - Eine Oberfläche mit Containern strukturieren
* Container sind etwas aus java-awt Layout-Manager abgeleitet
#### 4 - CSS beim Scene Builder
* Übung: **JavaFXCSS**
* dem Project eine CSS-Datei hinzufügen
    * Rechtklick auf root-Ordner
    * New 
    * StyleSheet
* im ScneneBuiler bei Properties kann man dann diese Datei der GUI zuweisen
    * dem GUI-Element dann die ID/Klasse zuweisen
* Aufpassen: die CSS-Eigenschaften können von HTML-Eigenschaften abweichen
* Bsp:
```css
.root {
    display: block;
    /*background-color: red;*/
    -fx-background-color: red;
}
```
* diese Präfixe (z.B -fx-, -webkit, -moz) sind spzielle Eigenschfaten, die aus speziele Engines angepasst sind.
    * es weichen aber nicht alle Eigenschaften ab (siehe JavaFX-Doku) 
### 2.2 - GUI-Erstellung auf Java-Ebene
#### 1 - Application, Scene und Stage
* Übung: **JavaFXHalloWelt
```java JavaFXHalloWelt.java
package javafxhallowelt;

import javafx.application.Application; //hier ist die Basis-Klasse für JavaFX-App
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;

public class JavaFXHalloWelt extends Application { //jede JavaFX-App ist Unterklasse von Application (ist abstrakte Klasse)
    
    @Override
    public void start(Stage primaryStage) { // ist auch abstrakte Methode, = ist sowas wie main() für JavaFX-App; Stage primaryStage = Oberfläche wird als Bühne verstanden (auf der Bühne wird Szene abgespielt (siehe unten))
        Button btn = new Button();
        btn.setText("Say 'Hello World'");
        btn.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
                System.out.println("Hello World!");
            }
        });
        
        StackPane root = new StackPane();
        root.getChildren().add(btn);
        
        Scene scene = new Scene(root, 300, 250); //hier ist die Szene; Szene = Container für Fenster-Content
        
        primaryStage.setTitle("Hello World!");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) { //man kann auf main() hier verzichten, wenn man bi der Erzeugung javaFX-packager-Tool benutzt. (man braucht auf jeden Fall main(), wenn man JavaFX mit Swing verbinden will)
        launch(args); //launch() ist Methode der Klasse Application
    }
}

```
#### 2 - Controls hinzufügen und verwenden
* Übung **JavaFXGUI1**
```java JavaFXGUI1.java
package javafxgui1;

import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;

import javafx.scene.control.Label;

/**
 *
 * @author trainer
 */
public class JavaFXGUI1 extends Application {

    // Label erzeugen, zum Anzeigen von "Hello World"  <- damit Label überall in JavaFXGUI1 bekannt ist als Klassen-Attribute deklarieren (wenn man Label in Start erzeugen würde, würde der handler von btn diesen Label nicht sehen)

    Label1 lbl = null;

    
    @Override
    public void start(Stage primaryStage) {
        
        //label erzeugen:
        lbl = new Label();

        //Ablauf Erzeugung eines GUI-Objekts
        //1 Obj erzeugen
        Button btn = new Button();

        //2. Obj konfigurieren (Eigenschaften)
        btn.setText("OK");

        //3. Ereignisbehandlung implementieren
        btn.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
                System.out.println("Hello World!");
            }
        });


        //4. dieses Obj. auf die Oberfläche bringen 
        StackPane root = new StackPane();
        root.getChildren().add(btn);
        
        Scene scene = new Scene(root, 300, 250);
        
        primaryStage.setTitle("Hello World!");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
```

#### 3 - Mehrere Fenster
#### 4 - CSS einsetzen
#### 5 - Eine Oberfläche mit Containern strukturieren
#### 6 - Ereignisbehandlung

### 2.3 - FXML und Programmlogik verbinden
#### 1 - Die Java-Sourcen bei einer FXML-Applikation
#### 2 - Eventhandling mit der Controllklasse
#### 3 - Öffentliche Controllstrukturen
#### 4 - Eventhandling mit JS
#### 5 - Java im Scripting nutzen

### 2.4 - Spezielle Applikationsfeatures
#### 1 - JavaFX in Swing nutzen
#### 2 - Preloader
#### 3 - Java-Logik in JavaFX nutzen
#### 4 - Gruppieren von Controls und der Scene Graph

### 3.1 - Text und Texteffekte in JavaFX
#### 1 - Text gestalten und einer UI hinzufügen
#### 2 - Textgestaltung bei FXML
#### 3 - Text mit Effekten versehen
#### 4 - Texteffekte bei FXML

### 3.2 - Graphische Formen und Bilder
#### 1 - Grafische Formen verwenden
#### 2 - Grafische Formen bei FXML
#### 3 - Bilder mit ImageView

### 3.3 - Die JavaFX UI Controls
#### 1 - Konzept der JavaFX UI Controls
#### 2 - Anpassen von UI Conrols
#### 3 - Schaltfäche und Auswahlelemente
#### 4 - Hyperlinks
#### 5 - Eingabefelder
#### 6 - Menüs
#### 7 - Views und Panes
#### 8 - ComboBox und ChoiseBox
#### 9 - Slider und Fortschrittsanzeigen
#### 10 - Tooltips
#### 11 - Ein praktischer Beispiel

### 4 - Spezielle Features
#### 1 - HTML-Content und das WebView-Control
#### 2 - Arbeiten mit Canvas
#### 3 - Diagramme
#### 4 - Transformationen
#### 5 - Animationen
#### 6 - JavaFX Media
#### 7 - 