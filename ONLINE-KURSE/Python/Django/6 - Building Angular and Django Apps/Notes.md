### 0 - Introduction
#### 1 - Create a full-stack Angular app with Django REST Framework
#### 2 - What to know
1. Python
2. Django
3. Django RESTful API
    + eventuell Course Building RESTful Web API with Django schauen
4. JS + ECMSScirpt 6
5. React.js 
#### 3 - Demo Project Overview
+ installiert:
    * Backend 
        1. Django
        2. Django REST Framework
        3. Django-Filter (Django-REST Dependency) = QuerySets und Models filtern
        4. Django OAuth Toolkit
    + Frontend:
        1. Angular
        2. Angular Router = zwischen den Angular-Componenten navigieren
        3. Angular Material = für Material Design
        4. Protractor: End-To-End Tests
+ gebildet:
    1. Django Models
    2. Angular Components

### 1 - Django and Angular Prepartion
#### 1 - Running the Angular and Django Dev Servers
+ Django:
    1. `./manage.py runserver` 
    2. loclahost:8000/admin - Django-RESTful-API chekcen
    3. localhost:8000/api/v1/packages - Django-REST API checken

+ Angular:
    1. `ng serve` 
    2. localhost:4200

* Angualar-Dev Server ist in **proxy.conf.json** konfiguriert = sendet ensprechende URI and Django
#### 2 - Compiling Angular Code
* `ng build --prod` - Code für Prod kompilieren
    - `--prod` - Optimiert Code für Prod z.B Debug-Sachen wegmachen
* in `angular.json` - Konfiguration/Optionen für Angular-Server
#### 3 - Serving Angular Code Through Django static files
* nachdem Angular für Prod kompiliert wurde => in Django 
    1. in `settings.py` am besten unten in der Nähe von `STATIC_URL` einfügen: `FRONTEND_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..', 'frontend', 'dist', 'frontend'))` als RegEx: `re_path(r^(?P<path>.*)$, serve, { 'document_root': settings.FRONTEND_ROOT })` - leitet URL zu Frontend-Directory (in Directory die in `FRONTEND_ROOT` gesetzt wurde) => nun kann man Angular-Frontend über Django-Server erreichen
    2. in `urls.py` URL zu frontend hinzufügen
### 2 - Forms with Angular and Django
#### 1 - Creating models with Django REST Framework
#### 2 - Creating a ViewSet with Django
#### 3 - Creating a REST API service with Angular
#### 4 - Connecting an Angular component to a service

### 3 - Front-End Design and Layout with Angular
#### 1 - Date/time selection with a Calendar in Angular
#### 2 - Displaying a data table with Angular Material table
#### 3 - Displaying a pop-up dialog box with Angular
#### 4 - Displaying more information with Angular

### 4 - Authentication with Django and Django
#### 1 - Setting up Authentication with Django OAuth Toolkit
#### 2 - Using scopes with Django OAuth Toolkit for permissions
#### 3 - Registrering a new OAuth application with Django OAuth Toolkit
#### 4 - Logging in and authentication with Angular and HttpClient
#### 5 - Using OAuth headers with Angular and HttpClient
#### 6 - Authentication storage with Angular

### 5 - Filtering and Pagination with Django and Angular
#### 1 - Checking permissions with Django
#### 2 - Deleting an item using Angular and Django
#### 3 - Partially updating an item using Angular
#### 4 - Pagination with Django
#### 5 - Pagination with Angular
#### 6 - Filtering with Django
#### 7 - Fitlering with Angular
#### 8 - Animation with Angular

### 6 - Testing Angular
#### 1 - Unit testing a component
#### 2 - Unit testing a service
#### 3 - Unit testing a controller
#### 4 - End-To-End testing the form submission process
#### 5 - End-To-End testing the filtered data table

### 7 - Testing Django
#### 1 - Unit testing authentication
#### 2 - Unit testing permission checks
#### 3 - Unit testing validation for the REST API