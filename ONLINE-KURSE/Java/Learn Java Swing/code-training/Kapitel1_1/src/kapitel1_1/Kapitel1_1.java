/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package kapitel1_1;


import javax.swing.*;

public class Kapitel1_1 extends JFrame{
    JButton btn;
    JLabel lbl;
    JPanel panel;
    
    public Kapitel1_1(){
        this.panel = new JPanel();
        this.btn = new JButton();
        this.lbl = new JLabel();
        
        this.btn.setText("Click Me!");
        this.btn.setToolTipText("Click the button");
        
        this.panel.add(this.btn);
        this.panel.add(this.lbl);
        
        this.setTitle("Hello World from Swing");
        this.setSize(500,300);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setVisible(true);
        
        this.add(panel);
        
        //dem Button EventListener hinzufügen
        this.btn.addMouseListener(new java.awt.event.MouseAdapter (){
            @Override
            public void mouseClicked(java.awt.event.MouseEvent ae){
                //wenn geklickt wird, wird diese Funktion aufgerufen
                btnMouseClicked(ae);
            }
        });
    }
    
    private void btnMouseClicked(java.awt.event.MouseEvent ae){
        this.lbl.setText("Hello World");
    }
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        //erlaubt, Form zu starten
        java.awt.EventQueue.invokeLater(new Runnable(){
            //wenn man Runnable benutzt muss man run() überschreiben
            public void run(){
                new Kapitel1_1();
            }
        });
    }
    
}
