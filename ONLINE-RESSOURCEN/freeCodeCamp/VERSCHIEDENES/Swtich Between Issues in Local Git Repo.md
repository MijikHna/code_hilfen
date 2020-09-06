### Am Issue arbeiten - Workflow
* `git clone URL`
* `git remote add upstream URL` - Remote Repo nach Änderungen tracken (Upstream = Branch ???)
* `git remote -v`
* `git fetch UPSTREAM(ORIGIN)/MASTER` Upstream/master fetchen (eigentlich wird in den lokalen master/upstream gemerged)
##### Git Branch
* `git checkout -b DESCRIPTIV-BRANCH-NAME` - z.B Issue-Name
* `git checkout -b DESCRIPTIV-BRANCH-NAME TARGET-BRANCH` - statt von aktuellem Branch neuen Branch erstellen von TARGET-BRANCH einen Branch erstellen
* `git branch` - Branches auflisten
* `git push -u origin DESCRIPITV-BRANCH-NAME` - den neuen Branch zu Repo pushen.

### Zwichen den Issues switchen:
* Dafür wird CLI-Tool `hub` (hub utility) verwendet
* Workflow:
    * `hub sync` - bekommt den UPSTREAM und merged den in gerade erstellten Branch
    * `git status`

### Fehler, die gemacht werden können:
1. wenn man bestimmte Commit löschen will:
    1. `git checkout BRANCH`
    2. `git log` - Commit anzeigen
    3. `git log -n 1` - nur den letzten Commit anzeigen
    4. Wenn man jetzt alle Commits außer diesen `-n 1` löscen will:
        1. `git reset --hard UPSTREAM/master` - alle Stated und Unstaged Änderungen verwerfen
        2. `git cherry-pick HASH-N-1-COMMIT` - nur diesen einen Commit auf den Branch anwenden
        3. `git push --force origin` das Ganze auf Repository anwenden. ist GEFÄHRLICHES git Befehl, denn dann sind die Commit entgültig weg

