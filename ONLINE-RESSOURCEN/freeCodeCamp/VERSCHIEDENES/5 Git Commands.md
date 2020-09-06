1. `git remote add SHORTNAME URL` - Remote-Repo einstellen. Per Default `SHORTNAME` ist `origin`
2. `git remote set-url SHORTNAME NEW-URL` - Remote-Repo ändern
3. `git branch -d BRANCH` - Branch löschen
4. `git push SHORTNAME --delete BRANCH` - Branch auch auf Remote-Repo löschen
5. `git checkout BRANCH` und `git checkout --patch master FILE.END` - FILE.END aus Branche `master` in den Branch `BRANCh` mergen. `git checkout master index.html` - Statt mergen die Datei überschreiben
6. `git reset --soft HEAD~1` -letzten Commit löschen oder `git reset --hard HEAD~1`; `git reflog` - alle Commits davor bekommen. `git revert COMMIT-HASH` und pushen - Commits auch auf Remote löschen.