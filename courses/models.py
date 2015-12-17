from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse

from students.models import Student
from instructors.models import Instructor
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
    academic_year = models.CharField(
        max_length=120, help_text=_('E.g.: 2015/2016'))
    semester = models.CharField(max_length=2, choices=SEMESTER)
    days = models.CharField(max_length=3, choices=DAYS)
    completed = models.BooleanField(default=False)
    syllabusURL = models.URLField(null=True, blank=True)
    student_registration_open = models.BooleanField(default=True)
    students = models.ManyToManyField(Student, through='CourseStudent')
    instructor = models.ForeignKey(Instructor, blank=True)

    def __unicode__(self):
        return u" {} : {} : {} : {} ".format(
            self.name,
            self.instructor.name,
            self.days,
            self.semester)

    def __str__(self):
        return u" {} : {} : {} : {} ".format(
            self.name,
            self.instructor.name,
            self.days,
            self.semester)

    def get_absolute_url(self):
        return reverse(
            'instructor_view_course_stundets_announcments',
            kwargs={'course_id': self.pk})


class CourseStudent(models.Model):
    course = models.ForeignKey(Instructor)
    student = models.ForeignKey(Student)

    # student cannot register in same course twice
    class Meta:
        unique_together = ('course', 'student')


class GradeColumn(models.Model):
    name = models.CharField(max_length=120)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    course = models.ForeignKey(Course)
    description = models.TextField(blank=True)


class Grade(models.Model):
    column = models.ForeignKey(GradeColumn)
    student = models.ForeignKey(Student)
    value = models.DecimalField(max_digits=5, decimal_places=2)


class CourseAnnouncement(models.Model):
    name = models.CharField(max_length=120)
    comment = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course)

    def get_absolute_url(self):
        return reverse(
            'instructor_view_course_stundets_announcments',
            kwargs={'course_id': self.course_id})


class Lecture(models.Model):
    name = models.CharField(max_length=120)
    course = models.ForeignKey(Course)
    time_of_lecture = models.DateTimeField(auto_now=True)
    number_of_students = models.BigIntegerField(null=True, blank=True)

    def __unicode__(self):
        return u"{} : {} : {} ".format(self.course.name, self.name, self.time_of_lecture)

    def __str__(self):
        return u"{} : {} : {} ".format(self.course.name, self.name, self.time_of_lecture)

    def get_absolute_url(self):
        return reverse('lecture_details', kwargs={'lecture_id': self.pk, 'course_id': self.course.pk})


class Attendance(models.Model):
    lecture = models.ForeignKey(Lecture)
    student = models.ForeignKey(Student)
    time_attended = models.DateTimeField(auto_now=True, null=True)
    attended = models.BooleanField(default=False)

    class Meta:
        unique_together = ('lecture', 'student')

    def __unicode__(self):
        return u"{} : {} : {} ".format(self.lecture.course.name, self.lecture.name, self.lecture.time_of_lecture)

    def __str__(self):
        return u"{} : {} : {} ".format(self.lecture.course.name, self.lecture.name, self.lecture.time_of_lecture)
