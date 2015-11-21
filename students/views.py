from django.shortcuts import render , redirect
from .models import Student  #to import the Students Model
from django.views.generic.edit import CreateView , UpdateView
from forms import StudentEdit
# Create your views here.


def edit_profile(request):
    obj = request.user
    if request.method == 'POST':
        form = StudentEdit(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('Home')
    else:
        form = StudentEdit(instance=obj)

        return render(request, 'Student_Profile_Edit.html', {'profile': obj, 'form': form, })
