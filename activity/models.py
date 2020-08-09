from django.db import models

# Create your models here.

class User(models.Model):
    user_id=models.CharField(max_length=250)
    real_name=models.CharField(max_length=250)
    tz=models.CharField(max_length=250)

class ActivityPeriod(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

