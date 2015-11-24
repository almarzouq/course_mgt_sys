from django.db import models
from django.utils.translation import ugettext as _

from students.models import Student

# Create your models here.


class Course(models.Model):
    SEMESTER = (
        ('FA', _('Fall')),
        ('SP', _('Spring')),
        ('SU', _('Summer')),
    )

    DAYS = (
        ('24', _('Mondays/Wednesdays')),
        ('135', _('Sundays/Tuesdays/Thursdays')),
        ('E', _('Everyday')),
    )

    name = models.CharField(max_length=120)
    tag = models.CharField(max_length=20)
    academic_year = models.CharField(max_length=120, help_text=_('E.g.: 2015/2016'))
    semester = models.CharField(max_length=2, choices=SEMESTER)
    days = models.CharField(max_length=3, choices=DAYS)
    completed = models.BooleanField(default=False)
    syllabusURL = models.URLField()
    student_registration_open = models.BooleanField(default=True)
    students = models.ManyToManyField(Student)


class GradeColumn(models.Model):
    name = models.CharField(max_length=120)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    course = models.ForeignKey(Course)


class Grade(models.Model):
    column = models.ForeignKey(Student)
    course = models.ForeignKey(Course)
    value = models.DecimalField(max_digits=5, decimal_places=2)
