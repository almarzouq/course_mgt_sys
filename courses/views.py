from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic.edit import UpdateView
from django.views.generic import DetailView

from .forms import NewCourseForm, GradeForm, Grade


from students.models import Student
from courses.models import Course, CourseAnnouncement, Grade, GradeColumn, Lecture , Attendance

from .forms import (NewCourseForm, GradeForm,
                    GradeColumnEditForm, CourseAnnouncmentForm,
                    GradeColumnCreateForm,AttendanceStudentForm, InstructorLectureForm)
from .models import GradeColumn
# Create your views here.


def course_create(request):
    if request.method == 'POST':
        form = NewCourseForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect(obj)
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

    return render(request, "course_gradecolumn_list.html",
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
    return redirect(reverse('instructor_view_course_stundets_announcments', args=[course_id]))


def post_student_grade(request, course_id, student_id, gradecolumn_id):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('list_student_grade', args=(course_id, student_id,)))

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
            messages.success(request, 'Grade was successfully Edited.')
            return redirect(reverse('list_student_grade', args=(course_id, student_id,)))
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
    grade = get_object_or_404(Grade, pk=grade_id)
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


def list_student_grade(request, course_id, student_id):
    course_obj = get_object_or_404(Course, pk=course_id)
    gradecolumns = course_obj.gradecolumn_set.all()
    student = get_object_or_404(Student, pk=student_id)
    grades = student.grade_set.all()

    student_grade_value_list = []
    student_grade_column_list = []
    student_grade_value_dict = {}
    student_grade_column_dict = {}

    for gc in gradecolumns:
        student_grade_value_dict = {}
        student_grade_column_dict = {}
        student_grade_column_dict[gc.total] = gc.name
        for g in grades:
            if gc.pk == g.column.pk:
                student_grade_value_dict[g.pk] = g.value
        if len(student_grade_value_dict) < len(student_grade_column_dict):
            student_grade_value_dict[gc.pk] = ''
        student_grade_column_list.append(student_grade_column_dict)
        student_grade_value_list.append(student_grade_value_dict)
        # cycle to change color background in table
    return render(
        request,
        'list_student_grade.html',
        {
            'course_id': course_id,
            'student_id': student_id,
            'student_grade_column': student_grade_column_list,
            'student_grade_value': student_grade_value_list,
            'student': student,
        }
    )


def delete_student_grade(request, course_id, student_id, gradecolumn_id, grade_id):
    grade = get_object_or_404(Grade, pk=grade_id)
    grade.delete()
    messages.success(request, 'Grade was successfully deleteded.')
    return redirect(reverse('list_student_grade', args=(course_id, student_id,)))


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
    course = Course.objects.get(pk=course_id)
    student = Student.objects.get(pk=student_id)
    if course.student_registration_open:
        course.students.add(student)
        student.save()
        messages.success(request, 'You are enrolled in %s' % (course))
    else:
        messages.success(
            request, 'You are not allowed to enroll in this course talk to your instructor')
    return redirect(reverse('instructor_view_course_stundets_announcments', args=[course_id]))


def create_course_announcment(request, course_id):
    if request.method == 'POST':
        form = CourseAnnouncmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('instructor_view_course_stundets_announcments', kwargs={'course_id': course_id}))
    else:
        form = CourseAnnouncmentForm(initial={'course': course_id, })
    return render(
        request,
        'create_course_announcment.html',
        {
            'form': form,
            'course_id': course_id,
        })


class CourseEdit(UpdateView):
    model = Course
    template_name = "course_edit.html"
    context_object_name = "course"
    fields = '__all__'


def list_of_courses_to_add(request):
    qs = Course.objects.all()
    return render(
        request,
        'course_list_to_add.html',
        {
            'courses': qs,
            'student_id': request.GET.get("student_id")
        }
    )


def student_attendance(request, course_id, student_id):
    if request.method == 'POST':
        form = AttendanceStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
            form = AttendanceStudentForm(initial={'course': course_id, 'student' : student_id })

    return render(request,'lecture_attendance.html',{'form': form,'course_id': course_id,'student_id': student_id,})


def instructor_lecture(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = InstructorLectureForm(request.POST)
        if form.is_valid():
            form.save()
            obj = form.save()

            return redirect(reverse('lecture_details',kwargs = {'course_id' : course_id, 'lecture_id' : obj.pk }))
    else:

        form = InstructorLectureForm(initial={'course': course_id, })

    return render(request, 'create_lecture.html', {
        'form': form,
        'course_id': course_id,
        'course': course,
    })




def lecture_details(request, lecture_id, course_id):
    obj = Lecture.objects.get(pk=lecture_id)
    qs = Course.objects.filter(pk=course_id)
    qs2 = Attendance.objects.filter(lecture__pk=lecture_id)
    return render(request, 'lecture_details.html',{'lecture' : obj,'attended' : qs2,'course' : qs,})


def gradecolumn_delete(request, course_id, gradecolumn_id):
    course = get_object_or_404(Course, pk=course_id)
    qs = course.gradecolumn_set.get(pk=gradecolumn_id)
    qs.delete()
    messages.success(request, 'Grade Column was successfully deleted.')
    return redirect(reverse('list_course_grade_column', kwargs={
        'course_id': course.pk,
    }))


def gradecolumn_create(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = GradeColumnCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('list_course_grade_column', kwargs={
                'course_id': course_id}))
    else:
        form = GradeColumnCreateForm(initial={'course': course_id, })
    return render(
        request,
        'gradecolumn_create.html',
        {
            'form': form,
            'course': course
        }
    )


def student_view_course_announcments_grades(request, course_id, student_id):
    course = get_object_or_404(Course, pk=course_id)
    student = Student.objects.get(pk=student_id)
    announcments = CourseAnnouncement.objects.filter(course__pk=course_id)
    return render(request, "course_details_for_student.html",
                  {
                      'course': course,
                      'announcments': announcments,
                      'student': student,
                  })


def list_students_grades_in_course(request, course_id):
    course_obj = get_object_or_404(Course, pk=course_id)
    gradecolumns = course_obj.gradecolumn_set.all()
    student = course_obj.students.all()
    grades = Grade.objects.filter(column__course=course_id)

    student_grade_value_list = []
    student_info_dict = {}
    student_grade_id_list = []
    student_grade_value_dict = {}
    student_grade_column_dict = {}
    big = []
    lists = []
    for s in student:
        student_info_dict = {}
        student_grade_column_list = []
        student_grade_value_list = []
        for gc in gradecolumns:
            student_grade_value_dict = {}
            student_grade_column_dict = {}
            student_grade_column_dict[gc.total] = gc.name
            for g in grades:
                if gc.pk == g.column.pk:
                    if s.pk == g.student.pk:
                        student_grade_value_dict[g.pk] = g.value
            if len(student_grade_value_dict) < len(student_grade_column_dict):
                student_grade_value_dict[gc.pk] = ''
            student_grade_column_list.append(student_grade_column_dict)
            student_grade_value_list.append(student_grade_value_dict)
        student_info_dict[s.university_id] = [student_grade_value_list, s.pk]
        big.append(student_info_dict)

    for grade in grades:
        lists.append(grade.pk)
        lists.append(grade.value)
        lists.append(grade.student.university_id)
        lists.append(grade.column.name)

    return render(
        request,
        'list_students_grades_in_course.html',
        {
            'course_id': course_id,
            'student_grade_column': student_grade_column_list,
            'student_grade_value': student_grade_id_list,
            's': big,
            'g': lists
        }
    )


class CourseAnnouncementEdit(UpdateView):
    model = CourseAnnouncement
    template_name = 'edit_course_announcments.html'
    context_object_name = 'course_announcement'
    fields = ('name', 'comment')
