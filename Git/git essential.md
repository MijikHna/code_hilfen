# Git Essential

## 1 - What is git
### 1 - Versionskontrollen <-Geschichte
> 1. SCCS (Source Code Control System)
> 2. RCS (Revision Control System)
> 2. CVS (Concurrent Version System)
> 4. SVN (Apache Subersion)
> 5. BitKeeper (SCM) <- closed source

## 2 - Installing Git:
### 1 - Git Configuration
>1. System -> /etc/gitconfig bzw. \Program Files\Git\etc\gitconfig
>> * `git config --system`
>2. User -> ~/.gitconfig bzw. \$HOME.gitconfig
>>* `git config --global`:
>>   * `git config --global user.name "Lala Lala"` 
>>   * `git config --global user.email "lala@lala.com`
>>   * `git config --list` - Alles anzeigen
>>   * `git config --global core.editor "nano"/"emacs"/"vim"/"mate -wl1"/"nodepade.exe"` - Standardeditor auswählen + Optionen für den Editor. `w`-Warte, `l1`-beginne bei Zeile 1
>>   * `git config --global core.ui true` - Farbe benutzen

>3. - Project -> my_project/.git/config

>4. - git config

### 2 - Git Auto-ComplitionScript
>1. Windows hat schon Auto-Complition

>2. Vorgehensweise:
>    * Autocomplition von github herunterladen
>    * Umbennen
>    * in .bashrc hinzufügen (siehe Bash ist implementiert) 
## 3 - Getting Started
### 1 - git add .
> `git add .` - alle Dateien auf ein Mal hinzufügen

### 2 - Best Practices für git-Kommentare
>1. max 50 Buchstaben
>2. Wenn mehr => eine leere Zeile dann mehr Beschreibung + max. 72 Buchstaben
>3. Bsp für Kommentar: `fix bug` oder `fixed bug` nicht `fixed a bug`
>4. Ticketnummer  hinzufügen bzw. Bugnummer was z.B. `js/css` usw.

### 3 - View commit log
>1. `git log` - Commit History anzeigen
>2. `git help log`
>3. `git log -n 1` - wie viele
>3. `git log --since==2012-06-15` - Commits ab anzeigen
>3. `git log --until==2012-09-18` - Commits bis 
>4. `git log --author="Kirill"`
>4. `git log --grep="Teil des Commits"` - zeigt Commits an, die `..` beinhaltet

## 4 - Git Concepts and Architecture
### 1 - Git benutzt Drei-Baum-Architekture, andere Versionierungstool benuten Zwei-Baucm-Architektur
>1. Zwei-Baum-Arch
>>1. Repository und Working Direktory
>>>1. `checkout` - aus Repository nach Working
>>>2. `commit` - aus Working nach Repository

>2. Drei-Baum-Arch
>>1. Repository, Staging + Workong Direktory
>>>1. `add` -  aus Working nach Stagin
>>>2. `commit` - aus Working nach Repository

### 2 - Working with the HEAD pointer
>1. `HEAD` zeigt auf den letzen Commit
>>1. `HEAD` ist wichtig beim Arbeiten mit Branches
>2. `HEAD` zeigt auf den letzten Commit des aktuell ausgwählten Branches
>3. `git log HEAD` - zeigt alle Commits beginnend bei `HEAD`  
## 5 - Making Changes to Files:
###1. Adding Files:
>1. Untrackted Files - Dateien, die von git nicht beobachtet werden (sind in Working)
>2. Changes to be committed - Dateien, die in Staging sind

### 2 - Editing Files:

### 3 - Viewing changes with diff
>1. `git diff` - zeit Unterschiede zwischen Repository und Working
>2. `git diff Dateiname.end` - zeigt Unterschiede bestimtmer Datei

###4 - Viewing only staged changes
>1. `git diff --staged` - zeigt alle Unterschiede zwischen Repository und Working
>2. `git diff --cached` - veraltet 

### 5 - Deleting Files
>1. Datei löschen -> `git rm DateiName.end`  
>ODER
>2. `git rm DateiName.end` 

### 6. Moving and renaming files
>1. `git rm dateiAlt.end` -> `git add unbenannteDatie.end`  
>ODER
>2. `git mv dateiAlt.end dateiNeu.end` oder `git mv dateiAlt.end Ordner\dateiNeu.end`

## 6 - Using Git with a Real Project
>1. **-+SHIFT+S** - in git-Terminal <- man kann das in config einstellen. 
>2. `git dif --color-words datei.end` - zeigt farbig, was genau geändert wurde.
>3. `git commit -am "Kommentar"`- `commit` und `add` in einem. !Aufpassen, wird alles Commit.
>4. `git rm alt.end neu.end` stat `mv alt.end neu.end`
>5. `git add ordner/` - wird alles geaddet, was im Ordner ist 

## 7 - Undoing Changes
### 1 - Undoing in Working
>1. `git checkout datei.end` - einzelne Dateien zurückholen vom letzten Commit
>2. `git checkout ordner\` - Ordner zurückholen
>3. `git checkout -- datei.end` - Datei aus dem aktuellen Branch zurückholen 

### 2 - Undoing in Stage
> 1. `git reset HEAD datei.end` - datei.end in Staging auf den letzten Commit bringen

### 3 - Undoing in Repo
>1. `git add datei.end; git commit --amend - "letzter Kommentar` - Änderungen zum letzten Commit hinzufügen. Damit kann man auch nur Kommentare ändern
### 4 -  
> 1. `git checkout sha-commit-nummer -- datei` - (reichen ersten 10 Zeichen) Datei aus beliebigem Commit in Staging holen

### 5 - Revert
>1. `git revert sha-commit-nummer` - wird neuer Commit erstellt, der alle Änderungen im Commit umkehrt.
>2. `git revert -- sha-commit-nummer` - wie oben nur wird auf Staging angewandt, also kein neuer Commit erstellt.
### 6 - Mehrere Commits zurücksetzen - HEAD zurücksetzen (git reset)
>1. Commits danach werden überschrieben, da der revertete Commit nicht mehr erreichbar wird.
>>1. `git reset --soft ` - HEAD wird zurückgesetzt, sonst nichts gemacht, also Working bleibt unangetastet
>>2. `git reset --mixed` - HEAD wird zurückgesetzt + Staging wird auf den HEAD gesetzt (ist default)
>>3. `git reset --hard` - wird alles auf HEAD gesetzt

### 7 - Demonstrating a soft reset
>1. `git reset --soft sha-nummer-des-commits` 
>2. `git log` - HEAD zeigt auf den commit aus 1)
>3. `git status` - in Working ist noch die aktuelle Datei
>4. `git reset --soft sha-nummer-des-alten-HEAD` - muss aber vorher irgendwo aufschreiben.
>>1. ← Tipp: ein paar aktuelle Commits in .txt kopieren

### 8 - Deonstraiting mixed reset
>1. `git reset --mixed sha-nummer-des-commits` 
>2. `git status` 
>3. `git diff`
>4. `git reset HEAD datei.end` - add zurückmachen => Staging zurücksetzen

### 9 - Demonstraiting hard commit
>1. `git reset --hard sha-nummer-des-commits` 
>2. `git log`
>3. `git status` - alles aktuell => Datei in Working wurde auch zurückgesetzt.

### 10 - Removing untracked files
>1. `git clean -n` - zeigt, welche Dateien git entfernen würde = Test
>2. `git clean -f` = löschte wirklich.

### 8 - Ignoring Files
>1. Using .gitignore files
>>1. .gitignore-Datei in Projekt-Ordner erstellen
>>2. Regulare Ausdrücke:
>>>1. `*,?[a-x]`
>>>1. `*.php`
>>>2. `!datei.php` - nicht ignorieren
>>>3. `ordner/ordner/`
>>>4. `#` - Kommentare
>>>5. `.DS_Store`
>>>6. `*.zip`
>>>7. `*gz`
>>>8. `log/*.log`
>>>9. `log/*.log.[0-9]`
>>>10. `assets/video/`
>>>11. `!assets/video/la_*.mp4`
>>2. .gitignore
>>>1. `nano .gitignore` - .gitigbire öffnen
>>>1. .gitignore Verändern
>>>2. `Shift+X` - .gitignore speichern
>>>3. `Y` - YES
>>>4. `.gitignore` - 

>2 - Understanding what to ignore
>>1. kompilierter Code
>>2. packages + zips usw.
>>3. logs und Databases
>>4. OS generierte Dateien
>>5. User-uploades Assets (images, Pdfs, videos)
>>6. Tips zum Ignorieren:
>>>1. https://help.github.com/articles/ignoring-files
>>>2. https://github.com/github/gitignore

>3 - Ignoring files globally
>>1. z.B um OS-Dateien zu ignorieren
>>>* `git config --global core.excludesfile ~/.gitignore_global`

### 4 - Ignoring tracked files
>`git rm --cached datei.txt` = aus Staging löschen = wird nicht mehr getrackt
### 5 - Tracking empty directories
>1. da git keine leeren Ordner trackt => eine Datei anlegen:
>>* `touch .gitkeep` - Datei anlegen, damit ein lerere Ordner getrackt wird 

## 9 - Navigating the Commit Tree
### 1 - Referencing commits
>1. Referenz zeugt auf Commit 
>2. tree-ish ist bzw. kann sein:
>>1. full sha-1 hash
>>2. short sha-1 hash
>>>1. at least 4 chars
>>>2. (8-10) Zeichen
>>3. HEAD Zeiger
>>4. Branch Referenz
>>5. Tag Referenzen
>>6. Ancestry
>3. parent commit suchen:
>>1. HEAD^
>>2. sha-1^
>>3. master^
>>4. HEAD~1
>>5. HEAD~
>4. grandparent commit
>>1. HEAD^^
>>2. sha-1^^
>>3. master^^
>>4. HEAD~2
>5. grear-grandparent commit
>>1. HEAD^^^
>>2. sha-1^^^
>>3. master^^^
>>4. HEAD~3

### 2 - Exploring tree listings
>1. `git ls-tree HEAD` - zeigt an, was *tree* und *blob* ist
>2. `git help ls-tree`
>3. `git ls-tree master ordner/` - zeigt an, was *tree* und *blob* im bestimtmen Branch und Order ist
>>1. **blob** - Datei
>>2. **tree** - Ordner

### 3 - Getting more from the commit log
>1. `git log --oneline` - Ausgabe einzeilig
>2. `git log –oneline -3` - einzellig 3 Commits anzeigen
>3. `git log --since=“2010-02-20“` 
>4. `git log --until=“2010-10-10"` 
>5. `git log --since=2.weeks --until=3.days` 
>6. `git log --author=„kirill“`
>7. `git log --grep=“temp“` - werden alle Commits angezeigt, wo temp irgendwo vorkommt
>8. `git log sha-1-num1..sha1-num2` - Commit von num1 bis num2 anzeigen
>9. `git log sha-1-num1… datei.html` - zeigt, wie datei.html bis Commit ..num1 passiert ist
10. `git log -p  sha-1-num1… datei.html` - `-p` zeigt auch was im Code verändert wurde
11. `git log --stat --summary` - zeigt Statistiken zu den Commits an
12. `git log --format=oneline` 
13. `git log --format=short/medium/full/fuller/email/raw`
14. `git log --graph` 
15. `git log --oneline --graph --all –decorate`

### 4 - Viewing Commits
>1. `git show sha-1-commit`
>2. `git show --format=oneline HEAD`
>3. `git help show` - als Arguments kann Commit, Ordner, Datei als sha-1
>>1. `git ls-tree master`
>>2. `git show sha-1-tree/blob` - zeigt dann einfach den Inhalt von Order/Datei

### 5 - Compare Commits
>1. `git diff` - Unterschiede zwischen Staging und Working
>2. `git diff --cached` - Unterschiede zwieschen Staging und Repo
>3. `git diff sha-1commit` - Unterschiede zwischen dem Commit und Working
>4. `git diff sha1-commit datei.html` - Unterschiede zwischen dem Commit und Working in der Datei datei.html
>5. `git diff sha1-commit..sha1-commit2` - Unterschiede zwischen den 2 Commits
>6. `git diff sha1-commit..sha1-commit2 datei.html`
>7. `git diff sha1-commit..HEAD`
>8. `git diff --stat --summary sha1-commit..HEAD`
>9. `git diff -b sha1-commit..HEAD` - (`-b` = --ignore-space-change)
>10. `git diff -w sha1-commit..HEAD` - (-w = --ignore-all-spaces)

## 10 - Branching
### 1 - Branching overview
>1. wofür Branches:
>>1. neue Ideen ausprobieren
>>2. einzelne Features
>>3. beim Wechseln des Branches = fast Context Switching = beim Branch-wechsel wird Working auf den Stand von Branch gesetzt
### 2 - Viewing and creating Branches
>1. `git branch` - zeigt auf welchem Branch man gerade ist
>2. alle Branches werden in `.git/refs/heads` gespeichert 
>3. `git branch new_feature1` - Branches anlegen
### 3 - Switching branches
1. `git checkout branch_name`
### 4 - Creating and switching branches
>1. `git checkout -b new_branch_name` - Branch erstellen und direkt wechseln
>2. `git log --graph --decorate --all` - zeigt welcher Branch an welchem Commit ist
### 5 - Switching branches with uncommitted changes
1. um zu switchen, muss Working saube sein = keine Änderungen = Dateien die schon getrackt werden, müssen sauber sein.
### 6 - Compare Branches
>1. `git diff master..branch2` - zeigt Unterschiede zwischen beiden HEADs von den 2 Branches
>2. Reihenfolge der Branches ist eigentlich egal.
>3. `git diff --color-words branch1..branch2` - zeigt die Änderungen in einer Zeile farbig
>4. `git diff --color-words branch1..branch2^`
>5. `git branch --merged`  - zeigt Branches, die in Momentanen reinlaufen (=merged Branches in Momentanen)
### 7 - Rename Branches
>1. git branch -m/--move alter_branch_name neuer_branch_name
### 8 - Deleting Branches
>1. `git branch -d/--delete branch_name` - löscht den Branch nicht, wenn man auf dem Branch ist
>>2. `git branch -D branch_name` - falls Branch nirgendwohin führt wird `git branch -d branch_name` verweigert, da damit die Änderungen (=Commits nach der Brancherzeugung) verloren geht, sollte man Branch mergen, bevor man ihn löscht (=> -D = lösche trotzdem)
### 9 - Configuring the command prompt to show the branch
>1. `__git_ps1` - Funktion, die zeigt den Branchname in Terminal an
2. `$PS1` - Promt String1 -> hier/in dieser Variablen ist Prompt gespeichert 
3. wenn man Promt auf etwas andere setzen möchte:
1. `export PS1=‘lala $ ‘` - man sollte am Ende Leerzeile machen, da sonst Cursor direkt nach `$` laufen würde
2. `export PS1=‘\W$(__git_ps1 „(%s)“ >‘` - (`\W` - der Verzeichnis), (`„(%s)“` - Format string hier wird die Ausgabe von `__git_ps1` stehen)
3. 2 in `.bashrs` einfügen

## 11 - Merging Branches
### 1 - Merging code
>1. auf den Branch wechseln in den gemerged werden soll
>2. `git merge branch_name`
>3. **!!!** mit sauberer Working mergen
### 2 - Fast-Forward merge vs. true merge
>1. Fast-Forward - HEAD von zu mergendem Branch wird zum neusten Commit auf dem gemergtem Branch
>>1. `git merge --no-ff branch_name` - (`--no-ff` - no FastForward)
>>2. `git merge –ff-only branch_name` - Mache nur FastForward, falls nicht möglich dann breche ab
>2. True Merge = erstellt neuen Commit auf dem aktuelle Branch aus dem zu mergendem Branch und aktuellem HEAD
>>1. `git merge branch_name`
>>2. \+ wird nach Kommentar verlangt → nur Enter drucken => übernimmt den Kommentar vom zu mergendem Branch
### 3 - Merging conflicts
>1. Konflikt = wenn auf Branches gleiche Zeile verändert wird, sonst nicht
2. `git log branch_name` - zeigt Commits auf dem angegebenem Branch
3. git markiert mit `>>>>>HEAD/Branchname … ===== die Konfliktzeilen in Working` die Zeilen in der Datei im Konflikt sind und öffnen im editor. Den Konflikt auflösen und die `>>>>>HEAD/Branchname … =====`-Zeile löschen und Editor schließen.
### 4 - Resolving merge conflict
>1. 3 Optionen:
>>1. Merge abbrechen
>>2. Manuell auflösen
>>3. merge tool benutzen
>2. Merge abbrechen
>>1. `git merge --abort` 
>3. Manuell auflösen:
>>1. Datei öffnen → löschen die Markierungen und Zeile behalten, die man behalten will → `git status` → `git commit` → Conflicts-Zeilen löschen + Enter
>4. Merge tool:
>>1. `git mergetool` - zeigt Mergetools an
### 5 - Exploring strategies to reduce merge conflicts

## 12 - Stashing Changes
### 1 - Saving changes in Stash
>1. vierte Dimension in git = zwischenspeichert keine Commits, sondern Snapshots + haben keine sha1-nummer
>2. `git stash -m „kleiner Kommentar“` - Kommentar, damit man später weiß, wieso man gestasht hat
### 2 - Viewing stashed changes
>1. `git status` - wird `stash@{0}` on `branch_name` als letzter Commit angezeigt.
>2. `git checkout branch_name` = zum Branch mit Stash wechseln
>3. `git stash list`
>4. `git stash show stash@{0}`
>5. `git stash show -p stash@{0}` - detalierter

### 3 - Retrieving stashed changes
>1. es können auch Konflikte entstehen
>2. `git stash pop stash{0}` oder `git stash apply stash@{0}` - wenn man stash@{} nicht angibt => wird der {0} genommen. `applay` - `stash@{}` bleibt in der Stashliste, `pop` - `stash@{}` wird von der Stashliste gelöscht. 
>>1. `git stash pop` - holt es und löscht den Stash auch
>>2. `git stash apply` - holt es aus dem Stash und lässt es in Stash

### 4 - Deleting stashed changes
>1. `git stash drop stash@{x}`
>2. `git stash clear` - löscht ganzen Stash

## 13 - Remotes
### 1 - Using local and remote repositories
>1. **push** - auf Remote Server schieben
>2. **fetch** - vom Remote holen, aber nicht auf dem master ← muss noch merge gemacht werden.
>3. **origin/master** – Pointer zeigt auf gefetchten Commit; master zeigt auf Commit auf dem lokalen Rechner
### 2 - 
### 3 - Additing a remote repository
>1. `git remote`  zeigt Liste mit den Remotes
>2. `git remote add localer_name https://github.com/…` -`localer_name` = meist origin
>3. `git remote -v` = zeigt Liste mit Remotes für fetch und push
>4. in `.git/config` wird `[remote „localer_name“]` angelegt
>5. `git remote rm localer_name` - Remote-Repo löschen
### 4 - Creating a remote repository
>1. `git push -u localer_name master` - den Branch master zu Remote-Repo senden
>2. nach dem Push wird in `.git/config` `[branch „branch_name“]` angelegt:
>3. in `.git/refs/remotes/localer_name` kann man schauen wohin der Pointer zeigt.
>4. `git branch -r` - zeigt Remote-Branches
>5. `git branch -a` - zeigt alle Branches: Remote-Branches und Locale-Branches:
### 5 - Cloning a remote branch
>1. `git clone https://github.com/….git` - Ordner wird erstellt, Name ist vor .git
>2. `git clone https://github.com/….git ordner_name` - clont in den Ordner ordner_name
>3. ← bei default wird nur master-Branch geclont.
### 6 - Tracking remote branches - ???
>1. `git push -u repo master` - `-u` trackt remote-Branch
>2. in `.git/config` in `[branch]` kann man getrackten Branch sehen
>>1. `git config branch.branchname.remote name_des_repos`
>>2. `git config branch.branchname.remote name_des_repos`
>>3. `git branch --set-upstream branchname remote_name/branchname`
>>>1. ← nicht getrackten Branch zum Tracken aufnehmen
>3. ← sonst schauet git nicht nach, ob auf dem Branch etwas verändert wurde
### 7 - Push changes to a remote repository
>1. `git log reponame/master` - schauen, was auf dem Remote ist
>2. `git push reponame master` 
>3. `git push` ← da der Branch getrackt wird, kann man reponame master weglassen
### 8 - Fetching changes from a from repo
>1. `git fetch repo_name`
>2. `git fetch` - falls man nur eine Remoterepo hat
>3. fetchen bevor man mit der Arbeit beginnt
>4. fetchen bevor man pusht
>5. ofters fetchen
### 9 - Merging in fetched changes
>1. macht Fast Forward Merge
>2. `git branch -a`
>3. `git dif master..repo_name/master`
>4. `git merge repo_name/master`
>5. `git pull` - git fetch origin + git merge
### 10 - Checking out remote branches
>1. `git branch branch_vom_remote reponame/branch_name` - `reponame/branch_name`  = von wo der Branch starten soll, default ist HEAD (theoretisch kann man hier beliebigen Commit angeben)
>2. `git checkout -b branch_vom_remote /reponame/branch_name`
### 11 - Push in to an update remote branch
>1. wenn während dem Weiterarbeiten, jemand Remote upgedatet hat => zuerst muss man fetschen, ← git wird den Push verweigern.
### 12 - Delete a remote branch
>1. `git push remote :branch_name`
>2. eigentlich wenn man einen Branch pusht:
>>1. `git push repo branch_name:branch_name` - schiebe zu Repo (lokalen)branch_name:(erstelle remote)branch_name
>>2. `git push repo :branch_name` - ~ so zusagen löschen lokalen branch_name auf der Repo  
>>ODER:
>>3. git push origan --delete branch_name
### 13 - Enabling collaboration
>1. auf github:
>>1. Fork
>>2. am Issue arbeiten
>>3. Pull Request
### 14 - Collaboration Workflow
>1. `git checkout master`
>2. `git fetch`
>3. `git merge repo/master`
>4. `git checkout -b neuer_branch`
>5. `git add .end`
>6. `git commit -m „Kommenatar“`
>7. `git fetch`
>>1. eventuell `git merge repo/master`
>8. `git push -u repo neuer_branch`
>9.  
>10. `git checkout -b neuer_branch repo/neuer_branch`
>11. `git log`
>12. `git show HEAD`
>13.  
>14. `git log -p neuer_branch..repo/neuer_branch`
>15.  
>16. `git checkout` 
>17. `git fetch`
>18. `git merge repo/master` - falls Änderungen auf Remote passiert sind
>19. `git merge neuer_branch`
>20. `git push`

## 14 - Tool and next
### 1 - Setting up aliases for common commands
>1. am besten in global config machen
>>1. `git config --global alias.st status`
>>2. `git config --global alias.st „status“` - `git st` = `git status`
>>3. Standardaliases:
>>>1. `git config --global alias.co checkout`
>>>2. `git config --global alias.ci commit`
>>>3. `git config --global alias.br branch` -  git br -r = git branch -r
>>>4. `git config --global alias.dfs „dfs –staged“`
>>>5. `git config --global alias.logg „log --graph --decorate --oneline --abbrev-commit --all“` - git logg
### 2 - Using SSH keys for remote login
### 3 - Exploring IDEs
>1. sollten git-Features integriert haben (meist als Plugin)
### 4 - Exploring graphical user interfaces
>1. GitWeb ← braucht WebServer = zeigt Commits im Browser
>2. weitere googeln