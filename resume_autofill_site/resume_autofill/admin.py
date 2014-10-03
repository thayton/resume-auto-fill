from django.contrib import admin
from resume_autofill.models import Resume, Education, Job, Accomplishment, SkillUsed

class AccomplishmentInline(admin.StackedInline):
    model = Accomplishment
    extra = 1

class SkillUsedInline(admin.StackedInline):
    model = SkillUsed
    extra = 1

class JobAdmin(admin.ModelAdmin):
    inlines = [AccomplishmentInline, SkillUsedInline]

# Register your models here.
admin.site.register(Resume)
admin.site.register(Education)
admin.site.register(Job, JobAdmin)
