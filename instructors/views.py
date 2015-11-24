from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Instructor, Announcement


# Create your views here.
@login_required
def instructor_profile(request):
    qs = Instructor.objects.get(pk=request.user.pk)
    return render(
        request,
        'instructor_profile.html',
        {
            'instructor': qs,
        })


class AnnouncementView(DetailView):
    model = Announcement
    fields = '__all__'
    template_name = "announcement.html"
    context_object_name = "announcement"


class InstructorRegister(CreateView):
    model = Instructor
    fields = '__all__'
    template_name = 'instructor_create_profile.html'


class InstructorEditProfile(UpdateView):
    model = Instructor
    fields = ['phone', 'email', 'office_hours', 'twitter_id', ]
    template_name = 'instructor_profile_edit.html'
    context_object_name = "form"
