from django.conf.urls import url
from courses import views

urlpatterns = [
    url(r'^course/create/$', views.course_create,
        name='course_create'),
    url(r'^course/grade/$', views.CourseGradeView.as_view(),
        name='course_grade'),
    url(r'^course/{course_id}/enroll/{student_id}',
        views.enroll_student_to_course, name='enroll'),

]