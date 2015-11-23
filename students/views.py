from django.shortcuts import render
from django.contrib.auth. decorators import login_required
from django.views.generic.edit import CreateView
from .models import Student


@login_required
def student_profile(request):
    qs = Student.objects.get(pk=request.user.pk)
    return render(
        request,
        'student_profile.html',
        {
            'student': qs,

        })


class StudentRegister(CreateView):
    # to use the models variable
    model = Student
    # we require all fields since students will need register him/her self
    fields = '__all__'
    template_name = "Student_Profile_Create.html"
    # after succeding in the registery proccess the student will be redirected
    # to this directery
    success_url = ("Home",)
