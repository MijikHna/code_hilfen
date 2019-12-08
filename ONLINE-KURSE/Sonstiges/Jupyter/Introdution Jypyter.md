### 1 - Gettin to know Jupyter
#### Installing Jupyter
* am liebsten mit Anaconda installieren
    * Anaconda installiert direkt 
        * Python
        + Jypyter
        + NumPy, pandas, usw
        + Anaconda Navigator + Conda Package Manager
* Distribution - Kollection von Packages
* 
#### Running your Jupyter notebook
1. Notebook starten
    * Terminal öffnen (davor `source prog/anaconda3/bin/activate`)
    * `jupyter notebook`
    * falls man Browser geschlossen hat => aus Terminal den Link kopieren
    * Beenden:
        * zwei Mal `STRG+C` + `y` oder `Quit` in Jupyter Notebook
* File -> Save - erstellt Checkpoint (Backup)
* File -> Revert to Checkpoint - zu diesem Backup 
zurückkehren
#### Jupyter interface
* 3 Tabs:
    1. Files
    2. Running - laufende Notebook-Dateien
    3. Cluster - für parallele Environments
* Notebook auswählen
    1. Dupclicate
    2. Shutdown
    3. View - 2 Variante um Notebook anzuschauen
    4. Edit - wird in JSON-Format geöffnet
    5. Rename (nur wenn Notebook nicht läuft)
    6. Move (nur wenn Notebook nicht läuft)
* `Shift+Enter` - Zelle ausführen + zur weiteren Zelle gehen
* Es gibt `In` und `Out` - Zellen
```python
import natplotlib.pyplot as plt
greeting = "Hello Jupyter"
words = greeting.split(" ")
word_length = [len(w) for w in words]
plt.bar(words,word_length)
plt.show()
```
* mit den Up/Down- Buttons kann man Zellen nach oben/untern verschieben
* in der Auswahl Menü kann Eingabe für die Zelle auswählen
    1. Code - Python-Code
    2. Markdown - zur Beschreibung des Codes
* daneben gibt es Command-Palette
### 2 - Working Efficiently with Jypyter
#### 1- Modes
* Grün - Edit-Mode
* Blue - Command-Mode -> `Esc`
    * man kann auch mehrere Zellen auswählen und auf diese Comamnds anwenden
* KeyBoard Shortcuts - Hilfe für Shortcuts in Edit- und Command-Mode   
#### 2 - Shortcuts
* Edit-Shortcuts.
    * `STRG+UpArrow` - zum Beginn der Zeile bewegen
    * `STRG+\` - Python-Kommentar einfügen
    * `ALT+Left/Right` - Wortweise springen
    * `STRG+Del` - Wort löschen
    * `STRG+Z` - Undo
    * `SRTG+SHIFT+Z` - Redo
    * `ALT+Enter` - Zelle ausführen + darunter neue Zelle erstellen
    * `STRG+Enter` - Ausführen + in der gleichen Zelle bleiben
    * `STRG+SHIFT+-` - Zelle Teilen
* Bsp:
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("../../xx.csv)
df_week1 = df[df["date"].between["2013_01_01", "2013_01_07"]]
df_week2 = df[df["date"].between["2013_01_08", "2013_01_15"]]
plt.plot(df_week1["Air_Temp1"])
plt.plot(df_week2["Air_Temp2"])
```
+ Command-Mode
* `SHIFT+UpArrow/DownArrow` - mehrere Zellen auswählen
* `SHIFT+m` - Zellen verbinden
* `c` - Copy
* `v`- Paste
* `o` - Output aus/einmachen
* `h` - zeigt Help
* `p` - öffnent Comamnd-Palett

#### 3 - Line magic commands
* Syntax ähnlich wie für Bash (nicht Python Syntax)
* beginnen mit `%`
* 2 Typen
    1. Line Magics
        * `ls`, `mv`, `cat` usw
        * Bsp: 
            * `%laod helper.py`
            * `%cat file.py`
            * `%run file.py param1 param2`
            * `%time sum(x for x in df["Air_Temp"])/len(df["Air_Temp"])` - CPU-Zeit zu messen
            * `%timelt df["Air_Temp"].mean()` - CPU-Zeit zu messen
            * `%system grep suchenString datei | wc -l`
            * `Out[index]` - Output-Zelle nochmal ausgeben
    2. Cell Magics

#### 4 - Cell magic commands
* muss erste Anweisung in der Zelle sein
* beginnen mit `%%`
* manche Commands sind Cell und Line Commands
* Bsp:
    * `%%writefile pythonFile.py ...python Code` - Code in eine Datei speichern
    * `%%capture chart run ... pythonFile.py` Output in Variable chart spiechern
        * `chart.show()`
* `%lsmagic`
* `%magic` - Info zu den Magic-Commands
#### 5 - Cell types
* Zwei Typzellen
    * Code Zelle - wird von Pyhton-kernel interpretiert
    * Markdown Cell (github-Markdown)
### 3 - Effectives Plots for Visualitaion
#### 1 - Using pyplot to visualize data
* `matplotlib.pyplot` - ist Plot-Modul aus `matplotlib`-Bib, die vom Jupyter benutzt wird
* Bsp:
```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("../xx.csv")
?plt.plot # Hilfe für die Funktion/Object aufrufen
% load hours_dict.py # Datei hours_dict.py laden
feb15 = hours_dict.py("2015_02_15")
plt.plot(feb15.keys, feb15.values())
feb16 = hours_dict.py("2015_02_16")
plt.plot(feb16.keys, feb16.values())
plt.xticks(np.arange(0,24,6))
plt.xlim(-3,26)
plt.ylim(-3,28)
plt.xlabel("Hour of the day")
plt.ylabel("Mesurements Taken")
plt.title("Measurements By Hour")
plt.show()
```
#### 2 - Line Graphs
* Syntax:
    * `plot([x], y, [fmt], data=None, **kwargs)`
    * `plot([x], y, [fmt], [x2], y2, [fmt2], ..., **kwargs)
* Bsp:
```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
%load ../helper_funcs/get_df
%load ../helper_funcs/line_helpers.py
def yearly_avg(category):
    return list[map(lambda m: monthly_avg_calc(m, catetory), range[1,13])]
df = get_df("2014")
plt.plot(yearly_av("Wind_Speed"), label="Wind Speed", color="#XXXXXXXX)
plt.plot(yearly_av("Wind_Gust"), "d-", label="Wind Gust", color="#XXXXXXXX)
plt.plot(yearly_av("Dew_Point"), "d-" , label="Dew Point", color="#XXXXXXXX)
plt.plot(yearly_av("Barometer_Press"), label="Pressure", color="#XXXXXXXX)
plt.legend()
plt.show()


```
#### 3 - Bar graphs
#### 4 - Bar graphs with subplots
#### 5 - Tables

### 4 - Publishing and Sharing your Jupyter Notebook
#### 1 - Exporting to HTML and PDF
#### 2 - Distributing on GitHub
#### 3 - Notebook Viewer
#### 4 - Slideshow

### Sonstiges:
* man kann auch Kernel für andere Sprachen herunterladen die den Jypiter-Interpreter für diese Sprache anbieten.