from django.conf.urls import include, url
from students import views

urlpatterns = [
url(r'^register/$',views.StudentRegister.as_view(),name="student_register",),
]
