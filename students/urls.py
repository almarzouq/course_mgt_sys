from django.conf.urls import url
from students import views


urlpatterns = [
    url(r'^student/(?P<pk>\d+)$', views.student_profile, name='student_view',),
    url(r'^register/$', views.StudentRegister.as_view(),
        name="student_register",),
    url(r'^student/edit/', views.edit_profile, name="student_edit",),
    url(r'^student/filter/(?P<search_text>\w+)$',views.student_search,name="student_search",),

]
