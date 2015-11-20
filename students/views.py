from django.shortcuts import render
from .models import Student
from django.contrib.auth. decorators import login_required


@login_required
def student_profile(request):
	qs = Student.objects.get(pk=request.user.pk)
	return render(
		request,
		'student_profile.html',
		{
			'student':qs,
			
		})
