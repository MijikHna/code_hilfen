from django.db import models

# Create your models here.
class Job(models.Model):
    #Images:
    image = models.ImageField(upload_to="images/")  #Klassenattribut, dass vom Typ Image ist(param = wo die Images gespeichert werden)
        #<- um mit Images zu arbeiten muss man pip3 Pillow installieren -> sudo pip3 install pillow
    #summary:
    summary = models.CharField(max_length=200)

    #Methoden
    def __str__(self):
        return self.summary
