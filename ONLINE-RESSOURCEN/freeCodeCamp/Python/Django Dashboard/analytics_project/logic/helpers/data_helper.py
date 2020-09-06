from django.http import request

from django.http import JsonResponse
from dashboard.models import Order
from django.core import serializers

import analytics_project.logic.helpers.data_helper


def pivot_data(request):
    dataset = Order.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)
