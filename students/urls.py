from django.conf.urls import url
from students import views
from django.views.generic import ListView


from .models import Student


urlpatterns = [
    url(r'^student/(?P<pk>\d+)$', views.student_profile, name='student_view',),
    url(r'^register/$', views.StudentRegister.as_view(),
        name="student_register",),
    url(r'^student/edit/', views.edit_profile, name="student_edit",),
    url(r'^student/list$', views.students_list, name='students_list',),
    url(r'^student/list/uni/$', views.StudentListUni.as_view(), name='student_list_order_uni'),
    url(r'^student/list/name/$', views.StudentListName.as_view(), name='student_list_order_name'),


]
