from django import forms

from .models import Instructor, Announcement, Appointment


class InstructorForm(forms.ModelForm):

    class Meta:
        model = Instructor
        fields = '__all__'


class AnnouncementForm(forms.ModelForm):

    class Meta:
        model = Announcement
        fields = '__all__'


class AppointmentForm(form.ModelForm):

    class Meta:
        model = Appointment
        fields = '__all__'
