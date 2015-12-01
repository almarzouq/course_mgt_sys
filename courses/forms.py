from django import forms
from .models import Course, Grade


class NewCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class GradeForm(forms.ModelForm):

    class Meta:
        model = Grade
        fields = '__all__'
