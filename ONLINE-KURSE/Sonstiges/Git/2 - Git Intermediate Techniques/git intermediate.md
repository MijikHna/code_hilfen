### 1 - Branch Management:
#### 1 - Force push to a remote:
* um z.B. wenn Remote-version ist zu alt
*  `git push -f / git push --force` 
*  = das was im Remote anders ist wird gelöscht und meine Version wird commitet
* ← ist aber gefährlich = wird auf Repo alles gelöscht
* `git push -f` 
* `git reset --hard origin/master` = den forced Commit holen
#### 2 - Identify merged branches:
* `git branch --merged` = zeigt alle Branches, die in momentanen Branch gemerged wurden
*  `git branch --no-merged` = zeigt Branches, die nicht in momentanen Branch gemerged wurden
*  `git branch -r --merged` = zeigt remote Branches, die in momentanen Branch gemerged wurden
*  ← schauet, welche HEADs von anderen Branches erreichbar sind
* `git branch --merged sha1_nummer` = so zusagen sagen das HEAD(Kopf des anderen Branches) sha1_nummer ist
### 3 - Delete local and remote branches:
* `git branch -d branch_name` / `git branch -D branch_name` = lokalen Branch löschen:
* `git push repo_name :branch_name` / `git push --delete repo_name branch_name` / `git push -d repo_name branch_name` = remote Branch löschen
* wenn man Branch lokal löscht => auf dem localen Rechner wird der trozdem Branch getrackt => damit er nicht mehr getrackt wird => `git push -d repo_name branch_name`
#### 4 - Prune Stale Branches:
*  = alte Branches löschen, nicht remote-Branches, sondern getrackte remote-Branches
*  es gibt 3 Remote-Branches:
    *  Branch der im Remote existiert
    * Lokaler Snapshot des Remote-Branches
    * lokaler Branch, der Remote-Branch checkt
* ← wenn jemand den Branch auf Remote löscht => er existiert noch lokal, wird aber nicht mehr getrackt, git fetch macht es nicht automatisch =>:
    * `git remote prune repo_name` = löschte Tracking des gelöschten Branches
    * `git remote prune repo_name --dry-run` = zeigt erst an, was passieren wird
* `git fetch --prune /git fetch -p` = fetch + prune gleichzeitig
* `git config --global fetch.prune true` → in config festlegen, dass bei fetch gleichzeitig geprunet wird
* `git prune` = schneidet alle unerreichbaren Objekte ← ist Teil von git gc
* `git gc` = löscht alle unerreichbaren Objekte (garbage collection)
### 2 - Tagging:
* Create tags:
    * wichtige Commits markieren
    * z.B Releases v1.0, v1.1 usw.
* ligthweight Tag:
    * `git tag tagName sha1_des_Commits`
*  Annotated Tag (mehr gebraucht) = hat noch Kommentar
    * `git tag -a v1.1 -m „Kommentar“ sha1_des_commits` → `-a` = annotated, `-m` = Message oder `-am` => `git tag -am „Kommentar“ v1.1 sha1_des_commits`  → ohne „Kommentar“ => wird Fenster für Kommentareingabe geöffnet
    * `git tag v1.1` => der HEAD wird getagt.
#### 2 - List tags:
* `git tag / git tag --list / git tag -l`
* `git tag -l „v2*“` = filter der Tagliste => nur Tags, die mit v2 beginnen, werden angezeigt.
* `git tag -l -n` = Liste von Tags mit Annotationen öffnen
* `git show tag_num`
* `git diff tag_num1..tag_num2` = Tagged-Commits untersuchen
#### 3 - Delete tags:
* `git tag --delete tag_name`
* `git tag -d tag_name`
#### 4 - Push tags to a Remote:
* Tag werden nicht automatisch gepusht
* => es können eigene Tags 
* => Tags werden aber automatisch gefetcht
* `git push repo_name tag_name`
* `git push repo_name --tags` = alle Tags pushen
* `git fetch --tags` = holte nur Commits, die getaggt sind
* `git push repo_name :tag_name / git push --delete repo_name tag_name / git push -d repo_name tag_name` = Remote-Tags löschen
#### 5 - Check out Tags:
* `git checkout -b neuer_branch_name tag_name`
* `git checkout tag_name` ← verschiebt eigentlich nur HEAD (HEAD detached) auf den Tag  und erstellt von da neuen Tag=> Commits danach werden verloren gehen
    + ← umgehen:
        + `git tag temp` = letzten Commit als temp taggen
        + `git branch temp_branch` = vom letzten Commit Branch bilden (HEAD ist aber immer noch nicht auf letztem Commit)
    * `git checkout -b temp_branch` ← beste Lösung (
    * ← = Branch ab dem Tag bilden
### 3 - Interactive Staging:
#### 1 - Interactive Mode:
* =Interaktives Staging:
+ =Teilen des  Stages 
+ ist ein Feature von Git GUI
+ `git add --interactive / git add -i`
+ `git add -i` → **Enter**
    * wird Liste + Optionen angezeigt = Zahl oder erster Buchstaben
    * update = add => `u` → Dateien auswählen
    * revert = add zurücksetzen => `r` → Dateien auswählen
    * `q` = Interaktiven Modus beenden
#### 2 - Patch Mode of Interactiv Mode:
* = nur Teile der Datei stagen
+ = in Hunk teilen
+ Hunks können gestaget, überlesen, n kleine Hunks geteilt werden
+ Vorgehen:
    1. `git add -i`
    2. `p/5`
    3. Datei auswählen
    4. git entscheidet selber über die Hunks + Optionen unten angezeigt
        * Optionen-Bedeutung anzeigen => ? eingeben
    5. y/n 
    6. <=> geht zum nächsten Hunk
+ in Patch Mode kann man von überall gehen
    1. `git add --patch / git add -p`
    2. `git stash -p`
    3. `git reset -p`
    4. `git checkout -p`
    5. `git commit -p`
    6. `git add -p datei.end` = Patch-Mode für bestimmte Datei
### 3 - Split a hunk:
* `git add -i`
* p
* Datei auswählen => Hunk werden angezeigt
* s=Änderungen hunken:
    * Wenn keine unveränderte Zeile gibt => git kann es noch kleiner unterteilen
#### 4 - Edit a hunk:
* = Hunk manuell bearbeiten <= verwendet, wenn man Hunk automatisch nicht unterteilt werden kann.
* = in Datei gehen und diff modifizieren mit +,-,#, Leertaste
    * Jeder unveränderte Zeile in Diff hat Leertaste
* Vorgehensweise:
    1. `git add -i`
    2. `s` = status
    3. `p` = patch-mode
    4. Dateiauswählen
    5. `s` = split
    6. `e` = manuelles Bearbeiten
    7. Datei datei.diff in Editor öffnen
    8. z.B –/+ zu Leertaste
        * speichern
    9. weiter in git mit Hunk weitermachen
### 4 - Share Select Changes: = zwischen Repositorys und Branches 
#### 1 -  Cherry-picking commits:
* Veränderungen von einem oder mehreren Commits (z.B von anderem Branch) übernehmen
* => existierende Commits werden als neue Commits in dem Branch aufgenommen
* ähnlich wie Copy-Paste
* => neue Commits bekommen andere SHA-Nr
* `git cherry-pick sha_commit` / `git cherry-commit sha_commi1..sha_commit2`
    1. ← Merge-Commit können nicht cherry-gepickt werden
    2. mit `--edit/-e` kann man Commit-Kommentar eingeben
    3. ← kann Konflikte verursachen
#### 2 -Resolve cherry-pick conflicts:
* => wie normalen Commit-Konflikt auflösen => in der Datei die richtige Veränderung auswählen
    * `git cherrry-pick --continue` = mit Cherry-pick fortsetzen
#### 3 - Create Diff Patches:
* Veränderungen mit Hilfe der Dateien teilen:
* = nützlich, wenn die Veränderung noch nicht bereit sind für den Repo-Branch + für Coworker, die die gleiche Remote-Repo nicht mit mir teilen  + für Diskussion usw.
* `git diff from-commit to-commit > output.diff` 
    1. `git diff sha_1 sha_2` = wird im Terminal 
    2. `git diff sha1 sha2 > ~/Schreibtis/for_review.diff`
* Apply diff patches:
    1. = .diff in Working anwenden
    2. `git apply datei.diff`
    3. Bsp: Vorgehensweise:
        1. `git checkout -b teste HEAD` = neuen Branch erstellen
        2. `git apply datei.diff`
        3. `git status`
        4. `git diff` = Veränderungen anschauen
    4. Manchmal geht apply schief ← wenn die Unveränderten Zeilen anders sind. => Working sollte in einem Stand sein, in dem der .diff angewendet werden kann.
#### 5 - Create formatted patches:
* = jeden Commit in Unix-Mailbox-Format exportieren ← für Email distribution der Änderungen + fügt Commit-Kommentar als Meta-Data
* eine Datei pro Commit:
* `git format-patch sha1..sha2`
* `git format-pacht branch_name` = ganzen Branch exportieren
* `git format-patch -1 sha1` = nur einen bestimmten Commit exportieren
* `git format-patch master -o Ordner/Ordner` = Dateien in bestimtmen Ordner ablegen, sonst immer im aktuellen Verzeichnis
* `git format-patch master --stdout > datei.patch` = alles auf stdout ausgeben, stdout dann in datei.patch umleiten
* Apply formatted patches:
    1. Extrahiert den Inhalt und fügt diesen in aktuellen Branch + ähnlich wie cherry-picking + ← dabei wir die Commit-history mitübertragen
    2. `git am  Ordner/datei.patch` => `am` = Apply Mailbox
    3. `git am Ordner/*.patch` => alle extrahieren
        1. ← eventuell neuen Branch erstellen
### 5 - Rebasing:
#### 1 - Rebase commits:
* = Commits von einem Branch als Commits auf anderem Branch duplizieren
    1. = aktuelle Commits ohne Mergin anwenden => saubere + lineare Projekt-History
    2. ← große Teams bevorzugen Rebase statt Merge
* = verschiebt Commits des aktuellen Branches auf den Anfang des anderen Branches ~ Commits vom anderen Branch werden reinkopiert vor den Commits des aktuellen Branches 
    1. => die sha-Nummer der Commits der aktuellen Branches werden verändet
* git rebase branch = aktuellen Branch auf das Ende von Branch branch verschieben
* git rebase branch branch_zu_verschieben = Branch branch_zu_verschieben an das Ende des Branches branch
* `git log --graph --all --decorate --oneline` 
* `git merge-base branch branch_zu_verschieben` = ??
####  2 - Perform a rebase:
* Bsp:
    1. `git branch -t newer_branch`
    2. `git checkout master`
    3. `git commit -am „lala“`
    4. `git log --graph --all --decorate --oneline` 
    5. `git merge-base master new_branch` 
    6. `git checkout camping`
    7. `git rebase master`
    8. `git log --graph --all --decorate --oneline` 
#### 3 - Merging vs. Rebaising:
* Merge:
    1. erstellt neuen Merge-Commit
    2. nicht destruktiv
    3. ← wird festgehalten, was und wann passiert ist
    4. leichter zurückzusetzen
    5. Logs nicht linear
* Rebasing:
    1. kein zusätzlicher merge-Commit
    2. destruktiv = sha wird geändert
    3. nicht festgehalten, was und warum passiert ist
    4. kompliziert zurückzusetzen
    5. Logs sind sauberer und linearer
* Golden Regel des Rebases:
    1. Thou shalt not rebase a public branch
    2. benutzen an localen Branches und Branches, die nur ich benutzen
    3. 
* Resolve rebase conflicts:
    1. git pausiert Rebase => um Konflikte zu lösen:
    2. `git rebase --continue` = nach dem die Konflikte geändert wurden
    3. `git rebase --skip` = den konfrontierenden Commit aus dem Rebase auslasssen → wenn der konfrontierenden Commit schon eigentlich im Code vorhanden
    4. `git rebase --abort`
    5. Bsp:
        1. `git rebase master my_branch`
        2. => Konflikt
        3. im Editor Konflikt auflösen
        4. `git add datei.end` ← Datei die man korriegiert hat
        5. `git rebase --continue`  ← man braucht keine -m „Kommentar“, da es ja Rebase ist
#### 5 - Rebase onto other branches:
* = Branch zum anderen Brachen verschieben
* `git rebase --onto new_base upsteam branch`
    1. `git rebase --onto zu_diesem_branch an_welchem_brach_aktuell branch_name`
#### 6 - Undo a rebase:
* `git reset --hard ORIG_HEAD`
    1. `ORIG_HEAD` = trackt, wo die Sachen wären, wenn man rebase, reset, merge change ← wenn man nochmal rebaset => ORIG_HEAD wird geändert
    2. `git rebase --onto sha_commit an_welchem_branch_aktuell branch_zu_undo`
#### 7 - Interactive rebaising:
* = Commit modifizieren bevor man rebast 
* = git-rebase-todo bearbeiten
    1. man kann Commits mitnehmen, oder auslassen
    2. Commitkommentar und Commit selbst bearbeiten
    3. mehrere Commits zu einem machen
* `git rebase -i base_branch aktueller branch`:
    1. wird git-rebase-todo Datei geöffnet, was anzeigt, was es machen wird
    2. git-rebase-todo schließen => wird rebase gemacht
* Bsp:
    1. `git rebase -i HEAD~3` = letzten Drei Commit rebasen = eigentlich heißt nur die letzten drei Commits bearbeiten
#### 8 - Squash commits:
* = mehrere Commits zu einem machen
* = bei mehreren Authoren nimmt den ersten
* squash = diesen Commit in den Commit davor einfügen
* fixup = 
* ← man muss Commit-Kommentar auch bearbeiten
#### 9 - Pull rebase:
* = beim von Remote-Pull rebasen
* Pull = Commits holen und Mergen mit der lokalen Repo
* => History ist saubereer
* `git pull --rebase` 
* git pull -r
* git pull --rebase=preserve 
* git pull --rebase=interactive 

### 6 - Track Down Problems:
#### 1 - Log options: 
* = Debuggin Code
* **git log** 
    1. hat mehrere Optionen => `git help log`
    2. `git log -p / git log --patch` = Commits + deren Diffs anzegien
    3. `git log -L 100,150:datei.end` = `-L xxx/xxx` = Diffs der Zeilen anzeigen
       1. ← Anzeige wird mit `less` gemacht → `man less`
#### 2 - Blame:
* = aderes debugging tool
* = annotierte Dateien durchsuchen 
* = schauen, wer welche Zeile verändert hat ← Schuldigen suchen:
    1. `git blame datei.end`
    2. `git blame -w datei.end` = die Änderungen der Leerzeilen skippen
    3. `git blame -L 100,500 datei.end`
    4. `git blame -L 100,+5 datei.end`
    5. `git blame sha_commit datei.end` 
    6. `git blame sha_commti – datei.end`
    7. da blame sich unschön anhört => guter Still alias zu blame erstellen:
        1. `git config --global alias.praise blame`
* `git annotate datei.txt` = annotate ähnlich wie blame
#### 3 - Bisect:
* = Debugging tool
* = Commit mit Bug suchen
    1. = letzten guten Commit und ersten schlechten Commit dem bisect sagen
    2. => resetet den Code zu Mittelpunkt
    3. `git bisect start` = Bisect-Session wird gestartet
    4. `git bisect bad <treeish>`
    5. `git bisect good <treeish>`
        1. zu 4. und 5. = setzt HEAD+Working auf den Commit
    6. `git bisect reset`
    7. Vorgehensweise:
        1. `git log` → z.B anhand des Commit-Kommentars schauen welche Commit gut schlecht ist
        2. `git bisect start`
        3. `git bisect bad` = letzter Commit
        4. `git bisect good sha_num`
        5. ← Test laufen lassen
        6. `git bisect good` = letzer Commit + (Commits dazwischen/2)
        7. ← Tests laufen lassen
        8. `git bisect bad` 
        9. `git bisect bad`
        10. ← gefunden 
        11. `git bisect reset`