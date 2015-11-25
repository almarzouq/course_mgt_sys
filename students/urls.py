from django.conf.urls import url
from students import views


urlpatterns = [
    url(r'^myprofile/$', views.student_profile, name='student_profile'),
    url(r'^register/$', views.StudentRegister.as_view(),
        name="student_register",),
    url(r'^edit/', views.edit_profile, name="student_edit",),

]
