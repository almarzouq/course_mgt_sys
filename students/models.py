from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=120)
    university_id = models.BigIntegerField()
    email = models.EmailField()
    twitter_id = models.CharField(max_length=50, blank=True, default="")

    def get_absolute_url(self):
        return reverse('student_view', kwargs={'pk': self.pk})
        
    def __unicode__(self):
        return u"{}: {}".format(self.name, self.university_id)
