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
+ = ein Start-Fenster, das weitere Fenster aufmacht:
* => weiter Java-Klasse:
    * Bühne wo dann weitere Szene präsentiert wird => Subklasse wird vom Typ `Stage sein`
        1. new Klasse `FolgeFenster.java` muss dann `extend Stage`
```java MainFenster
public class JavaFXMehrereFenster extends Application {
    
    @Override
    public void start(Stage primaryStage) {
        Button btn = new Button();
        btn.setText("Neues Fenster");
        btn.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
                new FolgeFenster();
            }
        });
        
        StackPane root = new StackPane();
        root.getChildren().add(btn);
        
        Scene scene = new Scene(root, 300, 250);
        
        primaryStage.setTitle("Mehrere Fenster");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
```
* FolgeFenster:
```java FolgeFenster.java
public class FolgeFenster extends Stage {
    Stage primaryStage; //Obj vom Typ primaryStage
    public FolgeFenster(){
        primaryStage = this; //in primaryStage wird dann aktuelles Fenster gespeichert
        Button btn = new Button();
        // Button zum Schließen des FolgeFensters
        btn.setText("Schließen");
        btn.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
                primaryStage.hide();
            }
        });
        
        StackPane root = new StackPane();
        root.getChildren().add(btn);
        
        Scene scene = new Scene(root, 300, 250);
        
        primaryStage.setTitle("Mehrere Fenster");
        primaryStage.setScene(scene);
        primaryStage.show();
    }
}
```
#### 4 - CSS einsetzen
* Neue Datei erstellen: `css` erstellen
* `scene.getStylesheet().add(AKTUELLER-KLASSEN-NAME.class.getRessource('lala.css').toExternalForm())`
* jetzt kann man .css bearbeiten:
```css
root{ // um auf .root umstellen. 
    display: inblock;
    -fx-background-color: green;

}

.button{
    display:block;
    -fx-background-color: red;
}
```
* inline CSS: `btn.setStyle('-fx-text-fill: white');` 
#### 5 - Eine Oberfläche mit Containern strukturieren
* mit Hilfe der Pain-Strukturen
* SceneBilder bzw. .fxml-Datei = Abbildung xml auf JavaFX-Klassen (javafx.scene.layout-Klassen)
* Wenn man JavaFX-Project anschaut => Wurzel-Obj ist vom Typ `StackPane` z.B durch `AnkerPane`. 
```java GUI
public class JavaFXGUI2 extends Application {
    
    @Override
    public void start(Stage primaryStage) {
        Button btn = new Button();
        btn.setText("Say 'Hello World'");
        btn.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
                System.out.println("Hello World!");
            }
        });
        
        AnchorPane root = new AnchorPane();
        btn.layoutXProperty().setValue(50); //X-Wert von btn um 50 PX verschieben
        btn.layoutYProperty().setValue(50); //Y-Wert von btn um 50 PX verschieben
        root.getChildren().add(btn);

        // HBox mit zwei Buttons erzeugen. Wird nach dem btn platziert.
        HBox hb = new HBox();
        
        Button btn2 = new Button();
        btn2.setText("1");
        
        Button btn3 = new Button();
        btn3.setText("2");
        
        hb.getChildren().addAll(btn2,btn3);
        root.getChildren().add(hb);
        
        
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
#### 6 - Ereignisbehandlung
* = Eventhandling
```java JavaFXEvent
public class JavaFXEvent extends Application {

    Label lb;

    @Override
    public void start(Stage primaryStage) {
        Button btn = new Button();
        btn.setText("OK");
        
        // Event setOnAction = ist StrandardAktion für Komponente= Click (! fast bei allen Elementen ist das CLICK)
        btn.setOnAction(new EventHandler<ActionEvent>(){ //neues Obj. EventHander als Parameter erzeugen ActionEvent als Generischer Typ (man kann es auch weglassen) = anonym erzeugtes Obj

            //EventHandler ist eine abstrakte Klasse, die eine abstrakte Methode handle() hat
            @Override
            public void handle(ActionEvent t) {
                lb.setText("Neuer Text"); //hier wird auf lb zugegriffen. muss in der aktuellen Klasse Attribut sein sonst ist der Methode handle() unbekannt
                
            }
        });

        lb = new Label();
        lb.setText("Vorgabe");

        //label und btn anordnen
        AnchorPane root = new AnchorPane();
        btn.layoutXProperty().setValue(50);
        btn.layoutYProperty().setValue(50);
        lb.layoutXProperty().setValue(50);
        lb.layoutYProperty().setValue(150);
        root.getChildren().addAll(btn, lb);


        Scene scene = new Scene(root, 300, 250);

        primaryStage.setTitle("Ereignisse");
        primaryStage.setScene(scene);
        primaryStage.show();

    }

    public static void main(String[] args) {
        launch(args);
    }
}
```

### 2.3 - FXML und Programmlogik verbinden
#### 1 - Die Java-Sourcen bei einer FXML-Applikation
* Lala.fxml hat meistens zwei .java-Dateien:
    1. Lala.java:
        ```java 
        public class JavaFXFXMLLogik extends Application {
        
            @Override
            public void start(Stage stage) throws Exception {
                Parent root = FXMLLoader.load(getClass().getResource("Sample.fxml"));
                
                Scene scene = new Scene(root);
                
                stage.setScene(scene);
                stage.show();
            }

            public static void main(String[] args) {
                launch(args);
            }
        }
        ```
        1. main()
        2. start() mit Scene und Stage. Wobei hier wird statt Java-Code die .fxml geladen.
    2. xxxController.java
        ```java SampleController.java
            public class SampleController implements Initializable {
            
            @FXML
            private Label lbl;
            
            @FXML
            private void handleButtonAction(ActionEvent event) {
                System.out.println("You clicked me!");
                lbl.setText("Hello World!");
            }
            
            @Override
            public void initialize(URL url, ResourceBundle rb) {
                // TODO
            }    
        }
        ```
        1. hier wird EventHandling notiert.
    3. in .fxml git es den Eintrag: `fx:controller=...`
        ```xml Sample.xml
        <?xml version="1.0" encoding="UTF-8"?>

        <?import java.lang.*?>
        <?import java.util.*?>
        <?import javafx.scene.*?>
        <?import javafx.scene.control.*?>
        <?import javafx.scene.layout.*?>

        <AnchorPane id="AnchorPane" prefHeight="200" prefWidth="320" xmlns:fx="http://javafx.com/fxml" fx:controller="javafxfxmllogik.SampleController">
            <children>
                <Button layoutX="126" layoutY="90" text="Click Me!" onAction="#handleButtonAction" fx:id="button" />
                <Label layoutX="126" layoutY="120" minHeight="16" minWidth="69" fx:id="lbl" />
            </children>
        </AnchorPane>
        ```
        1. `onAktion`= verweist auf die Methode die in Controller spezifiziert.
        2. in SceneBuilder -> Inspektor -> Code -> ControllerKlasse setzen
#### 2 - Eventhandling mit der Controllklasse
* in .fxml:
    * `onAction="#EventFunktName"` `#` ist wichtig.
    * `fx:controller="javafxfxmllogik.SampleController` - den Controller zuweisen
* in Controller.java
    ```java
    @FXML
    private Label lbl;

    @FXML
    private void handleButtonAction(ActionEvent event) {
        System.out.println("You clicked me!");
        lbl.setText("Hello World!");
    }
    ```
    * `@FXML` - obwohl es private Funktion ist, wird Zugriff aus .fxml erlaubt. Man kann auch die Methode public setzen und auf `@FXML` verzichten. Also bindet .fxml und Java-Attr/-Methoden
    * `lbl` ist ID in .fxml. Muss hier an .fxml gebunden werden, da in `handleButtonAction()` darauf zugegriffen wird. In SceneBuilder über Insektor-> Code -> ID setzen. und die Methode für OAction vergeben
#### 3 - Öffentliche Controllstrukturen
* man kann `@FXML` weglassen und `private` durch `public` erstetzen => Strukturen des Controllers nach außen freigeben => werden auch von anderen Java-Klassen erreichbar.
#### 4 - Eventhandling mit JS
* Logik kann man auch mit JS implementieren.
* `xxxController.java` weglassen und Logik in JS packen
* JS wir direkt im .fxml eingebunden.
    * dabei sieht die .fxml etwas anders aus.

```java xxxController.java
public class JavaFXFXMLJavaScript extends Application {
    
    @Override
    public void start(Stage stage) throws Exception {
        Parent root = FXMLLoader.load(getClass().getResource("Sample.fxml"));
        
        Scene scene = new Scene(root);
        
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
```

```xml 
<?xml version="1.0" encoding="UTF-8"?>

<?import java.lang.*?>
<?import java.util.*?>
<?import javafx.scene.*?>
<?import javafx.scene.control.*?>
<?import javafx.scene.layout.*?>
<?language javascript?> <!-- JS als Logiksprache festlegen -->

<AnchorPane id="AnchorPane" prefHeight="200" prefWidth="320" xmlns:fx="http://javafx.com/fxml" >
    <fx:script> <!-- der JS Script, man auch JS mit source="" JS-Datei statt inline Code einbinden -->
        function handleButtonAction(){
            label.setText("Hallo Welt");
        }
    </fx:script>
    <children>
        <Button layoutX="126" layoutY="90" text="Click Me!" onAction="handleButtonAction()" fx:id="button" /> <!-- die Aufrufe sehen jetzt auch etwas anders aus>
        <Label layoutX="126" layoutY="120" minHeight="16" minWidth="69" fx:id="label" />
    </children>
</AnchorPane>
```
+ in SceneBuilder: Inspektor -> Code keinen Controller eintragen und z.B bei OnAction wird komplettter JS-Funkt-Name eingetragen: `handleButtonAction()`
#### 5 - Java im Scripting nutzen
+ man kann auch andere Scripting-Sprachen statt JS verwenden
+ Bsp Java direkt in .fxml einbinden:
```xml
<?xml version="1.0" encoding="UTF-8"?>

<?import java.lang.*?>
<?import java.util.*?>
<?import javafx.scene.*?>
<?import javafx.scene.control.*?>
<?import javafx.scene.layout.*?>
<?language javascript?>

<AnchorPane id="AnchorPane" prefHeight="200" prefWidth="320" xmlns:fx="http://javafx.com/fxml" >
    <fx:script> <!--statt JS wird wird hier Java verwendet -->
        importClass(java.util.Random);
        function handleButtonAction(){
          label.setText(new Random().nextInt().toString());
        }
    </fx:script>
    <children>
        <Button layoutX="126" layoutY="90" text="Click Me!" onAction="handleButtonAction()" fx:id="button" /> <!--der Aufrufe bleibt aber wie für JS-->
        <Label layoutX="126" layoutY="120" minHeight="16" minWidth="69" fx:id="label" />
    </children>
</AnchorPane>
```

### 2.4 - Spezielle Applikationsfeatures
#### 1 - JavaFX in Swing nutzen
* JavaFX kann mit Swing zusammenarbeiten
* als Proj z.B JavaFX in SwingApplication
* also in Swing-Applet wird JavaFX-App ausgeführt
+ über Klassen Attirbute/Variablen können dann innere JavaFX-App mit Swing-App reden
```java
/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package javafxswingapplication1;

//Swing Imports
import java.awt.BorderLayout;
import java.awt.Dimension;
import javax.swing.JApplet;
import javax.swing.JFrame;
//JavaFX Imports
import javax.swing.SwingUtilities;
import javax.swing.UIManager;
import javafx.application.Platform;
import javafx.embed.swing.JFXPanel;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.StackPane;


/**
 *
 * @author trainer
 */
public class JavaFXSwingApplication1 extends JApplet { // ist von Swing-Klasse JApplet geerbt, also Swing-Applet
    
    private static final int JFXPANEL_WIDTH_INT = 300;
    private static final int JFXPANEL_HEIGHT_INT = 250;
    private static JFXPanel fxContainer;

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                try {
                    UIManager.setLookAndFeel("com.sun.java.swing.plaf.nimbus.NimbusLookAndFeel");
                } catch (Exception e) {
                }
                
                JFrame frame = new JFrame("JavaFX 2 in Swing"); //Swing Fenster festgelegt
                frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); //Schließverhalten für das Fenster
                
                JApplet applet = new JavaFXSwingApplication1(); //JApplet festgelegt
                applet.init();
                
                frame.setContentPane(applet.getContentPane());
                
                frame.pack();
                frame.setLocationRelativeTo(null);
                frame.setVisible(true); //Fenster wird angegzeigt
                
                applet.start(); //Apllet wird gestartet
            }
        });
    }
    
    @Override
    public void init() { // hier wird aber nun JavaFX benutzt
        fxContainer = new JFXPanel(); //JavaFX-Panel erzeugt 
        fxContainer.setPreferredSize(new Dimension(JFXPANEL_WIDTH_INT, JFXPANEL_HEIGHT_INT));
        add(fxContainer, BorderLayout.CENTER);
        // create JavaFX scene
        Platform.runLater(new Runnable() {
            @Override
            public void run() {
                createScene(); //Scene erstellen, die im wesentlichen JavaFX-Scene erstellt.
            }
        });
    }
    
    private void createScene() { // hier ist dann gewohnter Code für JavaFX-App
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
        fxContainer.setScene(new Scene(root));
    }
}
```
#### 2 - Preloader
* Animation, wenn etwas geladen wird
* New Project -> JavaFXPreloader
+ es wird Java-Klasse generiert, die `Preloader` extended.
* Preloader wird von anderem Program benutzt und nicht als selbststängiges Program ausgeführt.
* => den Preloader dem eigentlich Programm voranstellen:
    * bei `RUN`-Menü -> Project-Properties
    * Preloader-Project als Preloader eintragen
    * ist eigentlich nur nötig, wenn Programm-Start lange dauert.
    + man kann auch Preloader beim JavaFX-Project einstellen (passendes Häckchen (NetBeans))
#### 3 - Java-Logik in JavaFX nutzen
* Bsp: JavaFXNutzeJava (hat zwei Klassen)
```java JavaFXNutzeJava.java
public class JavaFXNuzteJava extends Application {
    private VBox vb;
    
    @Override
    public void start(Stage primaryStage) {
        Button btn = new Button();
        btn.setText("Ziehe Zahlen");
        btn.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
                vb.getChildren().clear();
                int[] zahlen = new Lotto().zahlen();
                for (int i : zahlen) {
                    vb.getChildren().add(new Label(""+i));
                }
            }
        });
        
        AnchorPane root = new AnchorPane();
        vb = new VBox();
        root.getChildren().addAll(btn,vb);
        btn.layoutXProperty().set(20);
        btn.layoutYProperty().set(20);
        vb.layoutXProperty().set(20);
        vb.layoutYProperty().set(50);
        Scene scene = new Scene(root, 300, 250);
        
        primaryStage.setTitle("Ziehung der Lottozahlen");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}

```
```java Lotto.java
/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package javafxnuztejava;

/**
 *
 * @author trainer
 */
public class Lotto {
    public int[] zahlen() {
         // TODO Auto-generated method stub
         boolean gefunden = false;
         int zahlen[] = new int[7];
         int zaehler=0;
         int tempzahl = 0;
         while(zaehler < 7) {
             tempzahl = (int) (1 + Math.floor(Math.random()*49));
             for (int i = 0; i < zahlen.length; i++) {
                 if(tempzahl==zahlen[i]) {
                     gefunden=true;
                     break;
                 }
             }
             if(!gefunden){
                 zahlen[zaehler]=tempzahl;
                 zaehler++;
             }
             gefunden=false;
         }
         return zahlen;
     }
}
```
#### 4 - Gruppieren von Controls und der Scene Graph
* Baumstruktur der Anordung der JavaFX-Elemente.
* Bsp: Rechteck in die Scene einbauen.
```java

public class JavaFXGruppe extends Application {

    @Override
    public void start(Stage primaryStage) {
        Button btn = new Button();
        btn.setText("Klick");
        Label lb = new Label();
        lb.setText("Ein Label");
        
        // Element vom Typ Group um einen Wurzel für Elemente zu bauen und dann anderen Layout-Strukturen hinzufügen
        Group groot = new Group();
        
        lb.layoutXProperty().set(50);
        lb.layoutYProperty().set(50);
        btn.layoutXProperty().set(50);
        btn.layoutYProperty().set(100);
        
        // Rechteck der in die Scene eingesetzt werden soll
        Rectangle r = new Rectangle(125, 125, 250, 250);
        r.setFill(Color.BLUE);

        //Button, Label und Rechteck der Gruppe hinzufügen
        groot.getChildren().addAll(btn, lb, r);

        Button btn2 = new Button("Klack");
        BorderPane root = new BorderPane();

        //dem root dann die Gruppe und Button2 hinzufügen
        root.getChildren().add(groot);
        root.setBottom(btn2);


        Scene scene = new Scene(root, 300, 250, Color.YELLOW);

        primaryStage.setTitle("Gruppieren und der Scene Graph");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
```

### 3.1 - Text und Texteffekte in JavaFX
#### 1 - Text gestalten und einer UI hinzufügen
* in der Doku: `java.scene.text` -> Klassen: `Text,`, `Layout`
```java JavaFXText
public class JavaFXText extends Application {

    @Override
    public void start(Stage primaryStage) {
        Text t1 = new Text();
        t1.setText("RJS EDV-KnowHow");
        t1.setFont(Font.font("Arial",24));
        t1.setFill(Color.RED);


        Text t2 = new Text("Dipl Math Ralph Steyer");
        //ID die in CSS definiert wurde vergeben
        t2.setId("t");

        Text t3 = TextBuilder.create().text("www.rjs.de").build(); //mit TextBuilder.create() = Obj erstellen, der Methode text() hat, die wiederum ein Obj liefert, das Methode build() hat

        BorderPane root = new BorderPane();
        VBox vb = new VBox();
        vb.getChildren().addAll(t1, t2, t3);
        root.getChildren().add(vb);

        Scene scene = new Scene(root, 300, 250);
        //CSS-Datei einbinden
        scene.getStylesheets().add(JavaFXText.class.getResource("text.css").toExternalForm());

        primaryStage.setTitle("Text");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
```
* man kann dann auf diese Texte dann CSS anwenden.
```css text.css
root { 
    display: block;
}

#t{ /*ID*/
    -fx-font:100px Tahoma;
    -fx-fill:linear-gradient(from 0% 0% to 80% 120%, repeat, aqua 0%, green 65%);
}
```
#### 2 - Textgestaltung bei FXML
* Text auch über .fxml-Datei definieren
* bei Scenen -> Library -> Text = entsprechen den Text-Obj in Java. 
```xml
<?xml version="1.0" encoding="UTF-8"?>

<?import java.lang.*?>
<?import java.util.*?>
<?import javafx.scene.*?>
<?import javafx.scene.control.*?>
<?import javafx.scene.layout.*?>
<?import javafx.scene.text.*?>

<AnchorPane id="AnchorPane" prefHeight="200.0" prefWidth="320.0" xmlns:fx="http://javafx.com/fxml">
  <children>
    <!--Text erstellen (wurde aber in SceneBuilder alles festgelegt) -->
    <Text fill="linear-gradient(from 0.0% 0.0% to 100.0% 100.0%, 0xff0000ff 0.0%, 0x0000ffff 30.0%, 0x000000ff 100.0%)" layoutX="136.0" layoutY="112.0" scaleX="9.040938384933801" scaleY="3.5687714145863927" strikethrough="false" stroke="#00a3ff" strokeType="INSIDE" strokeWidth="0.0" text="www.rjs.de" underline="false">
      <font>
        <Font name="Calibri Light Italic" size="5.0" />
      </font>
    </Text>
  </children>
</AnchorPane>
```
#### 3 - Text mit Effekten versehen
#### 4 - Texteffekte bei FXML

<!-- BIS HIERHIN -->

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