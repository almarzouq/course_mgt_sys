from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.urlresolvers import reverse
from .forms import NewCourseForm, GradeForm, GradeColumnEditForm
from .models import GradeColumn

from students.models import Student
from courses.models import Course, CourseAnnouncement
# Create your views here.


def course_create(request):
    if request.method == 'POST':
        form = NewCourseForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect("/")
    else:
        form = NewCourseForm()
    return render(
        request,
        'course_create.html',
        {
            "form": form,
        }
    )


def list_course_grade_column(request, course_id):
    course_obj = get_object_or_404(Course, pk=course_id)
    qs = course_obj.gradecolumn_set.all()

    return render(request, "course_grade.html",
        {
            'course': course_obj,
            'gradecolumns': qs,
        }
    )


def gradecolumn_edit(request, gradecolumn_id, course_id):
    course = get_object_or_404(Course, pk=course_id)
    gc = course.gradecolumn_set.get(pk=gradecolumn_id)
    if request.method == 'POST':
        form = GradeColumnEditForm(request.POST, instance=gc)
        if form.is_valid():
            form.save()
            messages.success(request, 'GradeColumn is successfully edited.')
        return redirect(reverse('list_course_grade_column', kwargs={'course_id': course_id}))
    else:
        form = GradeColumnEditForm(instance=gc)
    return render(request,
                  'course_gradecolumn_edit.html',
                  {
                      'gradecolumn_id': gradecolumn_id,
                      'form': form,
                      'course_id': course_id,
                      'course': course,

                  })


def enroll_student_to_course(request, course_id, student_id):
    course = Course.objects.get(pk=course_id)
    student = Student.objects.get(pk=student_id)
    course.students.add(student)
    course.save()
    messages.success(request, 'The student is successfuly added.')
    return redirect('/')

def post_student_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            return redirect('/')
    else:
        form = GradeForm()
    return render(
        request,
        'post_student_grade.html',
        {
            "form": form,
        }
    )

def instructor_view_course_stundets_announcments(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    students = Student.objects.filter(course__pk=course_id)
    announcments = CourseAnnouncement.objects.filter(course__pk=course_id)
    return render(request, "course_details_announcments.html",
                  {
                      'course': course,
                      'students': students,
                      'announcments': announcments
                  }
                  )
