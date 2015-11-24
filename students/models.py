from django.db import models
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=120)
    university_id = models.BigIntegerField()
    email = models.EmailField()
    twitter_id = models.CharField(max_length=50, blank=True, default="")
