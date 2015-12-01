from django.conf.urls import url

from instructors import views

urlpatterns = [
    url(r'^myprofile/$', views.instructor_view, name='instructor_profile'),
    url(r'^create/$', views.InstructorCreate.as_view(),
        name='instructor_create',),
    url(r'^instructor/(?P<pk>\d+)/edit/$',
        views.InstructorEditProfile.as_view(), name='instructor_edit',),
    url(r'^instructor/(?P<pk>\d+)/$', views.instructor_view,
        name='instructor_view'),
    url(r'^appointment/create/$', views.CreateAppointment.as_view(),
        name='take_appointment'),
    url(r'^grades/', views.GradesAdd.as_view(), name='instructor_grading',),
    url(r'^gradecolumn/(?P<gradecolumn_id>\d+)/$',
        views.gradecolumn_edit, name='gradecolumn_edit',),
    url(r'^appointment/(?P<appointment_id>\d+)/details/$', views.intructor_student_can_view_appoinment_detail,
    name='appointment_details'),
    url(r'^appointment/list/$', views.AppointmentList.as_view(),
        name='appointment_list',),


]
