from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from instructors import views


urlpatterns = [
    url(r'^instructor/create/$', views.instructor_create,
        name='instructor_create',),
    url(r'^instructor/(?P<pk>\d+)/$', views.instructor_view,
        name='instructor_view'),
    url(r'^instructor/list/$', views.instructors_list,
        name='instructor_list'),
    url(r'^instructor/(?P<pk>\d+)/edit/$',
        views.InstructorEditProfile.as_view(), name='instructor_edit',),
    url(r'^instructor/(?P<instructor_id>\d+)/announcement/create/$',
        views.create_general_announcment, name='create_general_announcment',),
    url(r'^announcement/(?P<pk>\d+)/edit/$',
        views.AnnouncementEdit.as_view(), name='edit_general_announcment',),
    url(r'^instructor/(?P<pk>\d+)/appointment/create/$',
        views.appointment_create, name='take_appointment'),
    url(r'^appointment/(?P<appointment_id>\d+)/$',
        views.intructor_student_can_view_appoinment_detail,
        name='appointment_details'),
    url(r'^instructor/(?P<pk>\d+)/appointments/$',
        views.appointment_view__for_specific_instructor,
        name='appointment_view'),
    url(r'^appointment/list/$', views.AppointmentList.as_view(),
        name='appointment_list',),
    url(r'^appointment/(?P<pk>\d+)/edit/$',
        login_required(views.AppointmentEdit.as_view()),
        name='appointment_edit',),
    url(r'^appointment/(?P<pk>\d+)/delete/$',
        views.appointment_delete, name='appointment_delete',),
    url(r'^appointment/(?P<pk>\d+)/approve/$',
        views.appointment_approve, name='appointment_approve'),
    url(r'^appointment/(?P<pk>\d+)/decline/$',
        views.appointment_decline, name='appointment_decline'),
    url(r'^/instructor/(?P<pk>\d+)/pending/appointment/list/$', views.pending_appointment_list,
        name='pending_appointment_list',),

]
