from django.db import models
from django.contrib.auth.models import User

class UserStats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    gender = models.CharField(max_length=10, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

    weight = models.FloatField(default=0)
    weight_unit = models.CharField(max_length=10, default='kg')

    bmi = models.FloatField(default=0)
    bmr = models.FloatField(default=0)

    height_cm = models.FloatField(null=True, blank=True)
    activity = models.CharField(max_length=100, null=True, blank=True)

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username