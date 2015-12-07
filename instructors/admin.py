from django.contrib import admin

from .models import Instructor, Announcement, Appointment


class InstructorAdmin (admin. ModelAdmin):
    list_display = ('name', 'email', 'phone', 'office_hours',
                    'department', 'school', 'twitter_id')


class AnnouncementAdmin (admin. ModelAdmin):
    list_display = ('name', 'comment', 'submitted_at')


class AppointmentAdmin (admin. ModelAdmin):
    list_display = ('name', 'date_time', 'reason', 'email', 'twitter_id',
                    'phone')

admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Appointment, AppointmentAdmin)
