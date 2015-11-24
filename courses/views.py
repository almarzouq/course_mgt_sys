from django.shortcuts import render
from django.http import HttpResponse

from .models import Student
from courses.models import Course
# Create your views here.
def enroll(request, name):
    try:
        course_name = request.GET['course']
    except:
        return HttpResponse("Please provide a course to enroll in.")

    courses = Course.objects.filter(name=course_name)
    if len(courses) == 0:
        return HttpResponse("No course called " + course_name + " exists")
    course = courses[0]

    students = Student.objects.filter(name=name)
    if len(students) == 0:
        student = Student(name=name)
    else:
        student = students[0]

    if course.student_set.filter(pk=student.pk).exists():
        return HttpResponse("Already enrolled")

    student.courses.add(course)
    student.save()
    return HttpResponse("Enrolled in " + course.name)
