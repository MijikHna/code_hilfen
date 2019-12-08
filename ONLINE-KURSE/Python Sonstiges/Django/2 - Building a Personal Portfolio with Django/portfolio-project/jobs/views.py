from django.shortcuts import render
from django.shortcuts import get_object_or_404

#meine Imports:
from .models import Job
# Create your views here.

#meine Funktionen:
def nick(request):
    return render(request, "jobs/nick.html")

def home(request):
    jobs = Job.objects  # alle Jobs aus der DB holen.
    return render(request, "jobs/home.html", {"jobs" : jobs}) # {} jobs = Variable die in html-Template benutzt wird, : jobs = Variable, die jobs so zu sagen übergeben wird

def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/detail.html', {'job':job_detail})
