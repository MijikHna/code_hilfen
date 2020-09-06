# Building Angular und Django App

## 0 - Introduction

### 1 - Create a full-stack Angular app with Django REST Framework

### 2 - What to know

1. Python
2. Django
3. Django RESTful API
    * eventuell Course Building RESTful Web API with Django schauen
4. JS + ECMSScirpt 6
5. React.js 

### 3 - Demo Project Overview

* installiert:
  * Backend
        1. Django
        2. Django REST Framework
        3. Django-Filter (Django-REST Dependency) = QuerySets und Models filtern
        4. Django OAuth Toolkit
  * Frontend:
        1. Angular
        2. Angular Router = zwischen den Angular-Componenten navigieren
        3. Angular Material = für Material Design
        4. Protractor: End-To-End Tests
* gebildet:
    1. Django Models
    2. Angular Components

## 1 - Django and Angular Prepartion

### 1 - Running the Angular and Django Dev Servers

* Django:
    1. `./manage.py runserver`
    2. loclahost:8000/admin - Django-RESTful-API chekcen
    3. localhost:8000/api/v1/packages - Django-REST API checken

* Angular:
    1. `ng serve`
    2. localhost:4200

* Angualar-Dev Server ist in **proxy.conf.json** konfiguriert = sendet ensprechende URI and Django

```ts proxy.conf.json
{
    "/api": {
        "target": "http://localhost:8000",
        "secure": false
    },
    "/oauth": {
        "target": "http://localhost:8000",
        "secure": false
    }
}
```

### 2 - Compiling Angular Code

* `ng build --prod` - Code für Prod kompilieren
  * `--prod` - Optimiert Code für Prod z.B Debug-Sachen wegmachen
* in `angular.json` - Konfiguration/Optionen für Angular-Server

### 3 - Serving Angular Code Through Django static files

* nachdem Angular für Prod kompiliert wurde => in Django
    1. in `settings.py` am besten unten in der Nähe von `STATIC_URL` einfügen: `FRONTEND_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..', 'frontend', 'dist', 'frontend'))` als RegEx: `re_path(r^(?P<path>.*)$, serve, { 'document_root': settings.FRONTEND_ROOT })` - leitet URL zu Frontend-Directory (in Directory die in `FRONTEND_ROOT` gesetzt wurde) => nun kann man Angular-Frontend über Django-Server erreichen

    ```python
    STATIC_URL = '/static/'

    MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'api', 'uploads'))
    MEDIA_URL = '/uploads/'

    FRONTEND_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..', 'frontend', 'dist', 'frontend'))
    ```

    2. in `urls.py` URL zu frontend hinzufügen

    ```python
    urlpatterns = [
        re_path(r'^api/v1/', include(router.urls)),
        path('admin/', admin.site.urls),
        path('oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
        //Alle URL auf Frontend-Ordner umleiten
        re_path(r'^(?P<path>.*)$', serve, { 'document_root': settings.FRONTEND_ROOT }),
    ]
    ```

## 2 - Forms with Angular and Django

### 1 - Creating models with Django REST Framework

* Model erstellen und Serializer für dieses Model erstellen

```python models.py
class Package(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    promo = models.TextField()
    price = models.FloatField()
    rating = models.CharField(max_length=50)
    tour_length = models.IntegerField()
    start = models.DateField(default=django.utils.timezone.now)

    def __str__(self):
        return self.name
```

```python serializer.py
from rest_framework import serializers

from api.models import Package

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'
```

* View und Url

```python view.py
class PackageCreateView(CreateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
```

```py urls.py
from rest_framework.routers import DefaultRouter

import api.views

router = DefaultRouter()

urlpatterns = [
    re_path(r'^api/v1/packages/', api.views.PackageCreateView.as_view()),
    path('admin/', admin.site.urls),
    path('oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    re_path(r'^(?P<path>.*)$', serve, { 'document_root': settings.FRONTEND_ROOT }),
]
```

### 2 - Creating a ViewSet with Django

* Django-Rest-Framework hat Operationen für Model (also CRUD)

```py view.py
# muss man importieren
from rest_framework import viewsets

class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all() # alle Queries erstellen
    serializer_class = PackageSerializer
```

```py urls.py

router = DefaultRouter()
router.register(r'packages', api.views.PackagesViewSet)

urlpatterns = [
    re_path(r'^api/v1/', include[router.urls]), # die URL werden von viewset ergänzt. URL werden vom Router aufgelöst
    path('admin/', admin.site.urls),
    path('oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    re_path(r'^(?P<path>.*)$', serve, { 'document_root': settings.FRONTEND_ROOT }),
]
```

### 3 - Creating a REST API service with Angular

```ts rest-api.service.ts
export interface OAuthLoginResponse {
  access_token: string;
}

const clientId = 'wql5aqXepfkcF0JQOAoOo921zbvcrQSg1MUb2VUe';
const clientSecret = 'tVnwobvL4C7D76AOsYkrtDLh1D1mahbUqkzSBfqVi2zXfsBBD9Jm8FNe6yWof1XYIOwBfxtKrZh4Eug3piGu94Oga2R0VHJVG2VxQn1pw5Y5xcBOva0IX1n4WrPXZn0N';

@Injectable({
  providedIn: 'root'
})
export class RestApiService {
  constructor(private http: HttpClient) { }

  commonOptions(): { params?: any, headers?: HttpHeaders } {
    return {};
  }

  createTour(tourPackageData: TourPackage) {
    const { start, tourLength, ...data } = tourPackageData; // param tourPacakgeData in drei Variablen zerlegen
    return this.http.post(
      `/api/v1/packages/`,
      {
        start: start.toISOString().split('T')[0],
        tour_length: tourLength,
        ...data
      },
      this.commonOptions()
    ); // start zur Django-Datum umformen
  }
}
```

### 4 - Creating a basic form as an Angular component

```ts create-tour-form.component
@Component({
  selector: 'app-create-tour-form',
  templateUrl: './create-tour-form.component.html',
  styleUrls: ['./create-tour-form.component.css']
})
export class CreateTourFormComponent implements OnInit {
  packageForm: FormGroup;
  @Input() id: number;

  constructor(
    private tourPackageController: TourPackageController
  ) {}

  // wird jedes Mal aufgerufen, wenn Component erstellt wird (constructor wird nur ein Mal aufgerufen)
  ngOnInit() {
    // bei Initialisierung
    this.packageForm = new FormGroup({
      id: new FormControl(0),
      category: new FormControl('tour'),
      name: new FormControl('Tour Package'),
      promo: new FormControl('Promotional text'),
      tourLength: new FormControl(1),
      price: new FormControl(99.99),
      rating: new FormControl('easy'),
      start: new FormControl(new Date())
    });
  }

  save() {} //momentan nur Attrappe
}
```

```html create-tour-form.component.html
<h2>Create Tour Package</h2>
<div class="form-and-preview">
  <div class="form">
    <h3>Form</h3>
    <form [formGroup]="packageForm"> <!-- Form zu packageForm binden-->
      <mat-form-field> <!--Material Form-Field -->
        <mat-label>Name:</mat-label> <!-- Material Label-->
        <input type="text" formControlName="name" matInput /> <!--Material Style für <input>  benutzen-->
      </mat-form-field>
      <mat-form-field>
        <mat-label>Category:</mat-label>
        <input type="text" formControlName="category" matInput />
      </mat-form-field>
      <mat-form-field>
        <mat-label>Length of Tour (in days):</mat-label>
        <input type="text" formControlName="tourLength" matInput />
      </mat-form-field>
      <mat-form-field>
        <mat-label>Price:</mat-label>
        <input type="text" formControlName="price" matInput />
      </mat-form-field>
      <mat-form-field>
        <mat-label>Promotional Description:</mat-label>
        <input type="text" formControlName="promo" matInput />
      </mat-form-field>
      <mat-form-field>
        <mat-label>Starts On:</mat-label>
        <input type="text" formControlName="start" matInput />
      </mat-form-field>

      <br/>

      <mat-label>Challenge Rating:</mat-label>
      <mat-radio-group [value]="packageForm.controls.rating.value">
        <mat-radio-button matInput value="easy">Easy</mat-radio-button>
        <mat-radio-button matInput value="medium">Medium</mat-radio-button>
        <mat-radio-button matInput value="hard">Hard</mat-radio-button>
      </mat-radio-group>

      <button mat-button>Cancel</button>
      <button mat-raised-button color="primary" (click)="save()">
        {{packageForm.get('id').value == 0 ? 'Create' : 'Update'}} <!-- Name des Buttons abhängig von Update oder Create ändern-->
      </button>
    </form>
  </div>
  <div class="preview">
    <h3>Summary Preview</h3>
    <app-summary [tourPackage]="packageForm.getRawValue()"></app-summary> <!-- Preview anzeigen; Values an tourPackage binden  (Ich glaube. <app-summary> ist eigene Komponte -->
    <h3>Full Preview</h3>
    <app-tour-package [tourPackage]="packageForm.getRawValue()"></app-tour-package>
  </div>
</div>
```

### 5 - Connecting an Angular component to a service

```ts tour-package-controller.ts
@Injectable()
export class TourPackageController {
  constructor(private restApiService: RestApiService) { }

  save(tourPackageData: TourPackage) {
    return this.restApiService.createTour(tourPackageData);
  }
}
```

```ts create-tour-form.component.ts

// save() füllen
save() {
    const tourPackageData = this.packageForm.getRawValue();
    this.tourPackageController.save(tourPackageData).subscribe((savedData: any) => {
      this.packageForm.get('id').setValue(savedData.id);
    });
  }
```

## 3 - Front-End Design and Layout with Angular

### 1 - Form Layout with Angular Material

* Angular Material Grid Component um Form zu layouten
    1. `mat-grid-list` - `<input>` Attribut
    2. `mat-grid-title` - `<input>` Attribut

```html create-tour-form.component.html
<h2>Create Tour Package</h2>
<div class="form-and-preview">
  <div class="form">
    <h3>Form</h3>
    <form [formGroup]="packageForm">
      <!-- Material Grid Layout benutzen-->
      <mat-grid-list cols="5" rowHeight="20vh">
        <mat-grid-tile>
          <mat-form-field>
            <mat-label>Name:</mat-label>
            <input type="text" formControlName="name" matInput />
          </mat-form-field>
        </mat-grid-tile>
        <mat-grid-tile>
          <mat-form-field>
            <mat-label>Category:</mat-label>
            <input type="text" formControlName="category" matInput />
          </mat-form-field>
        </mat-grid-tile>
        <mat-grid-tile>
          <mat-form-field>
            <mat-label>Length of Tour (in days):</mat-label>
            <input type="text" formControlName="tourLength" matInput />
          </mat-form-field>
        </mat-grid-tile>

        <mat-grid-tile>
          <mat-form-field>
            <mat-label>Price:</mat-label>
            <input type="text" formControlName="price" matInput />
          </mat-form-field>
        </mat-grid-tile>

        <mat-grid-tile>
          <mat-form-field>
            <mat-label>Promotional Description:</mat-label>
            <input type="text" formControlName="promo" matInput />
          </mat-form-field>
        </mat-grid-tile>

        <mat-grid-tile colspan="2">
          <mat-form-field>
            <mat-label>Starts On:</mat-label>
            <input type="text" formControlName="start" matInput />
          </mat-form-field>
          <br/>

          <mat-label>Challenge Rating:</mat-label>
          <mat-radio-group [value]="packageForm.controls.rating.value">
            <mat-radio-button matInput value="easy">Easy</mat-radio-button>
            <mat-radio-button matInput value="medium">Medium</mat-radio-button>
            <mat-radio-button matInput value="hard">Hard</mat-radio-button>
          </mat-radio-group>
        </mat-grid-tile>

        <mat-grid-tile colspan="3" class="actions">
          <button mat-button>Cancel</button>
          <button mat-raised-button color="primary" (click)="save()">
            {{packageForm.get('id').value == 0 ? 'Create' : 'Update'}}
          </button>
        </mat-grid-tile>
      </mat-grid-list>
    </form>
  </div>
  <div class="preview">
    <h3>Summary Preview</h3>
    <app-summary [tourPackage]="packageForm.getRawValue()"></app-summary>
    <h3>Full Preview</h3>
    <app-tour-package [tourPackage]="packageForm.getRawValue()"></app-tour-package>
  </div>
</div>
```

### 2 - Date/time selection with a Calendar in Angular

* Datepickers von Materia
  1. `MatNativeDateModule` - Date-Object des Browsers
  2. `MatMomentDateModule` - benutzt *Moment.js` Date-Library

```html create-form.component.html
<mat-grid-tile colspan="2">
    <mat-form-field>
    <!-- Date-Picker-->
    <mat-label>Starts On:</mat-label> 
    <input type="text" formControlName="start" matInput
        [matDatepicker]="startsOnDatepicker" />
    <mat-datepicker-toggle matSuffix
        [for]="startsOnDatepicker"></mat-datepicker-toggle>
    <mat-datepicker #startsOnDatepicker></mat-datepicker>
    </mat-form-field>
    <br/>

    <mat-label>Challenge Rating:</mat-label>
    <mat-radio-group [value]="packageForm.controls.rating.value">
    <mat-radio-button matInput value="easy">Easy</mat-radio-button>
    <mat-radio-button matInput value="medium">Medium</mat-radio-button>
    <mat-radio-button matInput value="hard">Hard</mat-radio-button>
    </mat-radio-group>
</mat-grid-tile>
```

### 3 - Displaying a data table with Angular Material table

```html tour-package-list.component.html
<h2>Tours Available</h2>
<table mat-table [dataSource]="packages">
    <!-- Tabellen-Spalten werden in ng-container definiert-->
    <ng-container matColumnDef="name">
        <th mat-header-cell *matHeaderCellDef>Name</th>
        <td mat-cell *matCellDef="let element">
            <a routerLink="/packages/{{ element.id }}/update">
                {{ element.name }}
            </a>
        </td>
    </ng-container>

    <ng-container matColumnDef="price">
        <th mat-header-cell *matHeaderCellDef>Price ($)</th>
        <td mat-cell *matCellDef="let element">
            {{ element.price | currency }}
        </td>
    </ng-container>

    <ng-container matColumnDef="tourLength">
        <th mat-header-cell *matHeaderCellDef>Tour Length</th>
        <td mat-cell *matCellDef="let element">
            {{ element.tourLength }} days
        </td>
    </ng-container>

    <ng-container matColumnDef="actions">
        <th mat-header-cell *matHeaderCellDef>Actions</th>
        <td mat-cell *matCellDef="let element">
            <button mat-raised-button color="primary"
                routerLink="/packages/{{ element.id }}/update">
            Edit</button>
            <button mat-button color="warn" (click)="deleteTour(element)">
                Delete
            </button>
        </td>
    </ng-container>

    <tr mat-header-row *matHeaderRowDef="displayColumns"></tr>
    <tr mat-row *matRowDef="let row; columns: displayColumns;"></tr>
</table>
```

```ts tour-package-list.component.ts
@Component({
  selector: 'app-tour-package-list',
  templateUrl: './tour-package-list.component.html',
  styleUrls: ['./tour-package-list.component.css']
})
export class TourPackageListComponent implements OnInit {
  displayColumns: string[] = ['name', 'price', 'tourLength', 'actions'];
  packages: TourPackage[];
  totalPackages = 0;

  constructor(private tourPackageController: TourPackageController) { }

  changePage() {
    this.tourPackageController.list().subscribe((page: TourPackagePage) => {
      this.packages = page.results;
      this.totalPackages = page.count;
    });
  }

  // also wenn diese Componente in den DOM geladen wird, wird changePage() aufgerufen
  ngOnInit() {
    this.changePage();
  }

  deleteTour(tourPackage: TourPackage) {
    
  }
}

```

### 4 - Displaying a pop-up dialog box with Angular

### 5 - Displaying more information with Angular

## 4 - Authentication with Django and Django

### 1 - Setting up Authentication with Django OAuth Toolkit

### 2 - Using scopes with Django OAuth Toolkit for permissions

### 3 - Registrering a new OAuth application with Django OAuth Toolkit

### 4 - Logging in and authentication with Angular and HttpClient

### 5 - Using OAuth headers with Angular and HttpClient

### 6 - Authentication storage with Angular

## 5 - Filtering and Pagination with Django and Angular

### 1 - Checking permissions with Django

### 2 - Deleting an item using Angular and Django

### 3 - Partially updating an item using Angular

### 4 - Pagination with Django

### 5 - Pagination with Angular

### 6 - Filtering with Django

### 7 - Fitlering with Angular

### 8 - Animation with Angular

## 6 - Testing Angular

### 1 - Unit testing a component

### 2 - Unit testing a service

### 3 - Unit testing a controller

### 4 - End-To-End testing the form submission process

### 5 - End-To-End testing the filtered data table

## 7 - Testing Django

### 1 - Unit testing authentication

### 2 - Unit testing permission checks

### 3 - Unit testing validation for the REST API