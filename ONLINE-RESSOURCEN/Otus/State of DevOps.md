### State of DevOps 2020
DevOps = Praktiken
1. z.B Continures Delivery
    * Build -> Test/Tests -> Deploy  

Dabei muss man Qualität des Code beobachten. Dann entsprechendes Tun z.B Roll-backen. 

DevOps:
1. Continous Delivery
2. Continous Integration = alle integrieren ihren Code zum gemeinsamen Code => dann muss getestet usw. dann an Kunden ausgeliefert.
2. Infrastructure as Code (Terraform, Cloudformation). (Kubernetes, Ansible, SaltStack usw. ist nicht wirklich IAC)
3. Deploy Politic
    1. Rolling Deployment = einzelne Apps updaten
    2. BlueGreen Deployment = zwei Versionen des Releases  (z.B 10% eine 90% andere und checken was gut/schlecht)
    3. Canary Release
4. Monitoring = Observation z.B Prmetheus = Metriken der App checken z.B Logs, OS-Metriken usw.  


DevOps-Buch: DevOps Handbook von Gene Kim, Jez Humble; Roman Project Phoenix  
DORA ~ Standartisierung von DevOps  
Knowledge Sharing:
1. Außere Quellen
2. Innere Quellen
* sollten kombiniert werden.

Googeln:
1. Quees Ingeniering -> Netflix -> Utility Quees Monkey

### DevOps Einführung:
1. DevOps - Einführung = DevOps Kultur; DevOps Ingeneering; DevOps Entwicklung 
2. Infrastruktur und Konfiguration = Infrastructure as Code (Git, Terraform, Ansible)
3. Continuous Integration & Continuous Delivery (Gitlab, GitlabCI, Docker; Deploy Strategie, Testing, Business Management)
4. Fast Feedback Loop (Monitoring + Logging = Metriken der Services)
5. Container Orchestration (Kubernetes)