from django.db import models

# Create your models here.
class Pet(models.Model):
    #Tuppels für choises
    SEX_CHOISES = [("M", "Male"), ("F", "Female")]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True)
    description = models.TextField()
    sex = models.CharField(choices=SEX_CHOISES, max_length=1, blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)
    vaccinations = models.ManyToManyField("Vaccine", blank=True)

class Vaccine(models.Model):
    name = models.CharField(max_length=50)

    #da Vaccine ist ManytoMany in Pet => Django gibt per Default einfach "Vaccine object" (Modelname + "Object") bei Verknüpfungen => __str__ überschreiben
    def __str__(self):
        return self.name
