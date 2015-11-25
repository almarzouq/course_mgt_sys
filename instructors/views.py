from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView

from .models import Instructor


# Create your views here.

def instructor_profile(request, pk=None):
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


class InstructorRegister(CreateView):
    model = Instructor
    fields = '__all__'
    template_name = 'instructor_create_profile.html'


class InstructorEditProfile(UpdateView):
    model = Instructor
    fields = ['phone', 'email', 'office_hours', 'twitter_id', ]
    template_name = 'instructor_profile_edit.html'
    context_object_name = "form"
