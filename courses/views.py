from django.shortcuts import render
from .forms import NewCourseForm
# Create your views here.

def course_create (request):
    if request.method== 'POST':
        form = NewCourseForm(request.POST)
        if form.is_valid():
            new_course = form.save(commit=False)
    else:
        form = NewCourseForm()
    return render(request,
    )
