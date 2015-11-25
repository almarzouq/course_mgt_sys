from .models import Instructor
from django import forms


class InstructorForm(forms.ModelForm):

    class Meta:
        model = Instructor
        fields = '__all__'
