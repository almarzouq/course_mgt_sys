from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy

from .models import Student
from .forms import  StudentEdit

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
    template_name = 'student_profile_create.html'
    # after succeding in the registery proccess the student will be redirected
    # to this directery
    success_url = reverse_lazy('student_profile')


@login_required
def edit_profile(request):
    obj = request.user
    if request.method == 'POST':
        form = StudentEditForm(request.POST, instance=obj)
        if form.is_valid():

            form.save()

            return redirect('home')
    else:
        form = StudentEditForm(instance=obj)

        return render(request, 'student_profile_edit.html', {'student': obj, 'form': form, })
