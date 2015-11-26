from django.conf.urls import url

from instructors import views

urlpatterns = [
    url(r'^myprofile/$', views.instructor_view, name='instructor_profile'),
    url(r'^register/$', views.InstructorRegister.as_view(),
        name='instructor_register',),
    url(r'^instructor/(?P<pk>\d+)/edit/$',
        views.InstructorEditProfile.as_view(), name='instructor_edit',),
    url(r'^instructor/(?P<pk>\d+)/$', views.instructor_view,
        name='instructor_view'),
    url(r'^appointment/$', views.AppointmentView.as_view(),
        name='take_appointment'),
    url(r'^grades/', views.GradesAdd.as_view(),name='instructor_grading',),
]
