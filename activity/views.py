from django.shortcuts import render

# Create your views here.
from django.core import serializers
from django.http import HttpResponse
from .models import ActivityPeriod
import json
from .models import User
from datetime import datetime


def Activities(request):
    #posts = User.objects.values('user_id','real_name','tz')
    posts = User.objects.all().values()
    print(list(posts))
    member=[]
    l=list(posts)
    for i in l:
        user={}
        s=i['id']
        user.update({'id' : i['user_id']})
        user.update({'real_name': i['real_name']})
        user.update({'tz': i['tz']})
        adata=list(ActivityPeriod.objects.filter(user=s).values('start_time','end_time'))
        activityLIst=[]
        for a in adata:
            a['start_time']=a['start_time'].strftime("%b %d %Y %H:%M %p")
            a['end_time'] = a['end_time'].strftime("%b %d %Y %H:%M %p")
            activityLIst.append(a)
        print("Activity data ")
        user.update({'activity_periods': activityLIst})
        member.append(user)
    f={'ok': 'true' ,'members':member}
    responce=json.dumps(f)
    #print("List Responxe "+responce +" LIst response competed")
    #post_list = serializers.serialize('json', posts)
    return HttpResponse(responce, content_type="text/json-comment-filtered")