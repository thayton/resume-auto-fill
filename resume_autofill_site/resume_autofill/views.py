from django.shortcuts import render
from django.http import HttpResponse
from resume_autofill.models import Resume

def index(request):
    return HttpResponse("Hello, world. You're at the resume_autofill index.")

def view_resume(request):
    resume = Resume.objects.all()[0]
    context = {'resume': resume}
    return render(request, 'view_resume.html', context)

def edit_resume(request):
    return HttpResponse("You're editing your resume.")
    
