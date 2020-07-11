from django.db import models

# Create your models here.
class Courses(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    time = models.TimeField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)


    def __str__(self):
        return self.title
