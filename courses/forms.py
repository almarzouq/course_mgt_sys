from django import forms
from .models import Course, CourseAnnouncement


class NewCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class CourseAnnouncmentForm(forms.ModelForm):
    class Meta:
        model = CourseAnnouncement
        fields = '__all__'
