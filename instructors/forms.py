from datetimewidget.widgets import DateTimeWidget

from django import forms

from courses.models import GradeColumn

from .models import Instructor, Announcement, Appointment


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
        dateTimeOptions = {
            'format': 'dd/mm/yyyy HH:ii P',
            'autoclose': True,
            'showMeridian': True
        }
        widgets = {
            'approved': forms.HiddenInput,
            'sent_1st_reminder': forms.HiddenInput,
            'sent_2nd_reminder': forms.HiddenInput,
            'instructor': forms.HiddenInput,
            'date_time': DateTimeWidget(options=dateTimeOptions, usel10n = True, bootstrap_version=3)
        }

        widget = {
        'date_time' :  DateTimeWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3)
        }



class GradeColumnEditForm(forms.ModelForm):

    class Meta:
        model = GradeColumn
        fields = '__all__'
