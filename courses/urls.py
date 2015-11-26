from django.conf.urls import url
from courses import views

urlpatterns = [
    url(r'^course/create/$', views.course_create,
        name='course_create'),

]
