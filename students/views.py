from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from django.db.models import Q
from django.views.generic import ListView

from .forms import StudentEditForm , testFormBootstrap3
from .models import Student


def student_profile(request, pk):
    qs = Student.objects.get(pk=pk)
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


def edit_profile(request, pk):
    obj = Student.objects.get(pk=pk)
    if request.method == 'POST':
        form = StudentEditForm(request.POST, instance=obj)
        if form.is_valid():

            form.save()

# changed functionality to switch to the students list instead of view
# that students own profile

            return redirect('students_list')
    else:
        form = StudentEditForm(instance=obj)
    return render(request,
                  'student_profile_edit.html',
                  {
                      'student': obj,
                      'form': form,
                  })


def students_list(request):
    obj = Student.objects.all()
    return render(request, 'student_list.html', {'students': obj})


def student_search(request, search_text):
    qs = Student.objects.filter(
        Q(name__icontains=search_text) | Q(university_id__icontains=search_text))
    return render(request, 'student_list.html', {'students': qs})



class StudentListUni(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'
    queryset = Student.objects.order_by('university_id')


class StudentListName(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'
    queryset = Student.objects.order_by('name')



def dateTimeViewBootstrap3(request):

    if request.method == 'POST': # If the form has been submitted...

        form = testFormBootstrap3(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass

            form = testFormBootstrap3()
            return render(request, 'home.html', {

                'form': form,'bootstrap':3,
            })
    else:
        if request.GET.get('id',None):
            form = testFormBootstrap3(instance=testFormBootstrap3.objects.get(id=request.GET.get('id',None)))
        else:
            form = testFormBootstrap3()

    return render(request, 'home.html', {
             'form': form,'bootstrap':3
            })
