from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
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

from instructors.models import Instructor, Announcement

from courses.models import (Course, CourseAnnouncement, Grade,
                            GradeColumn, Lecture, Attendance,
                            CourseStudent)

from .forms import (NewCourseForm, EditCourseForm, GradeForm,
                    GradeColumnEditForm, CourseAnnouncmentForm,
                    GradeColumnCreateForm, AttendanceStudentForm, InstructorLectureForm)

from .models import GradeColumn
# Create your views here.


@login_required
def course_create(request):
    if not request.user.is_instructor():
        raise Http404
    if request.method == 'POST':
        form = NewCourseForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect(obj)
    else:

        form = NewCourseForm(initial={'instructor': request.user.instructor.pk,
                                      'students': None, })

    return render(
        request,
        'course_create.html',
        {
            "form": form,
        }
    )


@login_required
def list_course_grade_column(request, course_id):
    if not request.user.is_instructor():
        raise Http404
    course_obj = get_object_or_404(Course, pk=course_id)
    qs = course_obj.gradecolumn_set.all()

    return render(request, "course_gradecolumn_list.html",
                  {
                      'course': course_obj,
                      'gradecolumns': qs,
                  }
                  )

@login_required
def view_course_gradecolumn(request, course_id, gradecolumn_id):
    if not request.user.is_instructor():
        raise Http404
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

@login_required
def gradecolumn_edit(request, gradecolumn_id, course_id):
    if not request.user.is_instructor():
        raise Http404
    course = get_object_or_404(Course, pk=course_id)
    gc = course.gradecolumn_set.get(pk=gradecolumn_id)
    if request.method == 'POST':
        form = GradeColumnEditForm(request.POST, instance=gc)
        if form.is_valid():
            form.save()
            messages.success(request, 'GradeColumn is successfully edited.')
        return redirect(reverse('view_course_gradecolumn', kwargs={
            'course_id': course_id, 'gradecolumn_id': gradecolumn_id}))
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

@login_required
def student_join_course(request, course_id):
    ''' this is used for a student to add himself to a course '''
    if request.user.is_instructor():
        # only student accounts
        raise Http404

    course = Course.objects.get(pk=course_id)
    # use current user student profile
    student = request.user.student
    if course.student_registration_open:
        try:
            # When using through models
            # This is how you add a relation
            # The through model is CourseStudent
            CourseStudent.objects.create(
                course=course,
                student=student)

            # this is how you add a relation
            # when you dont have a through model
            #course.students.add(student)
        except:
            # will through exception if duplicate
            messages.error(request, 'You are already enrolled in this course')
        else:
            messages.success(request, 'You are enrolled in %s' % (course))
    else:
        messages.error(
            request, 'You are not allowed to enroll in this course talk to your instructor')
    return redirect(reverse('student_view_course_announcments', args=[course_id]))


@login_required
def instructor_add_student_to_course(request, course_id, student_id):
    ''' This is used by instructor to add student to course '''
    if not request.user.is_instructor():
        raise Http404
    course = Course.objects.get(pk=course_id)
    student = Student.objects.get(pk=student_id)
    try:
        # When using through models
        # This is how you add a relation
        # The through model is CourseStudent
        CourseStudent.objects.create(
            course=course,
            student=student)

        # this is how you add a relation
        # when you dont have a through model
        #course.students.add(student)
        # no need to save when using add
        # because student record already exists
    except:
        # will through exception if duplicate
        messages.error(request, 'The student is already enrolled')
    else:
        messages.success(request, 'The student is successfuly added.')
    return redirect(reverse('instructor_view_course_stundets_announcments', args=[course_id]))


@login_required
def post_student_grade(request, course_id, student_id, gradecolumn_id):
    if not request.user.is_instructor():
        raise Http404
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Grade was successfully posted.')
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


@login_required
def edit_student_grade(request, course_id, student_id, gradecolumn_id, grade_id):
    if not request.user.is_instructor():
        raise Http404
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

@login_required
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

@login_required
def list_student_grade(request, course_id, student_id):
    course_obj = get_object_or_404(Course, pk=course_id)
    gradecolumns = course_obj.gradecolumn_set.all().order_by("id")
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



@login_required
def delete_student_grade(request, course_id, student_id, gradecolumn_id, grade_id):
    if not request.user.is_instructor():
        raise Http404
    grade = get_object_or_404(Grade, pk=grade_id)
    grade.delete()
    messages.success(request, 'Grade was successfully deleteded.')
    return redirect(reverse('list_student_grade', args=(course_id, student_id,)))


@login_required
def instructor_view_course_stundets_announcments(request, course_id):
    if not request.user.is_instructor():
        raise Http404
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


@login_required
def remove_student_from_course(request, course_id, student_id):
    if not request.user.is_instructor():
        raise Http404
    course = Course.objects.get(pk=course_id)
    student = Student.objects.get(pk=student_id)
    course.students.remove(student)
    course.save()
    messages.success(request, 'The student is successfuly removed.')
    return redirect(reverse('instructor_view_course_stundets_announcments', args=[course_id]))


@login_required
def create_course_announcment(request, course_id):
    if not request.user.is_instructor():
        raise Http404
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
    form_class = EditCourseForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_instructor():
            raise Http404
        else:
            return super(CourseEdit, self).dispatch(*args, **kwargs)

@login_required
def list_of_courses_to_add(request):
    if not request.user.is_instructor():
        qs = Course.objects.filter(student_registration_open=True)
        html = 'course_list_to_add.html'

    else:
        qs = Course.objects.all()
        html = 'course_list.html'
    return render(
        request,
        html,
        {
            'courses': qs,
        }
    )


@login_required
def my_list_of_courses(request):
    if not request.user.is_instructor():
        qs = Course.objects.filter(students=request.user.student)

    else:
        qs = Course.objects.filter(instructor=request.user.instructor)
    return render(
        request,
        'course_list.html',
        {
            'courses': qs,
        }
    )


def student_attendance(request, course_id, lecture_id):
    obj = Lecture.objects.get(pk=lecture_id)
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist as e:
        raise Http404
    try:
        Attendance.objects.create(
            lecture=obj, student=student, attended=True)
    except:
        messages.error(
            request,
            'You have already checked in'.format(student.name))
    else:
        messages.success(
            request,
            'the student {} have successfully checked in'.format(student.name))
    return redirect(reverse('lecture_details', kwargs={'course_id': course_id, 'lecture_id': lecture_id, }))


def instructor_lecture(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = InstructorLectureForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect(reverse('lecture_details', kwargs={'course_id': course_id, 'lecture_id': obj.pk}))
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
    return render(request, 'lecture_details.html', {'lecture': obj, 'attended': qs2, 'course': qs, 'lecture_id': lecture_id, 'course_id': course_id, })


def lectures_list(request, course_id):
    obj = Course.objects.get(pk=course_id)
    qs = Lecture.objects.filter(course=obj)
    return render(request, 'lecture_list.html', {'lectures': qs, 'course': obj, 'course_id': course_id})


@login_required
def gradecolumn_delete(request, course_id, gradecolumn_id):
    if not request.user.is_instructor():
        raise Http404
    course = get_object_or_404(Course, pk=course_id)
    qs = course.gradecolumn_set.get(pk=gradecolumn_id)
    qs.delete()
    messages.success(request, 'Grade Column was successfully deleted.')
    return redirect(reverse('list_course_grade_column', kwargs={
        'course_id': course.pk,
    }))


@login_required
def gradecolumn_create(request, course_id):
    if not request.user.is_instructor():
        raise Http404
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
    lecture = Lecture.objects.filter(course__pk=course_id)
    return render(request, "course_details_for_student.html",
                  {
                      'course': course,
                      'announcments': announcments,
                      'student': student,
                      'lectures' : lecture,
                  })

@login_required
def list_students_grades_in_course(request, course_id):
    if not request.user.is_instructor():
        raise Http404

    course_obj = get_object_or_404(Course, pk=course_id)
    gradecolumns = course_obj.gradecolumn_set.all().order_by("id")
    student = course_obj.students.all()
    grades = Grade.objects.filter(column__course=course_id)

    student_grade_column_list = []
    student_grade_value_list = []
    student_info_dict = {}
    student_grade_id_list = []
    student_grade_value_dict = {}
    student_grade_column_dict = {}
    big = []
    lists = []
    if not student:
        for gc in gradecolumns:
            student_grade_value_dict = {}
            student_grade_column_dict = {}
            student_grade_column_dict[gc.total] = gc.name
            student_grade_column_list.append(student_grade_column_dict)
    else:

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
            student_info_dict[s.university_id] = [
                student_grade_value_list, s.pk]
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
            'g': lists,
            'ss': student
        }
    )


class CourseAnnouncementEdit(UpdateView):
    model = CourseAnnouncement
    template_name = 'edit_course_announcments.html'
    context_object_name = 'course_announcement'
    fields = ('name', 'comment')


def student_view_course_announcments(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    announcments = CourseAnnouncement.objects.filter(course__pk=course_id)
    students = Student.objects.filter(course__pk=course_id)
    return render(
        request,
        "course_details_announcments.html",
        {
            'course': course,
            'students': students,
            'announcments': announcments
        })


def course_list(request):
    obj = Course.objects.all()
    return render(request, 'course_list_to_add.html', {'courses': obj})

def list_of_announcements(request):
    if request.user.is_anonymous():
        course_announcements = None
        instructor_announcements = None
        in_anno_massage = ''
        c_anno_massage = ''
    elif not request.user.is_instructor():
        course_announcements = CourseAnnouncement.objects.filter(
            course__students=request.user.student)
        c_anno_massage = 'No announcments in your courses'
        instructor_announcements = Announcement.objects.filter(
            instructor__course__students=request.user.student)
        in_anno_massage = 'your instructors didnt post any announcement yet'
    else:
        course_announcements = CourseAnnouncement.objects.filter(
            course__instructor=request.user.instructor)
        c_anno_massage = 'No announcments in your courses'
        instructor_announcements = Announcement.objects.filter(
            instructor=request.user.instructor)
        in_anno_massage = 'you didnt post any announcement yet'
    return render(request, 'index.html', {'course_announcements': course_announcements,
                                          'instructor_announcements': instructor_announcements,
                                          'c_anno_massage': c_anno_massage,
                                          'in_anno_massage': in_anno_massage},)
