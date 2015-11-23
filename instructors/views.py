from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Instructor
# Create your views here.


class InstructorRegister(CreateView):
    model = Instructor
    fields = '__all__'
    template_name = 'instructor_create_profile.html'
