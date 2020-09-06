#### Teil 1

+ `pip3 install jupyterthemes` - Themes installieren
+ `jt --list` - verfügbare Themes anzeigen
+ `jt -t chesterisch` - Theme **chesterisch** installieren
+ `jt -r` - Standart-Theme wiederverwenden
+ `STRG+Shift+P` - Command-Palette aufrufen
+ `Shift+Enter` - aktuellen Code ausführen
+ `Esc` - Command Modus aktivieren
    * `A` - Add Code-Teil
    * `B` - Add Code-Teil unter aktuellem
    + `M` - aktuellen Code-Teil zu Markdown ändern
    * `Y` - Code-Teil returnen
    + `D + D` - aktuellen Code-Teil löschen
    + `Enter` - zu Edit-Modus ändern
    + `Shift + Tab` - Doku des Objekts anzeigen
    + `Esc + F` - Find
    * `Esc + 0` - Ausgabe der Code-Teile umschalten
    + `Shift + J` oder `Shift + Down` - unteren Code-Teil auswählen
    * `Shift + K` oder `Shift + Up`
    + `Shift + M` - Code-Teile vereinen
* `!bach-command` - mit `!` bash-Commands in Jupyter ausführen
* `LaTex` in Markdown-Code-Teil eingeben (nach dem LaTex-Code) - LaTex in verwenden
* 
```python
from IPython.core.interactiveshell import InteractiveShell

InteractiveShell.ast_node_interactivity = “all”
```
* <- per Default wird nur letzte Zeile ausgeben. Sonst muss man alles `printen`. mit diesem Code am Anfang des Notebooks wird alles ausgegeben
    + `InteractiveShell.ast_node_interactivity = “last_expr”` - wieder zum Standard zurückkehren
* Seite des *jupyterthemes*-Codes: **https://github.com/dunovank/jupyter-themes**
* Für Jupyter gibt es viele Erweiterung (https://github.com/ipython-contrib/jupyter_contrib_nbextensions) und (https://github.com/ipython/ipython/wiki/Extensions-Index)
    * `pip install jupyter_contrib_nbextensions` - Tab mit Erweiterungen aktiveren. Eventuell noch `jupyter contrib nbextension install --user` ausführen
    * Famous Erweiterungen
        1. Scratchpad - Temp-Teil-Code generieren, um schnelle, kurze Berechnungen zu machen.
        2. Hinterland - Menu-Eintrag mit Autocomplition
        3. Snippets
        4. Autopep8 
        5. Split Cells Notebook - Cells teilen
        6. Table of Contents - Zeigt alle Titel des Notebooks an
        7. A Code Prettifier - Formattierung usw.
        8. Notify - Benachritiguen, wenn Kernel im Background läuft
        9. Code Folding
        10. Zen Mode
#### Teil 2
+ magics - Commands, die wie Bash-Commands aussehen, sind aber in Python implementiert
    1. `%magic` - einzeilige Magics
    2. `%%magic` - ganzteilige Magics
    * Bsp: `%lsmagic` 
+ Bsp: Magics:
    * `%env` - ENV-Varaiblen des Notebooks beeinflussen
    * `%load` - Code aus fremden Skript laden
        * `%laod lala.py`
    * `%% writefile lala.py python-code` - Code in eine Datei exportieren
        * z.B. Datei mit Imports erstellen und diese dann mit `%load lala.py` importieren
    * `%macro -q _hello_you 32` - Makro erstellen, 32 - Zeilen Nummer, man kann auch Nummer des Code-Teil angeben
        * Bsp:
        ```python
        name = "Kitten"
        print(Hello, %s!", % name)
        ```
        ```python
        %macro -q _hello_you 2
        %load __hello_you # - Makro laden
        __hello_you # Aufruf von: print(Hello, %s!", % name)
        ```
    * `%store` - um Makros zu speichern und in allen Notebooks verwenden
    ```python
    %store -r __hello_you
    name = ‘Rambo’
    %load __hello_you
    ```
    * `%run` - Code ausführen und dabei alles ausgeben (Ausnahme Matplotlib). Kann auch Code aus .py-Dateien ausführen
    * `%pycat` - *cat* für Python-Dateien
        * `%pycat lala.py`
    * `%autosave 60` - Autosave jede 60 Sekunden
    * `%matplotlib inline` - Matplotlib-Grafiken direkt ausgeben. Man sollte es am Anfang des Notebooks ausführen, sonst muss man den Code manuell ausführen
    * Zeit-Messungen:
        * `%time` und `%%time` - Zeit-Messung der Codeausführung
        * `%timeit` und `%%timeit` - mehrfache Messung und Mittelwert ermittelt. Mit `-n xx` und `-r xx` die Anzahl angeben.
    * andre Sprache ausführen (Code des andren Kernels ausführen)
        * `%%bash`, `%%HTML`, `%%python`, `%%pyhton3`, `%%ruby`, `%%perl`, `%%capture`, `%%capture`, `%%javascript`, `%%js`, `%%latex`, `%%markdown`, `%%pypy`
        * Bsp html
        ```
        %%HTML
        This is <em>really</em> neat!
        ```
        * Bsp LaTex
        ```
        %%latex
        This is an equation: $E = mc²$
        ```
    * `%who` - alle globalen Variablen ausgeben
    * `%who str` - alle Variablen vom Typ String ausgeben
    + `%prun` - zeigt Zeit an, die einzelne Funktionen verbrauchen
        + `%prun funkt_name` - zeigt genau Angaben zu der Ausführung der Funktion
    + `%pdb` - in Body der Funktion reinschauen bei Ausführung. man sollte dieses Magic am Anfang des Code-Teils ausführen
    + `%config InlineBackend.figure_format = 'retina' - Grafik in höhrere Auflösung ausgeben
    * `%%script false` - dann folgt Code. ??
    + Notification ertellen
        * für Linux und Mac
        ```python
        import os
        duration = 1 #Sekunden
        freq = 440 # Hz
        os.system(‘play — no-show-progress — null — channels 1 synth %s sine %f’ % (duration, freq))
        ```
        + für Windows
        ```python
        import winsound
        duration = 1000 # MilliSek
        freq = 440 # Hz
        winsound.Beep(freq, duration)
        ```
        * es wird **sox** benötigt. Schauen, ob man es mit Packat-Manager installieren kann
#### Teil 3 - automatisch Importieren Bibs für Notebooks
1. *~/ipython/profile_default* öffnen
2. Ordner *startup* erstellen, wenn nicht schon existiert
3. dort **startup.py** erstellen (kann auch andren Namen bekommen)
4. Dateien hinzufügen, die importiert weden sollen
5. jupyther oder ipython starten
```python
import pandas as pd
import numpy as np

# Pandas options
pd.options.display.max_columns = 30
pd.options.display.max_rows = 20

from IPython import get_ipython
ipython = get_ipython()

# If in ipython, load autoreload extension
if 'ipython' in globals():
    print('\nWelcome to IPython!')
    ipython.magic('load_ext autoreload')
    ipython.magic('autoreload 2')

# Display all cell outputs in notebook
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'

# Visualization
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import iplot, init_notebook_mode
init_notebook_mode(connected=True)
import cufflinks as cf
cf.go_offline(connected=True)
cf.set_config_file(theme='pearl')

print('Your favorite libraries have been loaded.')
```
+ mit `globals()` kann man chechen, ob die Bibs wirklich geladen wurden.
    * `globals()['pd']` und `globals()['np']`
+ damit bekannt ist, welche Bibs benutzt werden (importiert), sollte man es in Notebook irgendwie Dokumentieren

#### Teil 4 -  Juypter richtig einstellen
* Fehler bei Notebooks:
    1. kein Name
    2. keine Dokumentation des Codes
    3. Code-Teile sind nicht in der Reihenfolge, in der der Code wirklich ausgeführt wird
    4. Code hat Fehler
* Hilfe => Erweiterungen = erstelle Pattern für Dokumentation, importiert häufig benutzte Bibs, fragt nach Namen des Notebooks
    1. Erweiterungen installieren: 
    2. Order Setup von https://github.com/WillKoehrsen/Data-Analysis/tree/master/setup herunterladen
    3. `pip show jupyter_contrib_nbextensions`, um zu schauen, wo Erweiterungen installiert wurden
    4. in angezeigten Ordner den heruntergeladenen Ornder *Setup* ablegen
    5. `jupyter contrib nbextensions install` ausführen
    6. Jupyter starten und über Erweitrungen-Menu Setup aktivieren (eventuell davor edit > nbextentions config anklicken)

#### Automatisierung
+ oft muss man gleichen Code-Teil mehrmals mit unterschiedlichen Parametern ausführen. Das kann man automatisieren. Hilfen sind: **IPywidgets**, **mybinder**
##### IPywidgets
1. `pip install ipywidgets` - installieren
2. `jupyter nbextention enable --py widgetsnbextention` - aktivieren
3. `jupyter labextension install @jupyter-widgets/jupyterlab-manager` - damit man JupyterLab benutzen kann
4. ipywidgets ins Notebook importieren
```python
import ipywidgets as widgets
from ipywidgets import interact, interact_manual
```
5. Bsp der Verwendung
```python
df.loc[df['reads'] > 1000] #Beiträge anzeigen, deren Views/Reads > 1000 sind
df.loc[df['claps'] > 500] #Beträge, die > 500 Claps haben

# Hier beginnt die Automatisierung
@interact # erstellt Eingabefeld und Slider
def show_articles_more_than(column='claps', x=5000):
    return df.loc[df[column] > x] # es wird ein Eingabefeild erstellt, wo man die Anzahl der Claps eingeben kann

@interact
def show_articles_more_than(column=['claps', 'views', 'fans', 'reads'], x=(10, 100000, 10)):
    return df.loc[df[column] > x]

# Feld für Images die man auswählen kann.
import os
from IPython.display import Image

@interact
def show_images(file=os.listdir('images/')):
    display(Image(fdir+file))

# Correlationen zwei Felder anzeigen
@interact
def correlations(column1=list(df.select_dtypes('number').columns),
     column2=list(df.select_dtypes('number').columns)):
 print(f"Correlation: {df[column1].corr(df[column2])}")
```
* hier sind weiter Beispiele: https://github.com/jupyter-widgets/ipywidgets/tree/master/docs/source/examples

+ weitere Bsp:
```python
# Daten visualisieren
import cufflinks as cf
@interact #man kann hier auch @interact_manual benutzen, dann bekommt man noch Button RUN, damit man die Auswertung manuell starten kann
def scatter_plot(x=list(df.select_dtypes('number').columns), 
                 y=list(df.select_dtypes('number').columns)[1:],
                 theme=list(cf.themes.THEMES.keys()), 
                 colorscale=list(cf.colors._scales_names.keys())):
    df.iplot(kind='scatter', x=x, y=y, mode='markers', 
             xTitle=x.title(), yTitle=y.title(), 
             text='title',
             title=f'{y.title()} vs {x.title()}',
             theme=theme, colorscale=colorscale)
```
+ weiter Bsp:
```python
# Create interactive version of function with DatePickers
    #stats_for_articel_published_between = Funktion, die als Param. Anfangs- und Enddatum hat, und return alle Beiträge zwischen diesen Datums
interact(stats_for_article_published_between,
        start_date=widgets.DatePicker(value=pd.to_datetime('2018-01-01')),
        end_date=widgets.DatePicker(value=pd.to_datetime('2019-01-01')))


# Wenn ein Widget vom andren abhängen soll
# Create widgets
directory = widgets.Dropdown(options=['images', 'nature', 'assorted'])
images = widgets.Dropdown(options=os.listdir(directory.value))
 
# Updates the image options based on directory value
def update_images(*args):
    images.options = os.listdir(directory.value)
 
# Tie the image options to directory value
directory.observe(update_images, 'value') 

# Show the imagesdef show_images(fdir, file):    display(Image(f'{fdir}/{file}')) 
_ = interact(show_images, fdir=directory, file=images)
```
* Wetiere Beispiele: Widgets in mehreren Code-Teilen benutzen => Benutzung der Funktioen `interact` und in den Code-Teilen dann `stat.widget` aufrufen
```python
def show_stats_by_tag(tag):
    return(df.groupby(f'<tag>{tag}').describe()[['views', 'reads']])

stats = interact(show_stats_by_tag,
               tag=widgets.Dropdown(options=['Towards Data Science',
               'Education', 'Machine Learning', 'Python',
               'Data Science']))
```
* Dokumentation: https://ipywidgets.readthedocs.io/en/stable/user_guide.html

#### Teil 5 - Upgrade Jupyter
1. jupyterthemes installieren
2. `jt -t onedork -fs 95 -altp -tfs 11 -nfs 115 -cellw 88% -T` - Dark Mode anmachen
* Verschiedene Kernel (Sprachen) installieren
    1. `conda activate my_NLP` - wenn man Anaconda benutzt 
    2. `pip install ipykernel`
    3. `pyhton -m ipykernel install --user --name=my_NLP` - den Kernel an Jupyter binden
    4. `conda activate gym`
    5. `pip install ipykernel`
    6. `python -m ipykernel install --user --name=gym`
+ <- jetzt kann man in Jupyter zwischen den Kernels umschalten

#### Teil 6 - Tipps für Jupyter
##### 1 - Bash-Commands auführen
+ `!BASH_COMMAND` z.B `!ls`
##### Themen ändern:
* `pip install jupyterthemes`
    * `jt -l` - alle Themen anzeigen
##### Erweiterungen:
* `pip install jupyter_contrib_extensions`
* `jupyter cotrib nbexention install`
    1. `Headings generieren` mit `#`s kann man Headings dann erstellen
    2. Autocompletion
    3. Zellen teilen - Zelle auswählen und auf hinzugekommen Button klicken
    4. Dataframes mit Qgrid untersuchen ohne Pandas-Code
        * `pip install qgrid`
        * `jupyter nbextion enable`
        * python-code in NoteBooks
        ```py
        import qgrid
        qgrid_widget = qgrid.show_grid(df, show_toolbar=True)
        ```
        * wird ähnlich zu Excel-Sheet dargestellt
* Doku zu Jupyter: https://jupyter.org/documentation
