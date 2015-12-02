from django.conf.urls import url
from students import views

urlpatterns = [
    url(r'^student/(?P<pk>\d+)$', views.student_profile, name='student_view',),
    url(r'^student/create/$', views.StudentRegister.as_view(),
        name="student_register",),
    url(r'^student/edit/(?P<student_id>\d+)$', views.edit_profile, name="student_edit",),
    url(r'^list/', views.students_list, name='students_list',),
    url(r'^filter/(?P<search_text>\w+)/$',
        views.student_search, name="student_search",),


]
