from django.conf.urls import url
from instructors import views

urlpatterns = [
    url(r'^instructor/create/$', views.InstructorCreate.as_view(),
        name='instructor_create',),
    url(r'^instructor/(?P<pk>\d+)/edit/$',
        views.InstructorEditProfile.as_view(), name='instructor_edit',),
    url(r'^instructor/(?P<pk>\d+)/$', views.instructor_view,
        name='instructor_view'),
    url(r'^instructor/(?P<pk>\d+)/appointment/create/$',
        views.appointment_create, name='take_appointment'),
    url(r'^appointment/(?P<appointment_id>\d+)/$', views.intructor_student_can_view_appoinment_detail,
        name='appointment_details'),
    url(r'^appointment/list/$', views.AppointmentList.as_view(),
        name='appointment_list',),
    url(r'^instructor/(?P<instructor_id>\d+)/create/announcement$', views.create_general_announcment,
        name='create_general_announcment',),
    url(r'^appointment/(?P<pk>\d+)/edit/$', views.AppointmentEdit.as_view(),
        name='appointment_edit',),
    url(r'^instructor/(?P<pk>\d+)/appointments$',
        views.appointment_view, name='appointment_view'),
    url(r'^appointment/(?P<pk>\d+)/approvel/$',
        views.appointment_approve_decline, name='appointment_approvel'),
    url(r'^appointment/(?P<pk>\d+)/approve/$',
        views.appointment_approve, name='appointment_approve'),
    url(r'^appointment/(?P<pk>\d+)/decline/$',
        views.appointment_decline, name='appointment_decline'),




]
