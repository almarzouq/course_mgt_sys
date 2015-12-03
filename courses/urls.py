from django.conf.urls import url
from courses import views

urlpatterns = [
    url(r'^course/create/$', views.course_create,
        name='course_create'),
    url(r'^course/(?P<course_id>\d+)/gradecolumn/$', views.list_course_grade_column,
        name='list_course_grade_column'),
    url(r'^course/(?P<course_id>\d+)/enroll/(?P<student_id>\d+)',
        views.enroll_student_to_course, name='enroll'),
    url(r'^course/(?P<course_id>\d+)/student/(?P<student_id>\d+)/gradecolumn/(?P<gradecolumn_id>\d+)/grade/create$', views.post_student_grade,
        name='post_student_grade'),
    url(r'^course/(?P<course_id>\d+)/details/$',
        views.instructor_view_course_stundets_announcments, name='instructor_view_course_stundets_announcments'),
    url(r'^course/(?P<course_id>\d+)/student/(?P<student_id>\d+)/gradecolumn/(?P<gradecolumn_id>\d+)/grade/(?P<grade_id>\d+)/edit/$', views.edit_student_grade,
        name='edit_student_grade'),

]
