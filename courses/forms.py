from django import forms
from django.forms.models import inlineformset_factory
from .models import Course, Grade


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

# InlineCourseFormSet = inlineformset_factory(
# Grade,
# Course,
# fields=('name',)
#
# )
