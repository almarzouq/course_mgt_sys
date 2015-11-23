from  django.shortcuts import  render ,  redirect
from  .models import  Student  #to import the Students Model
from  django.views.generic.edit import  CreateView ,  UpdateView
from  forms import  StudentEdit
# Create your views here.

class StudentRegister(CreateView):
    #to use the models variable
    model = Student
    #we require all fields since students will need register him/her self
    fields = '__all__'
    template_name = "Student_Profile_Create.html"
    #after succeding in the registery proccess the student will be redirected to this directery
    success_url = ("Home",)

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
