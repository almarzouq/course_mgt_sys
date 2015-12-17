from django import forms
from django.forms.models import inlineformset_factory
from .models import Course, Grade, CourseAnnouncement, GradeColumn, Attendance, Lecture


class NewCourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = '__all__'


class GradeForm(forms.ModelForm):

    class Meta:
        model = Grade
        fields = '__all__'
        widgets = {
            'column': forms.HiddenInput,
            'student': forms.HiddenInput,
        }


class CourseAnnouncmentForm(forms.ModelForm):

    class Meta:
        model = CourseAnnouncement
        fields = '__all__'
        widgets = {
            'course': forms.HiddenInput,
        }


class GradeColumnEditForm(forms.ModelForm):

    class Meta:
        model = GradeColumn
        fields = '__all__'
        widgets = {
            'course': forms.HiddenInput,
        }


class GradeColumnCreateForm(forms.ModelForm):

    class Meta:
        model = GradeColumn
        fields = '__all__'
        widgets = {
            'course': forms.HiddenInput,
        }


class GradeColumnCreateForm(forms.ModelForm):
    class Meta:
        model = GradeColumn
        fields = '__all__'
        widgets = {
            'course': forms.HiddenInput,
        }


class AttendanceStudentForm(forms.ModelForm):

    class Meta:
        model = Attendance
        fields = '__all__'
        widgets = {

            'student': forms.HiddenInput,
            'lecture' : forms.HiddenInput,

        }


class InstructorLectureForm(forms.ModelForm):

    class Meta:
        model = Lecture
        fields = '__all__'
