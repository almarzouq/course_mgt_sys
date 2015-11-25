from django.conf.urls import url

from instructors import views

urlpatterns = [
    url(r'^myprofile/$', views.instructor_profile, name='instructor_profile'),
    url(r'^registor/$', views.InstructorRegister.as_view(),
        name='instructor_register',),
    url(r'^edit/(?P<pk>\d+)/profile/$', views.InstructorEditProfile.as_view(),
        name="instructor_profile_edit",),
    url(r'^profile/(?P<pk>\d+)/$', views.instructor_profile,
        name='instructor_profile'),
]
