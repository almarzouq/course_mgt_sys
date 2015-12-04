from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib import messages
from django.core.urlresolvers import reverse

from .forms import NewCourseForm, GradeForm, Grade


from students.models import Student
from courses.models import Course, CourseAnnouncement
from .models import GradeColumn
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


def view_course_gradecolumn(request, course_id, gradecolumn_id):
    course_obj = get_object_or_404(Course, pk=course_id)
    try:
        gc_obj = course_obj.gradecolumn_set.get(pk=gradecolumn_id)
    except GradeColumn.DoesNotExist as e:
        raise Http404()
    return render(request, "view_course_gradecolumn.html", {
        "gradecolumn": gc_obj,
        "course": course_obj
    }
    )


def enroll_student_to_course(request, course_id, student_id):
    course = Course.objects.get(pk=course_id)
    student = Student.objects.get(pk=student_id)
    course.students.add(student)
    course.save()
    messages.success(request, 'The student is successfuly added.')
    return redirect('/courses/course/{}/details'.format(course_id))


def post_student_grade(request, course_id, student_id, gradecolumn_id):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = GradeForm(initial={'column': gradecolumn_id,
                                  'student': student_id})
    return render(
        request,
        'post_student_grade.html',
        {
            'form': form,
            'course_id': course_id,
            'student_id': student_id,
            'gradecolumn_id': gradecolumn_id,
        }
    )
def edit_student_grade(request, course_id, student_id, gradecolumn_id, grade_id):
    grade = get_object_or_404(Grade, pk=grade_id)
    if request.method == 'POST':
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = GradeForm(instance=grade)
    return render(
        request,
        'edit_student_grade.html',
        {
            'form': form,
            'course_id': course_id,
            'student_id': student_id,
            'gradecolumn_id': gradecolumn_id,
            'grade_id': grade_id,
        }
    )


def view_student_grade(request, course_id, student_id, gradecolumn_id, grade_id):
    grade = get_object_or_404(Grade,pk=grade_id)
    return render(
        request,
        'view_student_grade.html',
        {
            'grade': grade,
            'course_id': course_id,
            'student_id': student_id,
            'gradecolumn_id': gradecolumn_id,
            'grade_id': grade_id,
        }
    )

ef delete_student_grade(request, course_id, student_id, gradecolumn_id, grade_id):
    grade = get_object_or_404(Grade, pk=grade_id)
    grade.delete()
    messages.success(request , 'Grade was successfully deleteded.')
    return redirect("/")
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


def remove_student_from_course(request, course_id, student_id):
    course = Course.objects.get(pk=course_id)
    student = Student.objects.get(pk=student_id)
    course.students.remove(student)
    course.save()
    messages.success(request, 'The student is successfuly removed.')
    return redirect(reverse('instructor_view_course_stundets_announcments', args=[course_id]))

def student_can_add_course(request, course_id, student_id):
    # this function is implemented incorrectly
    # it should check the student_registration_open
    # on course model, noura, open a ticket and fix this
    if 'student_registration_open' in request.GET:
        course = Course.objects.get(pk=course_id)
        student = Student.objects.get(pk=student_id)
        student.courses.add(course)
        student.save()
        messages.success(request, 'You are enrolled in %s' % (course))
    return redirect('/')
