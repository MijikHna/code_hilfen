from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from dashboard.models import Order
from django.core import serializers


def dashboard_with_pivot(request):
    return render(
        request,
        'dashboard_with_pivot.html',
        {}
    )


def pivot_data(request):
    dataset = Order.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)  # returnt String in JSON-Format