from  django.conf.urls import  include, url
from  students import  views


urlpatterns = [
    url(r'^register/$',views.StudentRegister.as_view(),name="student_register",),
    url(r'^edit/',views.edit_profile , name="student_profile_edit",),
]
