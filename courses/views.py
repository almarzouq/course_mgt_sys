from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib import messages

from .forms import NewCourseForm, CourseAnnouncmentForm
from .models import GradeColumn

from students.models import Student
from courses.models import Course, CourseAnnouncement
# Create your views here.


def course_create(request):
    if request.method == 'POST':
        form = NewCourseForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            return redirect()
    else:
        form = NewCourseForm()
    return render(
        request,
        'course_create.html',
        {
            "form": form,
        }
    )


class CourseGradeView(ListView):
    model = GradeColumn
    template_name = "course_grade.html"


def enroll_student_to_course(request, course_id, student_id):
    course = Course.objects.get(pk=course_id)
    student = Student.objects.get(pk=student_id)
    course.students.add(student)
    course.save()
    messages.success(request, 'The student is successfuly added.')
    return redirect('/')


def create_course_announcment(request, course_id):
   inst = get_object_or_404(Course, pk=course_id)
   if request.method == 'POST':
       form = CourseAnnouncmentForm(request.POST, instance=inst)
       if form.is_valid():
           form.save()
           return redirect('/')
   else:
       form = CourseAnnouncmentForm(instance=inst)
   return render(
       request,
       'create_course_announcment.html',
       {
           'course': inst,
           'form': form
       })
