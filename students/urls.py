from django.conf.urls import patterns , url
from students import views
urlpatterns = [
	url(r'^myprofile/$' , views.student_profile , name='student_profile'),
	]