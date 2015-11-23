from django.conf.urls import patterns, url
from instructors import views
from django.contrib.auth. decorators import login_required

urlpatterns = [
    url(r'^myprofile/$', views.instructor_profile, name='instructor_profile'),
    url(r'^announcement/$', login_required(views.AnnouncementView.as_view()),
        name='announcement_view',),

]
