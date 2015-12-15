from django.contrib import admin

from .models import Course, GradeColumn, CourseAnnouncement , Lecture
# Register your models here.


class GradeColumnInline(admin.StackedInline):
    model = GradeColumn


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'tag', 'academic_year', 'semester',
                    'days', 'completed', 'syllabusURL',
                    'student_registration_open')
    inlines = [GradeColumnInline, ]

class CourseAnnouncementAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment', "course")



admin.site.register(Course, CourseAdmin)
admin.site.register(CourseAnnouncement, CourseAnnouncementAdmin)
admin.site.register(Lecture)
