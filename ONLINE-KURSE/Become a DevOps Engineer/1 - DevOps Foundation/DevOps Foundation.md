### 1 - DevOps Basics
#### 1 - What is DevOps
+ (Dev = Code) + (Ops = System) 
#### 2 - DevOps core values: CAMS
* - Culture Automation Measurement Sharing
#### 3 - DevOps principles: The three ways
1. Systemsthinking - über das gesamt Output denken
2. Empliphying Feedbackloops - zwischen den Abteilungen
3. Create Workculture - Experimentieren und Lernen (lernen und teilen). Mehr wie man ein Tool/Feature nutzt statt welches Tool
    * Teamprozesse erstellen, Teamstandards erstellen, ist Teil des Managements
#### 4 - Your DevOps playbook
* 5 Methoden in DevOps:
    1. People over Process over Tools - zuerst definieren, wer verantwortlich dann für welchen Prozess dann mit welchen Tools
    2. Continuous Delivery (CD) - kleinere Releases in kürzeren Abständen
    3. Lean Management - in kleineren Bündeln arbeiten, mit Deadlines arbeiten, Feedback loops, Visualisieren 
    4. Visible ops change Control - Fragile Artefakte eliminieren, wiederkehrenden Buildprozess implementieren, Abhängigkeiten verwalten, Umgebung für andauernde Verbesserung erstellen
    5. Infrastructure as Code - Systeme wie Code bahandeln, Systemspezifikatonen sollten im Source Controll eingechecket werden, Reviewed, build und tested, sollten gemanaged werden 
#### 5 - 10 practices for DevOps success: 10 through 6
* Incident Command System - 
* Developers on Call - 
* Public Status Pages - Benutzer können über Probleme/Neuigkeiten informiert werden
* Blameless Postmortems (schuldlose Leichenrede) - 
* Embedded Teams 
#### 6 - 10 practices for DevOps success: 5 through 1
* The Cloud - IP-Driven Way
* Andon cords (cord - die Leitung, das Kabel) - kommt von Fließband, wenn ein Fehler entdeckt wurde, wird am Kabel gezogen, sodass ganze Fließband steht.
* Dependency Injection - die Anhängigkeiten sind in die App integriert. 
* Blue/Green Deployment - man hat zwei gleiche Systeme (blue und green). Eins ist online andere ist online. Zuerst die offline System upgraden und testen dann diese online schalten, wenn sich Probleme herausstellen, dann zurückschalten.
* Chaos Monkey - (von Netflix entwickelt) - ??? 
#### 7 - DevOps tools: The cart or the horse
* mehrere Tools zum Tool Chain machen (Gefahr zu viele Tools benutzen)
* Tools auswählen:
    1. programmierbar/einstellbar
    2. verfizierbar
    3. gutes Verhalten - aus Operation und Development Sicht

### 2 - DevOps: A Culture Problem
#### 1 - The IT crowd and the coming strom
* viele Abteilungen arbeiten "nicht zusammen". Jeder ist nur mit seiner Sache beschäftigt. Es entstehen "Wände".
#### 2 - Use your words
* "schuldlose Leihenrede":
    * Meeting
    * man sollte alles innerhalb von 48 Stunden erledigen/angehen, wenn es entschieden wurde.
* niemanden schuldig sprechen, sondern sicherstellen, dass es nicht mehr passiert
* Lösen:
    * Incident beschreiben
    * Root-Cause beschreiben
    * Wie wurde gelöst
    * Timeline des Events
* Transparent Uptime:
    1. Fehler zugeben/aktzeptieren
    2. wie ein Mensch klingen (also Entschuldigne)
    3. Kommunizieren
    4. Authentisch sein (einen auswählen, der Kommmunikation führt)
#### 3 - Do unto others
* Sozialle Skills sind wichtig
* ein Team weis nicht was anderes macht ("Wände")
    * Lösung verschiedene Teams in eigene Aufgabe involvieren
#### 4 - Throwing things over walls
* Westrum Model ist bis jetzt am erfolgreichstem:
    1. power-oriented
    2. rule-oriented
    3. performance-oriented
#### 5 - Kaizen: Continuous improvement 
* Lean wurde zuerst in Japan eingefürt:
    * Kaizen - Continues Improvment (in Toyota) (Verbesserung zum Besseren)
* Kaizen - gehen zum Problemort und schaue dir es an.
* "es gibt keine Menschlichen Fehler -> sondern Prozess-Fehler"

### 3 - The Building Blocks of DevOps
#### 1 - DevOps building block: Agile
* DevOps-Geschichte beginnt mit Agile
* SW wird in Sprints geliefert/entwickelt
#### 2 - DevOps building block: Lean
* kommt von Toyota -> dann zu SW angewendet.
* 7 Lean Prizipien:
    1. eliminate waste
    2. amplify learning
    3. decide as late as possible
    4. decide as fast as possible
    5. empower the team
    6. build in integrity
    7. see the whole
* Lean bringt zum Vorschen:
    1. muda - Arbeit, die Resourcen verbraucht, aber nicht kommt
    2. Muri - unnötige arbeit von Arbietern und Maschinen
    3. Mura - Arbeit kommt nicht gleichmässig
* also in Lean wird Pfad des Produkt analysiert
#### 3 - ITIL, ITSM and the SDLC
* ITSM - IT Service Management = SW Devlivery
* ITIL - Information Technology Library (kommt aus UK-Govermount-IT), hat vier Phasen (Guidenes ansehen (5000 Seiten (4 Bücher)))
    1. Service strategy
    2. Service design
    3. Service transition
    4. Service operation
* 

### 4 - Infrastructure Automation
#### 1 - Infrastructure as code
* www.infrastructures.org
* alles mit Scripts/Code realisieren.
* Application Code + Infrastructure Code -> Version Control -> Continuous Delivery Pipeline -> Prod + Stage
#### 2 - Golden image to foil ball
* Configuration Management
    * Provisioning - Server einrichten, damit er bestimmte Sache/Service ausführen kann.
    * Deployment - automtisches Deploying + Upgrading der App auf dem Server
    * Orchestration - koordinierte Operationen zwischen mehreren Systemen ausführen.
    * Configuration Management - Änderung/Maintaining/Upgrading der Konfiguration nach Provisonierung
* Rangehensweisen:
    * Imperative/Procedural - Befehle ausführe, die das Ganze in bestimmten Zustand bringen
    * Declarative/Funtional - Zustand wird definiert, anhand des Tools, mit dem das System konfiguriert wird
    * Idemponent - Befehle weiderholend ausführen und im selben Zustand landen
    * Self Service - Möglichkeit für "User" Prozesse anzukicken, ohne dabei andere ("Entwickler") um Hilfe zu fragen
* also z.B mit/in Chef/Puppit um System-zustand zu definieren. (also automatische Konfiguration)
* Deployment Pattern:
    * Canary (Staged) Deployment Pattern - einen Server/Service upgraden, wenn alles OK, alle anderen upgraden
    * Blue Green Deployment - zwei gleiche Systeme (Development, Live), Development upgraden, wenn alles OK, swappen, dann Live upgraden => Live wird zu Develpment und umgekehrt
    * Immutable Deployment - Systeme wird nicht upgraded, sodnern gekillt und ein komplett neues an seiner Stelle eingesetzt (Netflix)
#### 3 - Immutable deployment
* kommt mit Containers, da alles in Conatainern gemacht werden, und dann gehen sie live
* CMDB - ? 
#### 4 - Your infrastructure toolchain
* Entscheidung basiert darauf, wo/wie man Server betreibt (Cloud, onPremise, Container)
* Mögliche Tools 
    * Configuration Management:
        1. Chef
        2. Puppet
        3. Ansible
        4. Salt
        5. CFEngine
        6. Packer
    * Service Direcotry Tools:
        1. etcd
        2. ZooKeeper
        3. Consul
    * Container Orchestration:
        1. Docker
        2. Kubernetes
        3. Mesos
    * habitat - Tool erweitert Chef

### 5 - Continuous Delivery
#### 1 - Small + fast = better
* Continues Integarion - Code builden und Unit testen permanent
* Cotinues Delivery - automatische Integration und Testing
* Continues Deploy - zur Production automatisch wechseln
* ~ Deploy on Demand
#### 2 - Continuous integration practices
+ Cotinues Delivery: Code -> Build -> Unit Tests -> Code Validation -> Packing -> Arifact
* besteht aus:
    1. Continues Deploy
    2. Continues Delivery
    3. Continues Integration
* 6 Practices:
    1. Builds sollten in Kaffe Pause passen (< 4 Minutes)
    2. kleine Commits
    3. Builds niemals gebrochen lassen
    4. trunk-based Development flow benutzen
        1. trunk-based Dev
        2. brunch Dev 
    5. Don't allow flaky tests
    6. Build sollte status, Log und artifact zurückgeben
#### 3 - The continuous delivery pipeline
* Continues Delivery 
    1. Artifacts nur einmal bilden => alle benutzen den gleichen Artifact
    2. Artifacts sollten immutable sein (also nur lesbar sein)
    3. Deployment should go to a copy of production (um Test zu machen)
    4. Stop deploy if a previous step fails
    5. Deployments should be idemponent
* Artifact - Flow
    1. Code
    2. Verstion continued
    3. CI System creates build (z.B in master-branch mergen)
    4. Builds going into shelf + deploy goes to stage
    5. Staging ODER
    6. Testing ODER
    7. Ready for Prod
    8. Deploy to Prod -> Release
#### 4 - The role of QA
* Test Typen:
    1. Unit testing
    2. Code hygiene
        * Linting
        + Code formatting
        + Bannded function checks
    3. Integration testing
    4. Security testing
    5. TDD/BDD/ATDD
        1. Test-driven Dev  - Test schreiben, bevor man Code schreibt
            1. State desired outcome as a test
            2. Write code to pass the test
            3. Repeat
        2. Behavior-driven Dev - 
            1. Work with stakeholders
            2. Describe business functionality
            3. Test are based on natural language desctiptions (DSL)
        3. Acceptance-test-driven Dev
            * bauet auf TDD und BDD
            1. End user perspective
            2. Use case automated testing
            3. Testing is continuous during Dev
    6. Infrastructure testing
        * 
    7. Performance testing
        * Bsp: Webseite testen
            1. XSS-Attacke testen
            2. 
    8. Security Testing
* Techniken gegen langsam Test, die z.B Kaffe-Pause-Zet (siehe oben) überschreiten 
    1. Nonblocking Test in der Pipeline benutzen
    2. Time-Scheduled Tests (aka nightly test Suite benutzen)
    3. Use monitoring to accomplish some test goals
#### 5 - Your CI toolchain
* also Tools für Continuous Delivery
    1. Version Controll
    2. CI Systems (Continues Integration)
        * Jenkins, Teamcity usw.
    3. Build
        * make, rake, 
        * maven - 
        * gulp
        * packer
    4. Test
        * Unit Testing 
            * jUnit
            * golint/gofmt
        * Integration Testing
            * Robot
            * Protractor
            * Cucumber
            * Selenium
            * Sauce Labs
            * Kitchen CI für Chef
        * Performance Testing
            * ApacheBench
            + JMeter
        * Security Testing
            * Brakeman - Codeinspection
            * Veracode - Codeinspection
            * (Galen) - CSS-Tests
            * Grendel
            * Mitten
    5. Artifact repository
        * Artifactory
        * Nexus (open source)
        * Docker hub
        * AWS S3
    6. Deployment
        * Rundeck
        * UrbanCode
        * ThoughtWorks
        * Deployinator (kostenlos)
### 6 - Reliability Engineering
#### 1 - Engineering doesn't end with deployment
* Reliability - System soll funktionierten unter bestimmten Konditionen bestimmte Zeit
    * d.h. braucht: availability, performance, security
* 4 Key Areas von DevOps:
    1. Extend delivery to production
    2. Extend operations feedback to project
    3. Embed Project knowledge into Operations
    4. Embed Operations knowledge into Project
#### 2 - Design for operation: Theory
* Software Architecture Side => Design Patterns
    * Bsp:
        1. Circuit Breaker Pattern
            * Netflix-Open-Source-Lib -> Histrix
    * Lesen bzw. auschecken: 
        * The Twelve Factors
        * GitHub-Proj: factorish
        * http://martinfowler.com/bliki
#### 3 - Design for operation: Practice
* Chaos Monkey von Netflix
* Man soll immer damit rechnen, dass etwas ausfällt
* Performance:
    * z.B SW braucht mehr HW
    * Performance Test Tools:
        * Code-Profiler
        * Application Performance Management (Tool-Chain)
#### 4 - Operate for design: Metrics and monitoring
#### 5 - Operate for design: Logging
#### 6 - Your SRE toolchain

### 7 - Additional DevOps Ressources
#### 1 - Unicorns, horses and donkeys, oh my
#### 2 - The 10 best DevOps books you need to read
#### 3 - Navigating the series of tubes

### 8 - The Future of DevOps
#### 1 - Cloud to containers to serverless solutions
#### 2 - The rugged frontier of DevOps: Security
