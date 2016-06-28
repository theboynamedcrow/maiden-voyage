from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Golfer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=60,blank=True,null=True)
    name = models.CharField(max_length=60,blank=True,null=True)
    handicap = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.name
