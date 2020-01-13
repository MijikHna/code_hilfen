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
* mit den Up/Down- Buttons kann man Zellen nach oben/unten verschieben
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
* Bar Funktionen
```python
bar(x, height, *, align="center", **kwargs)
bar(x, height, width, *, align="center", **kwargs)
bar(x, height, widht, bottom, *, align="center", **kwargs)
```
* `x` - Coordinaten der Bar (Integer-Array oder String-Array)
* `height` - Liste oder Array
* <- nur diese beiden sind required
```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def get_df(yr):
    return pd.read_csv("../../xx.csv".format(yr))

def get_seasons(yr):
    df = get_df(yr)
    return [df[df["date"].between('{}_03_20'.foramt(yr), '{}_06_20'.foramt(yr))],
        df[df["date"].between('{}_03_20'.foramt(yr), '{}_06_20'.foramt(yr))]]


seasons = ["Spring", "Summer"]
heights = [season["Air_Temp".mean( for season in get_seasons("2013"))]]

alphas = [height/max(heights) for height in heights]
colors = [.1, .7, .2, a]

plt.bar(seasons, heights)
plt.bar(seasons, heights .6, color = colors)
plt.ylabel("Farenheit", fontsize=12)
plt.title("Avearage", fontsize=16)
plt.xticks(rotation=60, fontsize=12)
plt.ylim(0,80) #  y- von 0 bis 80 unterteilen
plt.show()

# zweiten Plot laden
#  zwei Plots in enem
index = np.arange(4)
fig, ax = plt.subplots()
rects1 = ax.bar(index, heights, .3, color=colors, label="2013")
rects2 = ax.bar(index+.3, heights14, .3, color=colors14, label="2013")
ax.legend()
plt.show()
```
* Farben für *plt*
    * Stirng
    + RGB(A) als Hex
    * RGB(A) als Tuple (0.0, 0.0, 0.5, 1)
#### 4 - Bar graphs with subplots
* erweiteitert oberen Bsp:
```python
index = np.arange(4)
fig, ax = plt.subplots()
rects1 = ax.bar(index, heights, .3, color=colors, label="2013")
rects1 = ax.bar(index+.3, heights14, .3, color=colors14, label="2014")
ax.legend()
plt.show()
```
#### 5 - Tables
* Syntax für Tabellen
```python
table(celText=None, cellColors=None, cellLoc="right", colWidths=None, rowLabels=None, rowColurs=None, rowLoc="left", colLabels=None, colColours=None, colLoc="center", loc="bottom", bbox=None)
```
+ Bsp
```python
plt.bar(seasons, heights .6, color = colors)
plt.ylabel("Farenheit", fontsize=12)
rows = ["Spring", "Sommer"]
columns = ["Max", "Date", "Min", "Date"]
plt.table(cellTex=min_max_temps("2014"), rowLabels=rows, colLabels=columns)

plt.table(cellTex=min_max_temps("2014"), 
    rowLabels=rows, 
    colLabels=columns
    rowColours=colours,
    cellColours=[[c]*4 for c in colours],
    loc="bottom")
plt.xticks([])
plt.show()
```
### 4 - Publishing and Sharing your Jupyter Notebook
#### 1 - Exporting to HTML and PDF
* 2 Wege nach Html zu konvertieren
    * File -> Download in HTML
    * `jupyter nbconvert noteBookName.ipynb` - da StandardTyp ist HTML
* nach PDF:
    * über Browser
    + File - Download as -> PDF via Latex
        * braucht aber LaTex (z.B Linux braucht Tex Live) <- Info dazu auf nbconvert-Doku-Seite
    * `jupyter nvcovnert --to pdf noteBookName.ipynb`
#### 2 - Distributing on GitHub
1. über GitHub-WebGui:
    1. Repo öffnen
    2. .ipynb drag and dropen
2. über GitHub-Gists gist.github.com
    1. Gist erstellen (secret + public Gist)
    2. Drag and Drop 
#### 3 - Notebook Viewer
* nbviewer.jupyter.org
    * Github oder Githu-Gist - Link dort eingeben
#### 4 - Slideshow
* zu Slides konvertieren
    1. View -> Cell toolbar -> Slidesshow
    2. bei jeder Celle kann man dann auswählen was + zu welchem SlideTyp werden soll
    3. File -> Downloas as -> slides  
    PDER
    4. `jupyter nbconvert  noteBookName.ipynb --to slides -post serve` - post = öffnen Slides direkt
* Slides sind dann nach Rechts/Links und Unten/Oben 

### Sonstiges:
* man kann auch Kernel für andere Sprachen herunterladen die den Jypiter-Interpreter für diese Sprache anbieten.

### empfehlenswerte Kuser:
* Data Science Foundations: Python Scientific Stack
* Python Statistics: Essential Training  

* Jupyter.org