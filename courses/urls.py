from django.conf.urls import url
from courses import views

urlpatterns = [
    url(r'^course/create/$', views.course_create,
        name='course_create'),
    url(r'^course/grade/$', views.CourseGradeView.as_view(),
        name='course_grade'),
    url(r'^course/(?P<course_id>\d+)/enroll/(?P<student_id>\d+)',
        views.enroll_student_to_course, name='enroll'),
    url(r'^course/(?P<course_id>\d+)/student/(?P<student_id>\d+)/gradecolumn/(?P<gradecolumn_id>\d+)/grade/create$', views.post_student_grade,
    name='post_student_grade'),


]
