from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Courses(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    time = models.TimeField(null=True, blank=True)
    url = models.CharField(null=True, blank=True, max_length=15)
    # image = models.ImageField(null=True, blank=True)
    active = models.BooleanField(default=False)



    def __str__(self):
        return self.title
class Students(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='myuser')
    course = models.ManyToManyField(Courses, blank=True, related_name='mescours')

    def __str__(self):
        return self.user.first_name

class Pin(models.Model):
    pin = models.CharField(max_length=6, unique=True)
    used = models.BooleanField(default=False)
