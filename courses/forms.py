from django import forms
from django.forms.models import inlineformset_factory
from .models import Course, Grade, CourseAnnouncement


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

class CourseAnnouncmentForm(forms.ModelForm):
    class Meta:
        model = CourseAnnouncement
        fields = '__all__'
        widgets = {
            'course' : forms.HiddenInput,
        }
