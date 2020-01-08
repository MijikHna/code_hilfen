### 0 - Introduction

### 1 - Swing Bacis
#### 1 - Learn about Swing
* Swing hat GUI-Componenten
* GUI besteht aus 3 Teilen:
    1. UI-Element
    2. Layout - Placement 
    3. Behavour - Events
* Swing-App besteht aus Containersystem
    * Top-Level-Container: JFrame, JDialog, JApplet
#### 2 - Use a WYSIWIG editor
#### 3 - Swing from scratch
#### 4 - MVC architecture
* Model-View-Controller-Arch:
    * Model - repräsentiert die Componenten der Daten
    * View - visuelle Repräsentation der Daten
    * Controller - verarbeitet die Daten
### 2 - Containers
#### 1 - Top-Level containers
* JRootPane -> JFrame + JWindow + JDialog + JApplet
* JXXX müssen zum Container hinzugefügt werden, damit sie in der GUI angezeigt werden können
#### 2 - Frames and panels
* Panels werden in Frames eingefügt
* Frame hat zwei Konstuktoren (ohne/mit Titel)
* Default Layout von Frame ist von Links nach Rechts - FlowLayout
* Man sollte bei Frames die Eigenschaft setzen, was soll passieren wenn auf *Schließen* geklickt wird:
    1. HIDE_ON_CLOSE - default
    2. EXIT_ON_CLOSE - meistens genutzt
    3. DISPOSE_ON_CLOSE 
    4. DO_NOTHING_ON_CLOSE
### 3 - Components and Layouts
#### 1 - Swing components
* alle Swing-Componenten erben von JComponent
* JComponent erweitert Container-Classe
#### 2 - Layout managers
* Layout Manager - Klassen, die Größe und Position der Komponenten kontrollieren
* Default ist FlowLayout - von Links nach Rechts
* Swing hat mehrere Layout Manager: (siehe Bsp. aus Exercise)
    1. BorderLayout - Teil View in 5 Teile: Nord, Süd, Ost, West und Zenter
    2. BoxLayout - Stackt die Komponenten - von Links nach Rechts -> bis kein Platz, dann zur nächsten Zeile
    3. CardLayout - Managet mehrere Komponenten, die den gleichen Teil teilen - man muss hier selber etwas Porgrammieren, da die Elemente den gleichen Space teilen
    4. FlowLayout - teilt alles in Zeilen
    5. GridBagLayout - tielt in Zeilen und Spalten
    6. GridLayout - teilt in alles in gleiche Zeilen und Spalten (also Zellen) - man muus hier eventuell auch eigenen Code einfügen, damit alles gut aussieht
    7. GroupLayout - arbeitet mit horizontalen und vetikalen Layout getrennt
    8. SpringLayout - flexibler Layout, der alle anderen Layouts simuliert
* in Designer kann man über Properties die Eigenschaften der Layout-Manager einstellen
* `JPanelName.setLayout(...)` - Layout setzen oder über Properties von JPanel oder über RechtsKlick auf JPanel -> Set Layout.  
#### 3 - Menus and toolbars
* Menu-Klasse in Swing hat:
    * Menu Bar
    * Menu Item
    * Menu
    * Menu Item/Checkbox
    * Menu Item/Radio Button
    * Popup Menu
* Toolbars - ist dem Menu sehr ähnlich, gruppiert Componenten (gewöhnlich Buttons)
    * oft als visuelle Repräsentation der Menu mit Icons zum anklicken
* in Design 
    1. Menu Bar auswähen
    2. Tool Bar auswählen
    3. Man kann im Designer Submenüs eingügen
        1. Menu-Eintrag auswählen
        2. Rechtsklicken -> Add From Palette -> Menu Item/../...
        3. über Properties dann z.B den Text ändern
        4. dann muss man Eventhänder für die Menü-Einträge programmieren
#### 4 - List model controls
* Swing hat Komponenten um Listen (Listen von Icons) zu erstellen
* Liste meisten Scroll Pane
* man muss dann auch Selection Mode setzen:
    1. SINGLE_SELECTION
    2. SINGLE_INERVAL_SELECTION
    3. MULTIPLE_INTERVAL_SELECTION
* Liste triggert automatisch ein Event, wenn Item der Liste ausgewählt wurde
    * Event muss dann vom Code behandelt werden
* Um Liste zu initialisieren => ListModel benutzen
    * Liste kann mit Array oder Vektor initialisiert werden, die automatisch zu ListModel konvertiert wird
* Liste ist immutable - kann nicht geändert werden
    * Listen, die gändert werden können, sind DefaultListModel
    * Drei Listen Modele:
        1. DefaultListModel - die flexibelste Liste
        2. AbstractListModel - default über Desing, ist ummutable
        3. ListModel
* Um z.B maximale Anzahl der Items in der Liste wird sichtbar `setVisibleRowCount(-1)`
* siehe Bsp. ListDemo -> ab Zeile 34:
    + `... ListDemo extends JPanel`
    + `implements ListSelectionListener`
    + `private JList list;` - eigentliche Liste
    + `private DefaultListModel listModel;` - ListModel festlegen
    + `public ListDemo(){}` - Konstuktor
        + `super(new BorderLayout());`
        + `listModel = new DefaultModelModel();`
        + `listModel.addElement("Mars");` - Item hinzufügen
        + `list = new JList(listModel);` - der Liste das ListModel zuweisen
### 4 - Events
#### 1 - What is a Swing event?
* User Interaction mit GUI-Interface
* meisten Events tiggern ein Action
    * Action = Veränderung im Zustand der Komponente
    * Event hat Info der Quelle des Events
* Swing benutzt *delegation-based-event Model*
    * Erhalter hörchen auf Event
    * wenn Event passiert, werden alle registierten Hörcher informiert
    * Vorteil: Code der Action(Event-Handler) ist getrennt von sonstigem Code 
        * vershiedene Kopmonenten haben verschieden Event-Handler
            * Button => Action Listener
            * ChechBox => Item Listener
* Event-Bahandlung besteht aus 3 Schitten: 
    1. Listener Interface implementieren z.B für Button => ActionListener implementierrn
    2. Instanz des Listener definieren
    3. Listener an der Komponente registrieren 
* Bsp: 
```java
class Test implements ActionListener {
    ActionListner al = new ActionListner(){ //1
        public void actionPerformed(ActionEvent ae){ //2 wegen Interface muss man actionPerfomed() überschreiben
            System.out.println("Action ausgeführt");
        };
    };
    button.addActionListener(al); //3
} 
```
* manche Listener-Interfaces können mehrere Methoden haben z.B MouseListener-Interface
* man kann auch Adapter-Klassen benutzen -> sie erstellen automatisch leeren Listener-Interface-Methoden und man überschreibt dann nur die, die man wirklich braucht
#### 2 - Event listeners
* Listener = Interfaces, die für Behandlung des Events zuständing sind
* an Component müssen die Event Listener registriert werden
* alle Listeners werden von EventListern extended
* entsprechende Listern haben eigenlciht passenden InterfaceNamen
* Bsp: ItemListenerEvent.java -> 3 ChechBoxen auswählen
```java
package swingexamples;

import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;
import javax.swing.BoxLayout;
import javax.swing.JCheckBox;
import javax.swing.JFrame;
import javax.swing.JPanel;

/**
 *
 * @author Producer
 */
public class ItemListenerExample extends JPanel implements ItemListener{

    JFrame frame;
    JPanel panel;
    JCheckBox checkBox1, checkBox2, checkBox3;

    public ItemListenerExample() {
        frame = new JFrame("Item Listener Example");
        frame.setSize(400, 400);
        panel = new JPanel();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);

        panel.setLayout(new BoxLayout(panel, BoxLayout.Y_AXIS));
        checkBox1 = new JCheckBox();
        checkBox1.setText("Check Box 1");
        checkBox2 = new JCheckBox();
        checkBox2.setText("Check Box 2");
        checkBox3 = new JCheckBox();
        checkBox3.setText("Check Box 3");

        //3 - Registierung
        chechBox1.addItemListener(this);
        chechBox2.addItemListener(this);
        chechBox3.addItemListener(this):

        panel.add(checkBox1);
        panel.add(checkBox2);
        panel.add(checkBox3);

        frame.setContentPane(panel);
    }

    public static void main(String ars[]) {
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new ItemListenerExample().setVisible(true);
            }
        });
    }

    @Override
    public void itemStateChanged(ItemEvent ie){
        //throw new UnsupportedOperationException("Not supported yed");
        //chechen, welche CheckBox ausgewählt wurde 
        Object source = ie.getItemSelecteable();
        if(source == checkBox1){
            System.out.println("ChechBox1"):
        }
        else if (source = chechBox2){
            System.out.println("ChechBox2"):
        }
        else{
            System.out.println("ChechBox3"):
        }
    }
}
```
#### 3 - How to handle an event
* Event Handler = Code, der ausgeführt wird, wenn Event getriggerd wird
* Componten geneieren Events
* Listener horchen dann, ob diese Event dann passiert ist
* und der Listener ruft Event Hanlder
    * Handler muss Event-Quelle kennen.
* wenn Event passiert ist, wird ein Event-Object erstellt und and den entsprechenden Listener gesendet. Diese Object hat dann Info über Event-Quelle und genauen Event-Action z.B Button geklickt
* Bsp: EventExample.java -> 9 Buttons 1 bis 9, die Farben generieren
```java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package swingexamples;

import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Random;

/**
 *
 * @author Producer
 */
public class EventExample extends javax.swing.JFrame implements ActionListener{

    /**
     * Creates new form EventExample
     */
    public EventExample() {
        initComponents();
        setSize(500, 500);
        jButton1.addActionListener(this);
        jButton2.addActionListener(this);
        //usw
    }

    private Color randomColor() {
        Random num = new Random();
        int randCol = num.nextInt(9) + 1;
        switch (randCol) {
        case 1:
            return Color.yellow;
        case 2:
            return Color.red;
        case 3:
            return Color.blue;
        case 4:
            return Color.green;
        case 5:
            return Color.orange;
        case 6:
            return Color.cyan;
        case 7:
            return Color.pink;
        case 8:
            return Color.magenta;
        case 9:
            return Color.white;
        default:
            return Color.black;
        }
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated
    // Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jPanel1 = new javax.swing.JPanel();
        jButton1 = new javax.swing.JButton();
        jButton2 = new javax.swing.JButton();
        jButton3 = new javax.swing.JButton();
        jButton4 = new javax.swing.JButton();
        jButton5 = new javax.swing.JButton();
        jButton6 = new javax.swing.JButton();
        jButton7 = new javax.swing.JButton();
        jButton8 = new javax.swing.JButton();
        jButton9 = new javax.swing.JButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("Random Color");
        setSize(new java.awt.Dimension(500, 500));

        jPanel1.setLayout(new java.awt.GridLayout(3, 3, 10, 10));

        jButton1.setFont(new java.awt.Font("Papyrus", 0, 36)); // NOI18N
        jButton1.setText("1");
        jPanel1.add(jButton1);

        jButton2.setFont(new java.awt.Font("Papyrus", 0, 36)); // NOI18N
        jButton2.setText("2");
        jPanel1.add(jButton2);

        jButton3.setFont(new java.awt.Font("Papyrus", 0, 36)); // NOI18N
        jButton3.setText("3");
        jPanel1.add(jButton3);

        jButton4.setFont(new java.awt.Font("Papyrus", 0, 36)); // NOI18N
        jButton4.setText("4");
        jPanel1.add(jButton4);

        jButton5.setFont(new java.awt.Font("Papyrus", 0, 36)); // NOI18N
        jButton5.setText("5");
        jPanel1.add(jButton5);

        jButton6.setFont(new java.awt.Font("Papyrus", 0, 36)); // NOI18N
        jButton6.setText("6");
        jPanel1.add(jButton6);

        jButton7.setFont(new java.awt.Font("Papyrus", 0, 36)); // NOI18N
        jButton7.setText("7");
        jPanel1.add(jButton7);

        jButton8.setFont(new java.awt.Font("Papyrus", 0, 36)); // NOI18N
        jButton8.setText("8");
        jPanel1.add(jButton8);

        jButton9.setFont(new java.awt.Font("Papyrus", 0, 36)); // NOI18N
        jButton9.setText("9");
        jPanel1.add(jButton9);

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addComponent(
                jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE));
        layout.setVerticalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addComponent(
                jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE));

        pack();
    }// </editor-fold>//GEN-END:initComponents

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        // <editor-fold defaultstate="collapsed" desc=" Look and feel setting code
        // (optional) ">
        /*
         * If Nimbus (introduced in Java SE 6) is not available, stay with the default
         * look and feel. For details see
         * http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(EventExample.class.getName()).log(java.util.logging.Level.SEVERE, null,
                    ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(EventExample.class.getName()).log(java.util.logging.Level.SEVERE, null,
                    ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(EventExample.class.getName()).log(java.util.logging.Level.SEVERE, null,
                    ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(EventExample.class.getName()).log(java.util.logging.Level.SEVERE, null,
                    ex);
        }
        // </editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new EventExample().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton jButton1;
    private javax.swing.JButton jButton2;
    private javax.swing.JButton jButton3;
    private javax.swing.JButton jButton4;
    private javax.swing.JButton jButton5;
    private javax.swing.JButton jButton6;
    private javax.swing.JButton jButton7;
    private javax.swing.JButton jButton8;
    private javax.swing.JButton jButton9;
    private javax.swing.JPanel jPanel1;
    // End of variables declaration//GEN-END:variables

    //ActionListener-Inteface Methoden überschreiben
    //ist eigentlich Event-Handler
    @Override
    public void actoinPerformed(ActionEvent ae){ 
        //throw new UnsupportedOperationException("Not supported yet");
        
        Color col = randomColor();
        if(ae.getSource() == jButton1){ //welches Button geklickt wurde
           jButton1.setBackground(col);
        }
        if(ae.getSource() == jButton2){ //welches Button geklickt wurde
           jButton2.setBackground(col);
        }
        //usw.

    }
}

```
#### 4 - Challenge
* GUI für Einkaufsliste
    * Labels + Textfelder
    * 3 Buttons. Add, Print, Clear
    * Event Listener + Event Handler für die Buttons 
#### 5 - Solution
* Lösung ist GroceryList.java
    1. jTextField1 nach itemTxt umbennen
    2. jButton1 nach AddBtn unbennen + für Print und Clear
    3. TextArea1 nach list umbennen
    4. Add-Button auswähen -> zu Events-Tab wechseln -> actionPerformed auf addButtonActionPerformed setzen => es wird automatisch die Handler-methoden erstellt
    ```java
    private void addButtonActionPerformed(java.awt.event.ActionEvent evt){
        if(item.getText().length() != 0){
            String groceryItem = item.getText();
            list.append(groceryItem + "\n");
            item.setText(""); //Text in TextField löschen
        }
    }
    ```
    * für print- und clear-Buttons ab 4. 
    ```java
    private void printButtonActionPerformed(java.awt.event.ActionEvent evt){
        System.out.println(list.getText());
    }
    private void printButtonActionPerformed(java.awt.event.ActionEvent evt){
        list.setText("");
    }
    ```
    + die Listener werden von IDE automatisch registiert
    im Konstruktor noch default Button setzen: `getRootPanel().setDefaultButton(addButton);`

### Outro
+ Swing wird momentan mehr und mehr von JavaFX verdrängt