from django.contrib import admin

from .models import Course, GradeColumn
# Register your models here.


class GradeColumnInline(admin.StackedInline):
    model = GradeColumn


class CourseAdmin (admin. ModelAdmin):
    list_display = ('name', 'tag', 'academic_year', 'semester',
                    'days', 'completed', 'syllabusURL',
                    'student_registration_open')
    inlines = [GradeColumnInline, ]

admin.site.register(Course, CourseAdmin)
