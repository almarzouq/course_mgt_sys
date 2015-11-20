from django.contrib import admin
from .models import Student

class StudentAdmin (admin. ModelAdmin ):
	list_display = ('name' ,'email', 'university_id' , "twitter_id")

admin.site.register(Student , StudentAdmin)