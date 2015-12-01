from django.conf.urls import url
from students import views


urlpatterns = [
    url(r'^student/(?P<pk>\d+)$', views.student_profile, name='student_view',),
    url(r'^register/$', views.StudentRegister.as_view(),
        name="student_register",),
    url(r'^student/edit/', views.edit_profile, name="student_edit",),
    url(r'^student/list',views.students_list, name='students_list',),

]
