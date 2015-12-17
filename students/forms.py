from .models import Student
from django import forms


class StudentEditForm(forms.ModelForm):

    class Meta:
        model = Student
        exclude = ['name', 'university_id']


class SignupForm(forms.Form):

    # university_id = forms.CharField(required=False)
    # twitter_id = forms.CharField(required=False)

    def signup(self, request, user):
        Student.objects.create(
            user=user,
            name=user.username,
            email=user.email,
            university_id=self.cleaned_data.get('university_id'),
            twitter_id=self.cleaned_data.get('twitter_id')
        )
