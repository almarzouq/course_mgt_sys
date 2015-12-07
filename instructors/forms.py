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
        widgets = {
            'instructor': forms.HiddenInput,
        }


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            'approved': forms.HiddenInput,
            'sent_1st_reminder': forms.HiddenInput,
            'sent_2nd_reminder': forms.HiddenInput,
            'instructor': forms.HiddenInput,
            }


class GradeColumnEditForm(forms.ModelForm):
    class Meta:
        model = GradeColumn
        fields = '__all__'
