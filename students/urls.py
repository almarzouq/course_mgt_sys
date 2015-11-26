from django.conf.urls import url
from students import views


urlpatterns = [
    url(r'^profile/(?P<student_id>\d+)$', views.student_profile, name='student_view',),
    url(r'^register/$', views.StudentRegister.as_view(),
        name="student_register",),
    url(r'^edit/', views.edit_profile, name="student_edit",),

]
