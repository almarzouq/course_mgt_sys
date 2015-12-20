from django.conf.urls import url
from students import views
from django.views.generic import ListView


from .models import Student

urlpatterns = [
    url(r'^student/(?P<pk>\d+)$', views.student_profile, name='student_view',),
    url(r'^student/create/$', views.StudentRegister.as_view(),
        name="student_register",),
    url(r'^student/edit/$', views.edit_profile, name="student_edit",),

    url(r'^student/instructor/edit/(?P<pk>\d+)$',views.instructor_edit_profile,name="instructor_student_edit",),
    url(r'^filter/(?P<search_text>\w+)/$',
        views.student_search, name="student_search",),
    url(r'^list$', views.students_list, name='students_list',),
    url(r'^list/uni/$', views.StudentListUni.as_view(), name='student_list_order_uni'),
    url(r'^list/name/$', views.StudentListName.as_view(), name='student_list_order_name'),
]
