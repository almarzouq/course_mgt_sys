from django.contrib import admin
from .models import Instructor


class InstructorAdmin (admin. ModelAdmin):
    list_display = ('name', 'email', 'phone', 'office_hours',
                    'department', 'school', 'twitter_id')

admin.site.register(Instructor, InstructorAdmin)
