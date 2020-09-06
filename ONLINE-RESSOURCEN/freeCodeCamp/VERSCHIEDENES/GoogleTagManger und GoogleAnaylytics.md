**Google Tag Manager**  und **Google Analytics** sind Tools um Traffic zu messen. Sind eigentlich JS-Code-Snippets, die Traffic der Seite abchecken.
* Weitere ähnliche Tools:
    1. Crazy Egg oder Hot Jar - Traffic Visualisaion
    2. Google Ads - Umbau/Umsetzung der "Pixels"
    3. Google Optimize oder AB Tasty - A/B Testing
    4. Cliet Side Error - Client Side Error Tracking
    5. GDRP Compliance Management
* Begriffe des GTMs:
1. Tags - Pixels oder Code Snippets
2. Variables - 
3. Triggers
4. Container - Gruppen von Tags

### Set UP GTM:
* einen Account auf https://tagmanager.google.com/#/home erstellen
* Account-Name sollte Top Level Hierarchy und Container-Name sollte bestimmte Instance represäntieren
* Snippets installieren.
* Es wird auch ein "Debugger" für GTM zu Verfügung gestellt.

### SET UP Google Anaytics 
* in GTM Variable `GA Settings` erstellen und als Typ `Google Analytics` auswählen und Google Analytics Tracker-ID eingeben
* in GTA einen Tag erstellen `GA-All Pages` Typ ist `Google Analytics: Universal Analytics` und die Variable `GA Settins` auswählen
* auf `Triggering Box` clicken.
* Seiten auswählen die Triggers sein sollten
* Speihern
* <- momentan ist GA doppelt installiert:
    1. in Google Analytics selbst
    2. über GTM
* => in den Code gehen und 
    * `[YOUR GA PROPERTY ID]` der GA Propert ID  durch `[YOUR GTM CONTAINER ID]` von GTM Container ID erstetzen.
* in der GTA-UI auf **Enable** clicken und referschen
* **Submit** und dann **Publish** klicken
* dann kann man Gruppen und Users in GTM Berechtigungen vergeben.