from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView

from .models import Instructor, Appointment
from courses.models import Grade, GradeColumn
from .forms import GradeColumnEditForm

# Create your views here.


def instructor_view(request, pk=None):
    if pk:
        obj = get_object_or_404(Instructor, pk=pk)
    else:
        obj = get_object_or_404(Instructor, pk=request.user.pk)
    return render(
        request,
        'instructor_profile.html',
        {
            'instructor': obj,
            'announcements': obj.announcement_set.all(),
        })


class InstructorCreate(CreateView):
    model = Instructor
    fields = '__all__'
    template_name = 'instructor_create_profile.html'


class InstructorEditProfile(UpdateView):
    model = Instructor
    fields = ['phone', 'email', 'office_hours', 'twitter_id', ]
    template_name = 'instructor_profile_edit.html'
    context_object_name = "instructor"


class AppointmentView(CreateView):
    model = Appointment
    fields = ('name', 'date_time', 'reason', 'email', 'phone',)
    template_name = 'take_appointment.html'
    success_url = "/"


class GradesAdd(CreateView):
    model = Grade
    fields = '__all__'
    template_name = 'instructor_grading.html'


def gradecolumn_edit(request, gradecolumn_id):
    obj = GradeColumn.objects.get(pk=gradecolumn_id)
    if request.method == 'POST':
        form = GradeColumnEditForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('instructor_profile')
    else:
        form = GradeColumnEditForm(instance=obj)
    return render(request,
                  'instructor_gradecolumn_edit.html',
                  {
                      'gradecolumn': obj,
                      'form': form,
                  })
