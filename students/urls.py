from django.conf.urls import url
from students import views
from django.views.generic import ListView


from .models import Student


urlpatterns = [
    url(r'^student/(?P<pk>\d+)$', views.student_profile, name='student_view',),
    url(r'^register/$', views.StudentRegister.as_view(),
        name="student_register",),
    url(r'^student/edit/', views.edit_profile, name="student_edit",),
    url(r'^student/list', views.students_list, name='students_list',),
    url(r'^student/list/uni/$', ListView.as_view(template_name='student_list.html',
                                                 context_object_name='students',
                                                 queryset=Student.objects.order_by('university_id'),), name='student_list_order_uni'),
    url(r'^student/list/name/$', ListView.as_view(template_name='student_list.html',
                                                  context_object_name='students',
                                                  queryset=Student.objects.order_by('name'),), name='student_list_order_name'),


]
