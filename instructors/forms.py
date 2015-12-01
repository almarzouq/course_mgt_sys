from django import forms

from .models import Instructor, Announcement, Appointment
from courses.models import GradeColumn


class InstructorForm(forms.ModelForm):

    class Meta:
        model = Instructor
        fields = '__all__'


class AnnouncementForm(forms.ModelForm):

    class Meta:
        model = Announcement
        fields = '__all__'


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = '__all__'


class GradeColumnEditForm(forms.ModelForm):
    class Meta:
        model = GradeColumn
        fields = '__all__'
