from django.contrib import admin
from resume_autofill.models import Resume, Education, Job, Accomplishment, SkillUsed, Skillset, Skill

class AccomplishmentInline(admin.StackedInline):
    model = Accomplishment
    extra = 1

class SkillUsedInline(admin.StackedInline):
    model = SkillUsed
    extra = 1

class SkillInline(admin.StackedInline):
    model = Skill

class SkillsetAdmin(admin.ModelAdmin):
    inlines = [SkillInline]

class JobAdmin(admin.ModelAdmin):
    inlines = [AccomplishmentInline, SkillUsedInline]

# Register your models here.
admin.site.register(Resume)
admin.site.register(Education)
admin.site.register(Skillset, SkillsetAdmin)
admin.site.register(Job, JobAdmin)
