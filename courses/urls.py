from django.conf.urls import url
from courses import views

urlpatterns = [
    url(r'^course/create/$', views.course_create,
        name='course_create'),
    url(r'^course/(?P<course_id>\d+)/grade/$', views.list_course_grade_column,
        name='list_course_grade_column'),
    url(r'^course/(?P<course_id>\d+)/enroll/(?P<student_id>\d+)',
        views.enroll_student_to_course, name='enroll'),

]
