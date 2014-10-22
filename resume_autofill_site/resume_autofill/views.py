from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from resume_autofill.models import Resume, Skillset
from resume_autofill.forms import SkillsetForm, SkillInlineFormSet

def index(request):
    return HttpResponse("Hello, world. You're at the resume_autofill index.")

def view_resume(request):
    resume = Resume.objects.all()[0]
    context = {'resume': resume}
    return render(request, 'view_resume.html', context)

def view_resume_skillset(request):
    ''' Return a list of skillsets that have been added for this resume '''
    resume = request.user.resumes.all()[0]
    skillsets = resume.skillsets.all()

    vars = {'skillsets': skillsets}
    reqc = RequestContext(request, vars)

    return render_to_response("view_skillsets.html", reqc)

def add_resume_skillset(request):
    ''' Create and add a new skillset '''
    return HttpResponse("You're editing your resume.")
    
def edit_resume_skillset(request, skillset_id):
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
                return HttpResponseRedirect(reverse('view_resume_skillset'))

    # GET: Show form for existing skillset so user can submit updates
    else:
        form = SkillsetForm(instance=skillset)
        skill_inlineformset = SkillInlineFormSet(instance=skillset)

    vars = {'form': form, 'skill_inlineformset': skill_inlineformset}
    reqc = RequestContext(request, vars)

    return render_to_response("edit_skillset.html", reqc)

