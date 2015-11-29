from django.conf.urls import patterns, url

from courses import views

urlpatterns = [
  url(r'^course/{course_id}/enroll/{student_id}', views.enroll_student_to_course, name='enroll'),
]
