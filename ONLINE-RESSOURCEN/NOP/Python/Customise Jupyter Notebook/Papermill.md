https://nuancesprog.ru/p/6405
* Problem: keien Automatisierung und Logging (keine Trace usw.)
+ Papermill = Tool für Parametrisierung und starten von Notebooks. Macht Notebook zum Prozess. 
* => Papermill in Notebook integrieren. Bsp: Notebook für Wettervorhersage mit Bib *PyOWM*
* Ablauf:
    1. Papermill und JupyterLab installeiren
        1. *Conda*-Umgebung einrichten: `conda create -n papermill python=3.7`
        2. Diese Umgebung aktivieren: `conda activate papermill`
        3. benötige Bibs installieren: `pip install papermill pyowm jupyterlab pandas seaborn boto3 pdfkit`
        4. Doku zu Papermill: `papermill -h`
    2. Jupyter Kernel für Papermil einrichten:
        1. `pip install ipykernelipython kernel install --user --name=papermill-tutorial` 
    3. mit PyOWM Wetterdaten einer Stadt berechnen:
        1. PyOWM = Bib für WEB API OpenWeatherMap (man Braucht API-Key für OpenWeather)
        2. Daten Bekommen: Info zu `city` bekomme. Obj. `forecast` durchsuchen und die Info in `DataFrame` ablegen. Alle in Jupyter Notebook 
            * Teil 1: Daten vorbereiten
            1. Bibs importieren:
            ```python
            import pyowm
            import pandas as pd
            import seaborn as sns
            import matplotlib.pyplot as plt
            import pdfkit
            ```
            2. API-Key installieren
            ```python
            owm = pyowm.OWM('xxxxxxxxxxxPyOWM-API-keyxxxxxxxx')
            ```
            3. die Stadt auswählen
            ```python
            city = 'Sao Paulo,BR`
            ```
            4. Daten der Stadt bekommen
            ```python
            fc = owm.three_hours_forecast(city)
            forecast = fc.get_forecast()
            ```
            5. Dictionary für Wetterdaten erstellen
            ```py
            dict_forecast = {
            ‘datetime’:[],
            ‘clouds’:[],
            ‘humidity’:[],
            ‘temp’:[],
            ‘temp_max’:[],
            ‘temp_min’:[],
            ‘detailed_status’:[],
            ‘icon_url’:[],
            ‘rain_vol’:[]
            }
            ```
            6. `forecast` durchlaufen und Daten holen
            ```python
            for weather in forecast:
                dict_forecast['datetime'].append(str(weather.get_reference_time(timeformat='iso')))
            dict_forecast['clouds'].append(weather.get_clouds())    dict_forecast['humidity'].append(weather.get_humidity())
            dict_forecast['temp'].append(weather.get_temperature(unit='celsius').get('temp'))
            dict_forecast['temp_max'].append(weather.get_temperature(unit='celsius').get('temp_max'))
            dict_forecast['temp_min'].append(weather.get_temperature(unit='celsius').get('temp_min'))
            dict_forecast['detailed_status'].append(weather.get_detailed_status())
            dict_forecast['icon_url'].append(weather.get_weather_icon_url())
                if '3h' in weather.get_rain().keys():
                    dict_forecast['rain_vol'].append(weather.get_rain().get('3h'))
                else:
            dict_forecast['rain_vol'].append(0)
            ```
            7. `DataFrame` erstellen
            ```python
            df = pd.DataFrame.from_dict(dict_forecast)
            df.head()
            ```
            * Teil 2: Daten visualisieren (mit *seaborn*)
            8. Grafik für die nächsten 5 Tage erstellen
            ```py
            fig = plt.figure()
            sns_plot = sns.lineplot(data=df_temp, style="event",markers=True, dashes=False)
            sns_plot.set_title(f'Temperature forecast for the next 5 days', fontsize=20)
            sns_plot.set_xlabel('Date', fontsize=14)
            sns_plot.set_ylabel('Temperature Celsius', fontsize=14)
            sns_plot.set_xticklabels(df_temp.index, rotation=20)
            sns_plot.grid(True)

            sns_plot.legend(labels=['Min. Temperature', 'Max Temperature', 'Average Temperature'])
            fig.set_size_inches(12, 6)

            temperature_plot = f"{city.split(',')[0].replace(' ','_')}_temperature.png"
            sns_plot.figure.savefig(temperature_plot, 
                            dpi=300, facecolor='w', 
            ```
            9. *DataFrame* mit RegenMenge sortiert nach Tagen:
            ```python
            df_rain_per_day = df.resample(‘D’, on=’datetime’).sum()[[‘rain_vol’]]
            df_rain_per_day.index = df_rain_per_day.index.date
            ```
            10. 
            ```py
            fig = plt.figure()
            # Линейный график влажности и облачности:
            ax1 = fig.add_subplot(211)
            ax1 = sns.lineplot(data=df_mean[['clouds', 'humidity']], markers=True, dashes=False)
            ax1.set_xticks([])
            ax1.set_title(f'Expected humidity and rain volume for the next 5 days', fontsize=20)
            ax1.set_ylabel('Percentage', fontsize=14)
            ax1.grid(True)

            # Столбцы с общим объемом осадков по дням:
            ax2 = fig.add_subplot(212)
            ax2 = sns.barplot(x=df_rain_per_day.index, y='rain_vol', 
                            data=df_rain_per_day,
                            palette="Blues_d")
            ax2.set_xticklabels(df_temp.index, rotation=30)
            ax2.set_ylabel('Total Rain Volume in mm', fontsize=14)
            ax2.set_xlabel('Date', fontsize=14)
            fig.set_size_inches(12, 6)

            rain_humidity_plot = f"{city.split(',')[0].replace(' ','_')}_rain_humidity.png"
            fig.savefig(rain_humidity_plot, 
                        dpi=300, facecolor='w', 
            ```
            * Teil 3: alles in PDF abspeichern mit `pdfkit`; mit HTML-Template PDF erstellen
            11. die Daten auswählen
            ```py
            today = str(df_mean.index.min()).replace(‘-’, ‘/’)
            last_day = str(df_mean.index.max()).replace(‘-’, ‘/’)
            ```
            12. HTML-Temlate
            ```py
            report_template = f’’’
            <!DOCTYPE html>
            <html>
            <head>
            <meta charset=’utf-8'>
            <title>Weather Forecast with PyOWM</title>
            <link rel=’stylesheet’ href=’report.css’>
            <style>
            h1 {{
            font-family: Arial;
            font-size: 300%;
            }}
            h2 {{
            font-family: Arial;
            font-size: 200%;
            }}
            @page {{
            size: 7in 9.25in;
            margin: 27mm 16mm 27mm 16mm;
            }}
            </style> 
            </head>
            <h1 align=”center”>Weather forecast for {city}</h1>
            <h2 align=”center”>Initial date: {today}</h2>
            <h2 align=”center”>Final date: {last_day}</h2>
            
            <figure>
            <img src=”{temperature_plot}” width=”1200" height=”600">
            </figure>
            <figure>
            <img src=”{rain_humidity_plot}” width=”1200" height=”600">
            </figure> 
            </html>
            ‘’’
            ```
            13. HTML ins Datei speichern
            ```py
            html_report = f"{city.split(',')[0].replace(' ','_')}_report.html"
            with open(html_report, "w") as r:
            r.write(report_template)
            ```
            * alle Prüfen, bevor man Paperpill dazuschaltet (Run -> Run all cells)
        4. Notebook für Paperpill eisntellen. Dazu JupyterLab benutzen oder Jupyter Notebook mit Pyperpill verbinden
            1. JupyterLab - Cell mit Konfig erstellen
                1. Konfig/Parameter-Cell erstellen
                2. Notebook Tools auswählen
                3. Advanced Tools erstellen
                4. eingeben und speichern
                ```json
                {
                    "tags": [
                        "parameters"
                    ]
                }
                ```
            2. Jupyter Notebook 
                1. View -> Cell -> Toolbar -> Tags
                2. Tag `parameters` in richtige Cell eingeben
        5. Papermill ausführen:
            1. erste Beiden Param: Name des Input-Notebooks und Output-Notebooks; mit `-p` Parameter angeben (Name und Wert der Parameter); `-k` - Jupyter-Kern (Hier *papermill-tutorial*)
            ```bash
            papermill weather_forecast_using_pyowm.ipynb \
            weather_forecast_using_pyowm_output.ipynb \
            -p city 'Sao Paulo,BR' \
            -k papermill-tutorial
            ```
            2. wenn man das gleiche direkt über PythonAPI ausführe will => 
            ```py
            import papermill as pm

            pm.execute_notebook('weather_forecast_using_pyowm.ipynb',
                                'weather_forecast_using_pyowm_output.ipynb',
                                parameters={'city':'Sao Paulo,BR'},
                                kernel_name='papermill-tutorial')
            ```
            * Die Ausgabedateien sing *.ipynb* in JSON-Format. Dort kann man auch Fehler ansehen, die eim Ausführen passiert sind.
            * Diese JSON-Ausgabe kann man dann z.B in DB speichern (MongoDbB, BigTable usw.)
