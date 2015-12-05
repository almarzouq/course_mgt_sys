from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView


from .models import Instructor, Appointment
from courses.models import Grade, GradeColumn
from .forms import GradeColumnEditForm, AppointmentForm, AnnouncementForm

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


def appointment_create(request, pk):
    inst = get_object_or_404(Instructor, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=inst)
        if form.is_valid():

            form.save()

            return redirect('appointment_list')
    else:
        form = AppointmentForm(instance=inst)

    return render(
        request,
        'take_appointment.html',
        {
            'instructor': inst,
            'form': form
        })


def intructor_student_can_view_appoinment_detail(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)

    return render(request,
                  'appointment_details.html',
                  {
                      'appointment': appointment,
                  })


class AppointmentList(ListView):
    model = Appointment
    template_name = "appointment_list.html"
    context_object_name = "appointments"

def create_general_announcment(request, instructor_id):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AnnouncementForm(initial={'instructor': instructor_id, })
    return render(
        request,
        'create_general_announcment.html',
        {
            'form': form,
            'instructor_id': instructor_id,
        })
