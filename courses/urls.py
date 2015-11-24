from django.conf.urls import patterns, url

from courses import views

urlpatterns = [
  url(r'^(?P<name>\w{0,120})/enroll$', views.enroll, name='enroll'),
]
