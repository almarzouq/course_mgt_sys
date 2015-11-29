from django.shortcuts import redirect
from django.contrib import messages

from .models import Student
from courses.models import Course
# Create your views here.


def enroll_student_to_course(request, course_id, student_id):
    course = Course.objects.filter(course_id=Course.pk)
    student = Student.objects.filter(student_id=Student.pk)
    student.courses.add(course)
    student.save()
    messages.success(request, 'The student is successfuly added.')
    return redirect('/some/url/')
