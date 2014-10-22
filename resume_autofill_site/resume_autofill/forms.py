from django import forms
from django.forms.models import inlineformset_factory

from resume_autofill.models import Skillset, Skill, Job, Accomplishment

SkillInlineFormSet = inlineformset_factory(Skillset, Skill, can_delete=True)
AccomplishmentInlineFormSet = inlineformset_factory(Job, Accomplishment, can_delete=True)

class SkillsetForm(forms.ModelForm):
    class Meta:
        model = Skillset
        exclude = ('resume',)


class AccomplishmentsetForm(forms.ModelForm):
    class Meta:
        model = Accomplishment
        exclude = ('job',)
