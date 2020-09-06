#### Django Features:

1. Class-based vs. Function-Based Views
2. Models
3. Objects with Queries

#### 1 - Class-based vs. Function-based Views

* function-based views: bessere Kontrolle, gut bei komplexer Logik
    1. man muss selbst entsprechende Methoden für views schreiben.
    2. man muss gucken, welche Django Methode man umschreiben/implementieren muss, um Requests zu bearbeiten und Daten an Views senden.
    3. Unit-Testing wird schwieriger
* class-based views:
    1. haben Templates, um CRUD(create, read, update, delete) zu performen
    2. sind leichter zu implementieren, weniger wiederholder Code.
    3. Weniger Tests, da Django hat schon Tests für die generischen Views
        1. oft nur die Erweiterung der Generischen Views testen

#### Django Models

* Models für Authentication: `User` und `Permission` z.B:

```py
class StaffMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.OneToOneField(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.company.name + " - " + self.user.email
```

#### Objects mit Queries bekommen

* mit Models Manager (`objects`) um QuerySets zu erstellen
* Doku zu QueryAPI: https://docs.djangoproject.com/en/3.0/ref/models/querysets/#django.db.models.query.QuerySet
* die Methoden der QueryAPI können verkettet werden z.B

```py
Post.objects.filter(
    type="new"
).exclude(
    title__startswith="Blockchain"
)
```
* Möglich, da einige Query-Methoden wieder QuerySet zurückliefert z.B `fitler()` oder `exclude()`