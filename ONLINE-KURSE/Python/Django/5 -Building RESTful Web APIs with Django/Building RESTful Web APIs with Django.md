### 0 - Introduction
#### 1 - Create a REST API with Django and Django REST framework
* Python (Python Buch: https.//learnpyhtonthehardway.org/python3/)
* Django
    * Models
    * Views
    + Templates
    + URL config
* Bsp: eCommerce
* Libs:
    * Django
    * Django REST Framework
    * Django-Filter
    * Mock - Mocks für Unit Tests
    * Pillow - Image Editing
Project wird in virtenv betrieben

### 2 - Installation:
1. `pip install djangorestframework markdown django-filter`
2. Project uns APP erstellen
3. eventuell in `settings.py` -> bei `INSTALLED_APPS` `rest_framework` einfügen, damit man die REST-API auch im Browser nutzen kann, sonst kann man REST-API mit **curl** oder **Postman**
### 1 - Serializin, Listing, Filtering and Paginating Models
#### 1 - Creating a Django REST Framework serializer to serialize a model
* Serializaition bedeutet einen Obj zu JSON, YAML, XML convertieren
    * Bsp hier: Product-Model zu JSON serialisieren und durch REST API anbieten
* `to_representation()` - Adden oder Removen Daten von Serializer
```python
#./store/serializers.py
from rest_framework import serializers

from store.models import Product

class ProductSerializer(serializer.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'desc', 'price', 'sale_start', 'sale_end')

        def to_representation(self, instance):
            data = super().to_representation(instance)
            data['id_on_sale'] = instance.is_on_sale()
            data['current_price'] = instance.current_price()
            return data
```
+ <- Implementierung testen:
    * `./manage.py shell`
    * `from store.models import Product`
    * `product = Product.objects.all()[0]`
    * `form store.serializers import Product`
    * `data = serializer.to_representation(product)`
    * `from rest_framework.renders import JSONRenderer`
    * `renderer = JSONRender()`
    * `renderer.render(data)` - Daten serializeren => Return ist JSON-Obj
#### 2 - Creating a ListAPIView subclass
* List API View erstellen
* Django REST Framework hat mehrere generische API views:
    1. ListAPIView
    2. CreateAPIView
    3. DestroyAPIView
    4. RetrieveUpdateDestroyAPIView
```python
# ./store/api_views.py
from rest_framework.generics import ListAPIView

from store.serialiers import ProductSerializer
from store.models import Product

class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializers_class = ProductSerialier
```
* render wird schon von `ListAPIView` übernommen. Also hier nur angeben was soll gerendert werden (`Product.object.all()`) und welcher Serializer wird verwendet (`ProductSerializer`)
* sehr selten wird man eigne APIView bilden wollen z.B wenn man viele Funktionen von mitgelieferten Views nicht braucht (dafür **base APIView*** benutzen)
#### 3 - Connecting an APIView to route
* Django REST Framework hat Compatibitilt mit Django Views, deswegen wurden Django REST Framework Views  gleich wie Methode as_view() implementiert
* /demo/urls.py mit folgenem path ergänzen
```python
# ./demo/urls.py
import store.api_views

path('api/v1/products/', store.api_views.Product.as_view()),
```
#### 4 - Filter back ends with URL query parameters
* = Product nach ID und on_sale filtern
* `filter_fields`-Fels von Serializer added entsprechende Felder zu URI und Filtert dann QuerySet nach diesen GET-Parametern
```python
# ./store/api_views.py
from rest_framework.generics import ListAPIView
form django_filter.rest_framework import DjangoFitlerBackend

from store.serialiers import ProductSerializer
from store.models import Product

class ProductList(ListAPIView):
    queryset = Product.object.all()
    serializers_class = ProductSerialier

    fitler_backends = (DjangoFilterBackend)
    fitler_fields = ('id') # es wird in URI ein Button für Fitlers -> id angzeigt (man kann auch mittels URI fitlern mit .../?id=3)

    # filter danach ob im Product-Model-Feld on_sale=true gesetzt ist
    def get_queryset(self): # get_queryset von ListAPIView überschreiben
        on_sale = self.request.query_params.get('on_sale', None) #GET-Option on_sale extrahieren
        if on_sale is None:
            return super().get_queryset() # wenn nicht gesetzt => Basis-Klasse get_queryset() aufrufen und returnen
        queryset = Product.object.all()
        if on_sale.lower() == 'true':
            form django.utils import timezone
            now = timezone.now()
            return qureyset.filter(
                sale_start__lte = now,
                sale_end_gte = now,
            )
        return queryset
```
#### 5 - Enabling full-text search filter back end
* = durch Productnamen und Product-Description suchen
* dafür wird SearchFilter von Django REST Framework benutzt
```python
# ./store/api_views.py
from rest_framework.generics import ListAPIView
from django_filter.rest_framework import DjangoFitlerBackend
from rest_freamwork.filters import SearchFilter

from store.serialiers import ProductSerializer
from store.models import Product

class ProductList(ListAPIView):
    queryset = Product.object.all()
    serializers_class = ProductSerialier

    fitler_backends = (DjangoFilterBackend, SearchFitler)
    fitler_fields = ('id') # es wird in URI ein Button für Fitlers -> id angzeigt (man kann auch mittels URI fitlern mit .../?id=3)
    search_fields = ('name', 'description') #wird von SearchFilter benutzt um name und description von URI auf Model zu mappen

    # filter danach ob im Product-Model-Feld on_sale=true gesetzt ist
    def get_queryset(self): # get_queryset von ListAPIView überschreiben
        on_sale = self.request.query_params.get('on_sale', None) #GET-Option on_sale extrahieren
        if on_sale is None:
            return super().get_queryset() # wenn nicht gesetzt => Basis-Klasse get_queryset() aufrufen und returnen
        queryset = Product.object.all()
        if on_sale.lower() == 'true':
            form django.utils import timezone
            now = timezone.now()
            return qureyset.filter(
                sale_start__lte = now,
                sale_end_gte = now,
            )
        return queryset
```
* SearchFilter kann suchen
    1. Partial Match (Default)
    2. Exact Match => `=SUCHEXPR`
    3. Regular Expression => `$[Ee]ar$`
#### 6 - Enabling pagination of querysets in API responses
* wenn zu viele Results geliefert werder kann man sie paginaten
* 3 Möglichkeiten um Results zu pagen
    1. PageNumber - URI hat PagenNumber
    2. Limit Offset - URI hat Limit (wie viele Results auf der Seite (`/?limit=xx`)) und Offset (welche Seite (/?limit=2&offset=1))
    3. Cursor - DB-Cursor um zu Paginaten
```python
# ./store/api_views.py
from rest_framework.generics import ListAPIView
from django_filter.rest_framework import DjangoFitlerBackend
from rest_freamwork.filters import SearchFilter

from rest_framework.pagination import LimitOffsetPagination

from store.serialiers import ProductSerializer
from store.models import Product

class ProductPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100

class ProductList(ListAPIView):
    queryset = Product.object.all()
    serializers_class = ProductSerialier

    fitler_backends = (DjangoFilterBackend, SearchFitler)
    fitler_fields = ('id') # es wird in URI ein Button für Fitlers -> id angzeigt (man kann auch mittels URI fitlern mit .../?id=3)
    search_fields = ('name', 'description') #wird von SearchFilter benutzt um name und description von URI auf Model zu mappen

    pagination_class = ProductsPagination

    # filter danach ob im Product-Model-Feld on_sale=true gesetzt ist
    def get_queryset(self): # get_queryset von ListAPIView überschreiben
        on_sale = self.request.query_params.get('on_sale', None) #GET-Option on_sale extrahieren
        if on_sale is None:
            return super().get_queryset() # wenn nicht gesetzt => Basis-Klasse get_queryset() aufrufen und returnen
        queryset = Product.object.all()
        if on_sale.lower() == 'true':
            form django.utils import timezone
            now = timezone.now()
            return qureyset.filter(
                sale_start__lte = now,
                sale_end_gte = now,
            )
        return queryset
```
* für Große Mengen an Daten sollte man Cursor Pagination benutzen
### 2 - Create, Retrieve, Update and Delelte(CRUD) Operations for Models
#### 1 - Creating a CreateAPIView subclass
* durch API neue Produkt erstellen, dafür CreateAPIView erstellen
```python
# ./store/api_views.py
# ...
from rest_framwork.excpetions import ValidatationError
from rest_framework.generics import CreateAPIView
#...

#...
class ProductCreate(CreateAPIView):
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        # try-catch benutzt um zu verhindern, dass Produkte mit WErt von 0.0 erstellt werden bzw muss zu Float umwandelbar sein
        try:
            price = request.data.get('price')
            if price is not None and float(price) <= 0.0:
                raise ValidationError({ 'price': 'Must be above $0.00' })
        except ValueError:
            raise ValicationError({ 'price': "A vaid Number is required" })
        return super().create(request, *args, **kwargs)
```
* <- so kann man Datan aus Excel, XML, JSON, anderen DBs erstellen und durch REST API ans BackEnd senden
#### 2 - Connecting a CreateAPIView to the router
* URL in `urls.py` für CreateView erstellen
```python
# ./store/api_views.py
# ...
 path('api/v1/products/new', store.api_views.ProductCreate.as_view())
# ...
```
* dann eventuell mit Postman oder curl testen + dann Postman bzw. Curl-Scripts unter Developern teilen
    * `curl -X POST http://localhost:8000/api/v1/products/new -d price=1.00 -d name="My Prodccut" -d description "Hello World"` 
    * es wird auch ein Formular in Django angezeigt, wo man neues Prod eingeben kann 

#### 3 - Creating a DestroyAPIView subclass
+ Product aus DB löschen mit DestroyView
```python
# ./store/api_views.py
# ...
from rest_framework.generics import DeleteAPIView
# ...

# ...
class ProductDestroy(DestroyAPIView):
    queryset = Product.objects.all()
    lookup_field = 'id' # welches Field durchsucht werden muss um zu löschende Obj zu löschen.
 
    def delete(self, request, *args, **kwargs): # überschreiben der delte-Methode
        product_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            # Eventuell muss man alle Daten im Cache von Django löschen, die mit diesem Produkt zusammenhängen = Cache freigeben für andere Sachen
            from django.core.cache import cache
            cache.delete('product_data_{}'.format(product_id))
        return response
```
#### 4 - Connecting a DestroyAPIView to the router
* URL in `urls.py` für CreateView erstellen
```python
# ./store/api_views.py
# ...
 path('api/v1/products/<int:id>/delete', store.api_views.ProductDelete.as_view())
# ...
```
* man kann über URI oder curl löschen:
    * `curl -X DELETE http://localhost:8000/api/v1/products/5/delete` 
#### 5 - Creating an UpdateAPIView subclass
* Also
    1. DELETE => DestroyAPIView
    2. GET => RetrieveAPIView
    3. PUT/PATCH => UpdateAPIView
ODER `RetrieveUpdataDestroyAPIView` benutzen. Vorteile:
1. Code und Config kann man dann reusen
2. eine URL für alles, die verschiedene HTTP-Methoden hat

```python
# ./store/api_views.py
from rest_framework.generics import RetrieveUpdataDestroyAPIView

class ProductRetrieveUpdateDestroy(RetrieveUpdataDestroyAPIView):
    queryset = Product.objects.all()
    lookup_field = 'id'
    serializer_class = ProductSerializer
    
     def delete(self, request, *args, **kwargs): # überschreiben der delte-Methode
        product_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            # Eventuell muss man alle Daten im Cache von Django löschen, die mit diesem Produkt zusammenhängen = Cache freigeben für andere Sachen
            from django.core.cache import cache
            cache.delete('product_data_{}'.format(product_id))
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
         if response.status_code == 204:
            # Eventuell muss man alle Daten zum Cache von Django adden, die mit diesem Produkt zusammenhängen
            from django.core.cache import cache
            product = response.data 
            cache.set('product_data_{}'.format(product['id']), {
                'name': product['name'],
                'description': product['description'],
                'price': product['price'],
            })
        return response
```
#### 6 - Connecting an UpdateAPIView to the router
* URL in `urls.py` für CreateView erstellen (eventuell destroy-URL löschen)
```python
# ./store/api_views.py
# ...
 path('api/v1/products/<int:id>/, store.api_views.ProductDelete.as_view())
# ...
```
+ wieder mit postman oder curl testen
### 3 - Managing Serializer Fields, Relations and Validation
#### 1 - Serializer with only selected fields
* in serializers.py
```python
#...
class ProductSerializer(serializers.ModelSerializer):
    is_on_sale = serializers.BooleanField(read_only=True)
    current_price = serializers.FloatField(read_only=True)
    description = serializers.CharField(min_length=2, max_length=200)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'price',
            'sale_start',
            'sale_end',
            'is_on_sale',
            'current_price',
        )
```
* `read_only` - sagt, ob der Serializer in das Feld schrieben kann oder nicht
* Weiter Optionen für Serializer-Fields:
    1. `product_name=serializers.CharField(source='name')`; = sagt, wo(im welchem Feld) sollen die Daten im Serializer übernommen werden => wenn man z.B Field überschreiben möchte

#### 2 - Serializer that shows model relationships
* in **serializers.py**
```python
#...

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCartItem
        fields = (
            'product',
            'quantity'
        )

class ProductSerializer(serializers.ModelSerializer):
    is_on_sale = serializers.BooleanField(read_only=True)
    current_price = serializers.FloatField(read_only=True)
    description = serializers.CharField(min_length=2, max_length=200)
    cart_item = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'price',
            'sale_start',
            'sale_end',
            'is_on_sale',
            'current_price',
            'cart_item'
        )

        def get_cart_items(self, instance):
            items = ShoppingCartItem.objects.filter(product=instance)
            return CartItemSerializer(item, many=True).data
```
* `SerializerMethodField` ruft per Default `get_PREFIX_OF_THE_FIELDNAME`-Methode
* `many=True` = erstellt Liste von serialisierten Model-Instanzen; `many=False` ist Default, erstell nur eine Model-Instanze
* Tests:
    1. `/.manage.py shell`
    2. `import json`
    3. `form store.models import *`
    4. `from store.serializers import *`
    5. `product = Product.objects.all().first()`
    6. `cart = ShoppingCart()`
    7. `cart.save()`
    8. `item = ShoppingCartItem(shopping_cart=cart, product=product, quantity=5)`
    9. `item.save()`
    10. `serializer = ProductSerializer(product)`
    11. `print(json.dump(serializer.data, indent=2))`

#### 3 - Number fields with serializers
* in `serializers.py` 
```python
#...

class CartItemSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(min_value=1, max_value=100)

    class Meta:
        model = ShoppingCartItem
        fields = (
            'product',
            'quantity'
        )

class ProductSerializer(serializers.ModelSerializer):
    is_on_sale = serializers.BooleanField(read_only=True)
    current_price = serializers.FloatField(read_only=True)
    description = serializers.CharField(min_length=2, max_length=200)
    cart_item = serializers.SerializerMethodField()
    price = serialiers.FloatField(min_value=1.00, max_value=100000.00) # eventuell noch max_digits, decimal_places benutzen
    price = serialiers.DecimalField(min_value=1.00, max_value=100000.00, max_digits=None, decimal_places=2)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'price',
            'sale_start',
            'sale_end',
            'is_on_sale',
            'current_price',
            'cart_item'
        )

        def get_cart_items(self, instance):
            items = ShoppingCartItem.objects.filter(product=instance)
            return CartItemSerializer(item, many=True).data
```
#### 4 - Date and time fields with serializers
* man wird hier `serializers.DateTimeField()` benutzen:
    1. `input_formats` - Input-Format für Datum
    2. `format` - ist Output-Format
    3. `help_text` = erscheint im Browser für REST API
    4. `style` - Style, wie es im Field im Browser erscheint
* in `serialisers.py`
```python
#...

class CartItemSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(min_value=1, max_value=100)

    class Meta:
        model = ShoppingCartItem
        fields = (
            'product',
            'quantity'
        )

class ProductSerializer(serializers.ModelSerializer):
    is_on_sale = serializers.BooleanField(read_only=True)
    current_price = serializers.FloatField(read_only=True)
    description = serializers.CharField(min_length=2, max_length=200)
    cart_item = serializers.SerializerMethodField()
    price = serialiers.FloatField(min_value=1.00, max_value=100000.00) # eventuell noch max_digits, decimal_places benutzen
    price = serialiers.DecimalField(min_value=1.00, max_value=100000.00, max_digits=None, decimal_places=2)
    sale_start = serializers.DateTimeField(
        input_formats=['%I:%M %p %d %B %Y'],
        format = None,
        allow_null=True,
        help_text='Accepted format is "12:01 PM 16 April 2019"',
        style={'input_type': 'text', 'placeholder': '12:01 AM 28 July 2019'}
    )
    sale_end = serializers.DateTimeField(
        input_formats=['%I:%M %p %d %B %Y'],
        format = None,
        allow_null=True,
        help_text='Accepted format is "12:01 PM 16 April 2019"',
        style={'input_type': 'text', 'placeholder': '12:01 AM 28 July 2019'}
    )


    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'price',
            'sale_start',
            'sale_end',
            'is_on_sale',
            'current_price',
            'cart_item'
        )

        def get_cart_items(self, instance):
            items = ShoppingCartItem.objects.filter(product=instance)
            return CartItemSerializer(item, many=True).data
```
* `input_formats` kann Format sein das Python String zu Time konvertieren kann; Default ist ISO-8601
#### 5 - Lists, dicts, and JSON objects
* in `serializers.py` neuen Serializer erstellen, der aber kein Model hat
```python
#....
class ProductStatusSerialisers(serializers.Serializer):
    stats = serializer.DictField(
        child = serializers.ListField(
            child = serializers.IntegerField(),
        )
    )
```
* in `api_views.py` `GenericAPIView` erstellen, d.h. komplett eigene View erstellen, da ja kein Model
```python
#...
from rest_framework import GenericAPIView
from rest_framework.response import Response #damit man eine .html-Seite für Browser erstellen kann
from store.serializers import ProductStatusSerializer
#...

class ProductStats(GenericAPIView):
    lookup_field = 'id'
    serializer_class = ProductStatSerializer
    queryset = Product.objects.all()

    def get(self, request, format=None, id=None):
        obj = self.get_object()
        serializer = ProductStatSerializer({
            'stats': {
                '2019-01-01': [5,10,15],
                '2019-01-01': [10, 1, ,1]
            }
        })
        return Response(serializer.data)
```
* in **urls.py** Path dafür einfügen
```python
#...
path('api/v1/product/<int:id>/stats', store.api_views.ProductStats.as_view())
#...
```
#### 6 - Serializer with ImageField and FileField
* in **serializers.py**
```python
# ...

class ProductSerializer(serializers.ModelSerializer):
    is_on_sale = serializers.BooleanField(read_only=True)
    current_price = serializers.FloatField(read_only=True)
    description = serializers.CharField(min_length=2, max_length=200)
    cart_item = serializers.SerializerMethodField()
    price = serialiers.FloatField(min_value=1.00, max_value=100000.00) # eventuell noch max_digits, decimal_places benutzen
    price = serialiers.DecimalField(min_value=1.00, max_value=100000.00, max_digits=None, decimal_places=2)
    sale_start = serializers.DateTimeField(
        input_formats=['%I:%M %p %d %B %Y'],
        format = None,
        allow_null=True,
        help_text='Accepted format is "12:01 PM 16 April 2019"',
        style={'input_type': 'text', 'placeholder': '12:01 AM 28 July 2019'}
    )
    sale_end = serializers.DateTimeField(
        input_formats=['%I:%M %p %d %B %Y'],
        format = None,
        allow_null=True,
        help_text='Accepted format is "12:01 PM 16 April 2019"',
        style={'input_type': 'text', 'placeholder': '12:01 AM 28 July 2019'}
    )
    photo = serializers.ImageField(default=None)
    warranty = serializirs.FileField(write_inly=True, default=None)


    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'price',
            'sale_start',
            'sale_end',
            'is_on_sale',
            'current_price',
            'cart_item',
            'photo',
            'warranty`
        )
        #...
        def update(self, isntance, validated_date):
            if validatad_date.get('warranty', None):
                instance.description += '\n\nWarranty Information:\n'
                instance.desciption += b'; '.join(
                    validated_data['warranty'].readlines()
                ).decode()
            return instance
```
* es gibt auch `write_only=True` => wird nicht in API-Response gespiechert und nicht im Model-Obj gespeichert
* `validated_data` - Daten, die schon von Serializer und Model-Validater bearbeitet wurden. Es wird benutzt, um Model zu erstellen oder upzudaten.
### 4 - Testing API Views
#### 1 - Test case for a CreateAPIView subclass
* Hat vier Typen, um API-Views zu testen:
    1. `APISimpleTestCase`
    2. `APITransasctionTestCase`
    3. `APITestCase`
    4. `APITestCase`
* alle diese Test-Klassen implementieren Django's Interface `TestCase`; Unterschied ist dass die HTTP-RestClient statd Djago-Client benutzen um zu testen
* man muus JSON-Format benutzen, wenn man API-Klient-Reqeust testen möchten: `self.client.post(url, data, format='json')`
```py tests.py
form rest_framework.test import APITestCase # statt Djangos-Tests API-Tests importieren

from store.model import Product

class ProductCreateTestCase(APITestCase):
    def test_create_product(self):
        initial_product_count = Product.objects.count() #wie viele Products momentan
        product_attrs = {
            'name': 'New Product'
            'description': 'Awesome product'
            'price': '123.45
        } # neues Product ertellen

        response = self.client.post('/api/v1/products/new', product_attrs) # Anfrage machen und Response speichern
        if resopnse.status_code != 201:
            print(response.data) # Beim Fehler von POST Daten ausgeben
        self.assertEqual(
            Pruduct.objects.count(),
            initial_product_count + 1,
        ) #Anzahl der Produkte checken
        for attr, expected_value in product_attrs.items(): # Werte des neuen Produkts checken
            self.assertEqual(response.data[attr], expected_value)
        self.assertEqual(response.data['in_on_sale'], False) #Werte dei vom Backend gesetzt werden checken
        self.assertEqual(
            response.data(['current_price'], float (product_atts['price']))
        ) #Werte dei vom Backend gesetzt werden checken
```
* Test laufen: `/manage.py test`
    * hier wird Fehler kommen => `serializer.py` korriegeren
    ```py
    #...
    class ProductSerialzer():
        #...
        sale_start = serializers.DateTime(required=False, '''..''')
        sale_end = serializers.DateTime(required=False, '''..''')

        #create überschreiben, damit warranty beim Erstellen des Obj. nicht mitbezogen wird
        def create(self, validated_data):
            validated_data.pop('warranty')
            return Product.objects.create(**validated_data)
    ```
#### 2 - Test case for a DestroyAPIView subclass
```py tests.py
#...
class ProductDestroyTestCase(APITestCase):
    def test_delete_product(self):
        initial_product_count = Product.objects.count()
        product_id = Product.objects.first().id
        self.client.delete('/api/v1/products{}/.format{product_id})
        self.assertEqual(
            Product.objects.count(),
            initial_product_count - 1,
        )
        self.assertRaises(
            Product.DoesNotExist,
            Product.objects.get, id=product_id
        )
```
* Man muss noch checken, ob Cache und weitere Daten, die mit Obj zusammenhängen auch gelöscht wurden
#### 3 - Test case for a ListAPIView subclass
* tests.py
```py
#...
class ProductListTestCase(APITestCase):
    def test_list_products(self):
        product_count = Products.objects.count()
        response = self.client.get('/api/v1/products/')
        self.assertIsNone(respose.data['next'])
        self.assertIsNone(response.data['previous'])
        self.assertEqual(response.data['count'], product_count)
        self.assertEqual(len(response.data['result']), product_count)
```
#### 4 - Unit test for an UpdateAPIView subclass
* tests.py
```py
class ProductUpdateTestCase(APITestCase):
    def test_update_product(self):
        product = Product.objects.frist()
        response = self.client.path('api/v1/products/{}/'.format{product.id}),{
            'name': 'New Product'
            'description': 'Awesome product'
            'price': '123.45
            },
            format='json'
        )
        updated = Product.objects.get(id=product.id)
        self.assertEqual(updated.name, 'New Product')
```
* es wird Error kommen
* in `serializer.py`
* tests.py
```py
#...
    def update(self, instance, validated_data):
        #...

        return super().update(instance, validated_data)
```
#### 5 - Handling image uploads in a unit test
```py
import os.path
from django.conf import settings
# ...

class ProductUpdateTestCase(APITestCase):
    #...

    def test_upload_product_photo(self):
        product = Product.objects.first()
        original_photo = product.photo
        photo_path = os.path.join(
            settings.MEDIA_ROOT, 'product', 'vitamin-iton.jpg'
        )

        with open(photo_path, 'rb') as photo_data:
            response = self.cleint.path(
                '/api/v1/products{}/'.format(product.id)
                {
                    'photo': photo_data,
                },
                format='multipart', # ist nicht JSON, da Upload ist
            )
            self.assertEqual(response.status_code, 200)

            self.assertNotEqual(resonse.data['photo'], origianl_photo)

            try: # hier wird Assertion versucht
                updated = Product.obejects.firts()
                expected_photo = os.path.join(settings.MEDIA_ROOT, 'product', 'vitamin-iton')
                self.assertTrue(
                    updated.photo.path.startswith(expected_photo)
                )
            finally: #Falls im Try etwas Schief gelaufen ist => aufräumen
                os.remove(updated.photo.path)
```
* Uploads sind wichtiger Teil, sollten au jeden Fall funktionieren
