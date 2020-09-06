`grep` = Globally Search For Regular Expressions and Print out. In Linux, um auf spezifische Pattern in Dateien zu suchen.
* Syntax: `grep PATTERN DATEI.END`
* Optionen:
    1. `-n`/`--line-number` - Line Numbers auflisten: `grep PATTERN DATEI.END -n`
    2. `-c`/`--count` - Anzahl der Matches printen: `grep PATTERN DATEI.END -c` 
    3. `-v`/`--invert-match` - Zeilen, die keinen Match habe printen `grep PATTERN DATEI.END -v`
    4. `-i`/`--ignore-case` - egal ob Groß oder Klein `grep PATTERN DATEI.END -i`
    5. `-l`/`--files-with-matches` - Dateiname mit Matches printen `grep PATTERN DATEI.END -l`
    6. `-w`/`--word-regexp` - nur Match, wenn Wort übereinstimmt, nicht Pattern irgendwo im Text `grep PATTERN DATEI.END -w`
    7. `-o`/`--only-matching` - nur matched Pattern print, statt die Zeile `grep PATTERN DATEI.END -o`
    8. `-A`/`--after-context` bzw. `-B`/`--before-context` - Anzahl der Zeile vor/nach dem Match printen `grep PATTERN DATEI.END -A 1 -B 1`
    9. `-R`/`--dereference-recursive` - rekursives Suchen = Direkory durchsuchen`grep PATTERN . -R` 
    10. Regular Expressions:
        1. `^pattern` Zeile beginnt mit `pattern` `grep ^pattern DATEI.END`
        2. `pattern$$` Zeile endet mit `patttern` `grep PATTERN$ DATEI.END`