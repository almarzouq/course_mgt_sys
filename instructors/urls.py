from django.conf.urls import url

from instructors import views

urlpatterns = [
    url(r'^profile/(?P<pk>\d+)/$', views.instructor_profile,
        name='instructor_profile'),
]
