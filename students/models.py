from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=120)
    university_id = models.BigIntegerField(null=True, blank=True)
    email = models.EmailField()
    twitter_id = models.CharField(max_length=50, null=True, blank=True, default="")
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('student_view', kwargs={'pk': self.pk})

    def __unicode__(self):
        return u"{} : {}".format(self.name, self.university_id)

    def __str__(self):
        return "{} : {}".format(self.name, self.university_id)
