from .models import ActivityPeriod
from .models import User


def getViewData():
    users = User.objects.all().values()
    member=[]
    listofUsers=list(users)
    for i in listofUsers:
        user={}
        user.update({'id' : i['user_id']})
        user.update({'real_name': i['real_name']})
        user.update({'tz': i['tz']})
        adata=list(ActivityPeriod.objects.filter(user=i['id']).values('start_time','end_time'))
        activityLIst=[]
        for a in adata:
            a['start_time']=a['start_time'].strftime("%b %d %Y %H:%M %p")
            a['end_time'] = a['end_time'].strftime("%b %d %Y %H:%M %p")
            activityLIst.append(a)
        user.update({'activity_periods': activityLIst})
        member.append(user)
    return {'ok': 'true' ,'members':member}