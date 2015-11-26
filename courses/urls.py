from django.conf.urls import url
from courses import views

urlpatterns = [
    url(r'^course/create/$', views.course_create,
        name='course_create'),
    url(r'^course/grade$', views.CourseGradeView.as_view(),
        name='course_grade')
]
