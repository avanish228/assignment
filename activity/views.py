from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json
from .formatData import getViewData


def Activities(request):
    responce=json.dumps(getViewData())
    return HttpResponse(responce, content_type="text/json-comment-filtered")