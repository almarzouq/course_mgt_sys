from django.contrib import admin
from .models import Instructor, Announcement


class InstructorAdmin (admin. ModelAdmin):
    list_display = ('name', 'email', 'phone', 'office_hours',
                    'department', 'school', 'twitter_id')


class AnnouncementAdmin (admin. ModelAdmin):
   list_display = ('name', 'comment', 'submitted_at')

admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
