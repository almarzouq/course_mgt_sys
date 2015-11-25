from  .models import  Student
from  django import  forms


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
