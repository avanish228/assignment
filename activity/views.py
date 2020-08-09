from django.shortcuts import render

# Create your views here.
from django.core import serializers
from django.http import HttpResponse
from .models import ActivityPeriod
from .models import User


def Activities(request):
    posts = ActivityPeriod.objects.all()
    post_list = serializers.serialize('json', posts)
    return HttpResponse(post_list, content_type="text/json-comment-filtered")