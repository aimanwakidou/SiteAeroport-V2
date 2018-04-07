from django.shortcuts import render
from django.http import HttpRequest,JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from app.models import *
import json

# Create your views here.

# flights
@csrf_protect
def flights(request):
    """
    Calling this method will search all flights matching with post parameters
    """
    
    assert isinstance(request,HttpRequest)

    if request.method == "GET" or not request.is_ajax():
        return HttpResponse(status=403)

    try:
        data_raw = request.body.decode("UTF-8")
        data = json.loads(data_raw)
        departure_id = data["departure_id"]
        arrival_id = data["arrival_id"]

        return JsonResponse({
            'test_flights':True
        })

    except KeyError:
        return HttpResponse(status=500)

# luggage
def luggage(request):
    """
    Calling this method with search luggage for an user matching with post parameters
    """
    assert isinstance(request,HttpRequest)
    return JsonResponse({
        'test_luggage':True
    })
   

