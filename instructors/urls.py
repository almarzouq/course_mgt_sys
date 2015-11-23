from django.conf.urls import patterns, url
from instructors import views


urlpatterns = [
    url(r'^registor/$', views.InstructorRegister.as_view(),
        name='instructor_register',),
]
