from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import NewCourseForm
from .models import GradeColumn

# Create your views here.


def course_create(request):
    if request.method == 'POST':
        form = NewCourseForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            return redirect()
    else:
        form = NewCourseForm()
    return render(
        request,
        'course_create.html',
        {
            "form": form,
        }
    )


class CourseGradeView(ListView):
    model = GradeColumn
    template_name = "course_grade.html"
