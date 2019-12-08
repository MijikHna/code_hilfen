from django.shortcuts import render

#Eigene Imports:
from django.http import HttpResponse

from .models import Pet

#im in der Excpetion 404 zu erzeugen
from django.http import Http404

# Create your views here.
def home(request):
    pets = Pet.objects.all()

    #render-Funktion:
    #2-Template-Name
    #3-Variablen, die in Template eingesetzt werden, sollte Dictionary sein.
    return render(request, "home.html", {"pets": pets})

    #return HttpResponse("<p> home view </p>")

def pet_detail(request, id):
    try:
        pet = Pet.objects.get(id=id)
    except Pet.DoesNotExist:
        raise Http404("Pet not found")
    return render(request, "pet_detail.html", {"pet":pet} )


    #return HttpResponse("<p> pet_detail view with the id {} </p>".format(id))  #{} ist Platzhalter
