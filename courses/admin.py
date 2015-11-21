from django.contrib import admin
from .models import Course
# Register your models here.


class CourseAdmin (admin. ModelAdmin):
    list_display = ('name', 'tag', 'academic_year', 'semester',
                    'days', 'completed', 'syllabusURL', 'student_registration_open')

admin.site.register(Course, CourseAdmin)
