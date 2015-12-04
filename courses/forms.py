from django import forms
from .models import Course, Grade, GradeColumn


class NewCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class GradeForm(forms.ModelForm):

    class Meta:
        model = Grade
        fields = '__all__'


class GradeColumnEditForm(forms.ModelForm):
    class Meta:
        model = GradeColumn
        fields = '__all__'
        widgets = {
            'course': forms.HiddenInput,
        }
