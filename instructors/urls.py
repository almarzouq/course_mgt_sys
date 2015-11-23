from django.conf.urls import patterns, url
from instructors import views

urlpatterns = [
    url(r'^myprofile/$', views.instructor_profile, name='instructor_profile'),
    url(r'^announcement/$', views.AnnouncementView.as_view(),
        name='announcement_view',),

]
