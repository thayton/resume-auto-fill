from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from resume_autofill.models import Resume, Skillset, Job, Education
from resume_autofill.forms import SkillsetForm, SkillInlineFormSet, JobForm, AccomplishmentInlineFormSet, EducationForm

def index(request):
    return HttpResponse("Hello, world. You're at the resume_autofill index.")

def view_resume(request):
    resume = Resume.objects.all()[0]
    context = {'resume': resume}
    return render(request, 'view_resume.html', context)

def edit_resume(request):
    resume = Resume.objects.all()[0]
    context = {'resume': resume}
    return render(request, 'edit_resume.html', context)

#----------------------------------------
def view_skillsets(request):
    ''' Return a list of skillsets that have been added for this resume '''
    resume = request.user.resumes.all()[0]
    skillsets = resume.skillsets.all()

    vars = {'skillsets': skillsets}
    reqc = RequestContext(request, vars)

    return render_to_response("view_skillsets.html", reqc)

def add_skillset(request):
    ''' Create and add a new skillset '''
    if request.POST:
        form = SkillsetForm(request.POST)
        resume = request.user.resumes.all()[0]

        if form.is_valid():
            skillset = form.save(commit=False) # Why commit=False?
            skillset.resume = resume

            skill_inlineformset = SkillInlineFormSet(request.POST, instance=skillset)

            if skill_inlineformset.is_valid():
                skillset.save()
                skill_inlineformset.save()                
                return HttpResponseRedirect(reverse('view_skillsets'))

    # GET: Show form for existing skillset so user can submit updates
    else:
        form = SkillsetForm()
        skill_inlineformset = SkillInlineFormSet(instance=Skillset())

    vars = {'form': form, 'skill_inlineformset': skill_inlineformset}
    reqc = RequestContext(request, vars)

    return render_to_response("add_skillset.html", reqc)
    
def edit_skillset(request, skillset_id):
    ''' Change an existing skillset '''

    # Get the skillset associated with id
    skillset = get_object_or_404(Skillset, pk=skillset_id)

    # POST: User has submitted updates to change skillset
    if request.POST:
        form = SkillsetForm(request.POST, instance=skillset)

        if form.is_valid():
            form.save(commit=False) # Why commit=False?
            skill_inlineformset = SkillInlineFormSet(request.POST, instance=skillset)

            if skill_inlineformset.is_valid():
                skillset.save()
                skill_inlineformset.save()                
                return HttpResponseRedirect(reverse('view_skillsets'))

    # GET: Show form for existing skillset so user can submit updates
    else:
        form = SkillsetForm(instance=skillset)
        skill_inlineformset = SkillInlineFormSet(instance=skillset)

    vars = {'form': form, 'skill_inlineformset': skill_inlineformset}
    reqc = RequestContext(request, vars)

    return render_to_response("edit_skillset.html", reqc)

#----------------------------------------
def view_jobs(request):
    ''' Return a list of jobs that have been added for this resume '''
    resume = request.user.resumes.all()[0]
    jobs = resume.jobs.all()

    vars = {'jobs': jobs}
    reqc = RequestContext(request, vars)

    return render_to_response("view_jobs.html", reqc)

def add_job(request):
    ''' Create and add a new job '''
    return HttpResponse("You're editing your resume.")
    
def edit_job(request, job_id):
    ''' Change an existing job '''

    # Get the job associated with id
    job = get_object_or_404(Job, pk=job_id)

    # POST: User has submitted updates to change job
    if request.POST:
        form = JobForm(request.POST, instance=job)

        if form.is_valid():
            form.save(commit=False) # Why commit=False?
            accomplishment_inlineformset = AccomplishmentInlineFormSet(request.POST, instance=job)

            if accomplishment_inlineformset.is_valid():
                job.save()
                accomplishment_inlineformset.save()                
                return HttpResponseRedirect(reverse('view_jobs'))

    # GET: Show form for existing job so user can submit updates
    else:
        form = JobForm(instance=job)
        accomplishment_inlineformset = AccomplishmentInlineFormSet(instance=job)

    vars = {'form': form, 'accomplishment_inlineformset': accomplishment_inlineformset}
    reqc = RequestContext(request, vars)

    return render_to_response("edit_job.html", reqc)

#----------------------------------------
def view_education(request):
    ''' Return a list of jobs that have been added for this resume '''
    resume = request.user.resumes.all()[0]
    education = resume.education.all()

    vars = {'education': education}
    reqc = RequestContext(request, vars)

    return render_to_response("view_education.html", reqc)

def add_education(request):
    ''' Create and add a new education '''
    return HttpResponse("You're editing your resume.")
    
def edit_education(request, education_id):
    ''' Change an existing education '''

    # Get the education associated with id
    education = get_object_or_404(Education, pk=education_id)

    # POST: User has submitted updates to change education
    if request.POST:
        form = EducationForm(request.POST, instance=education)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('view_educations'))

    # GET: Show form for existing education so user can submit updates
    else:
        form = EducationForm(instance=education)

    vars = {'form': form}
    reqc = RequestContext(request, vars)

    return render_to_response("edit_education.html", reqc)

