from .models import Student
from django import forms

from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget 

class StudentEditForm(forms.ModelForm):

    class Meta:
        model = Student
        exclude = ['name', 'university_id']


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        exclude = ('name',)

    def signup(self, request, user):
        Student.objects.create(
            name=user,
            email=self.cleaned_data.get('email'),
            university_id=self.cleaned_data.get('university_id'),
            twitter_id=self.cleaned_data.get('twitter_id')
        )
class testFormBootstrap3(forms.Form):

    date_time = forms.DateTimeField(widget=DateTimeWidget(usel10n=True, bootstrap_version=3))
    date = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3))
    time = forms.TimeField(widget=TimeWidget(usel10n=True, bootstrap_version=3))
