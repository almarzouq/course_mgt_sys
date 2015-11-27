from django.db import models
from django.core.urlresolvers import reverse


class Instructor(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, default="")
    office_hours = models.TextField(blank=True, default="")
    department = models.CharField(max_length=120, blank=True, default="")
    school = models.CharField(max_length=120, blank=True, default="")
    twitter_id = models.CharField(max_length=50, blank=True, default="")

    def get_absolute_url(self):
        return reverse('instructor_view', kwargs={'pk': self.pk})


class Appointment(models.Model):
    name = models.CharField(max_length=120)
    date_time = models.DateTimeField()
    reason = models.TextField(default="")
    email = models.EmailField()
    twitter_id = models.CharField(max_length=50, blank=True, default="")
    phone = models.CharField(max_length=20, blank=True, default="")
    approved = models.BooleanField(default=False)
    sent_1st_reminder = models.BooleanField(default=False)
    sent_2nd_reminder = models.BooleanField(default=False)

class Announcement(models.Model):
    name = models.CharField(max_length=120)
    comment = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    instructor = models.ForeignKey(Instructor)
