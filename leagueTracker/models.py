from django.db import models

# Create your models here.
class User(models.Model):
    display_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70, null=True, unique=True)
    date_joined = models.DateTimeField('date joined')
    def __str__(self):
        return self.display_name


class Golfer(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=60)
    handicap = models.IntegerField(default=0)
    def __str__(self):
        return self.name
