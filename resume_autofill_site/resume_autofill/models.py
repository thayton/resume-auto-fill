import time

from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
    user = models.ForeignKey(User, related_name='resumes')
    professional_summary = models.TextField()
    location = models.CharField(max_length=250)

    def __unicode__(self):
        return self.user.username

class Skillset(models.Model):
    resume = models.ForeignKey(Resume, related_name='skillsets')
    name = models.CharField(max_length=250) # Operating Systems, Languages, SCM

    def __unicode__(self):
        return self.name

class Skill(models.Model):
    skillset = models.ForeignKey(Skillset, related_name='skills')
    name =  models.CharField(max_length=250) # C++, Python, Java
    
    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return ''.join([self.skillset.name, '-', self.name])

# XXX Change model name to School
class Education(models.Model):
    DEGREE_CHOICES = (
        ('NA', 'N/A'), 
        ('AS','Associates'),
        ('BA','Bachelors'),
        ('MA','Masters'),
        ('DO','Doctorate'),
        ('JD','JD'),
        ('MD','MD'),
        ('OT','Other'),
    )

    resume = models.ForeignKey(Resume, related_name='education')

    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    school_url = models.URLField('School URL')

    # graduated = models.BooleanField(default=False)
    # major= models.CharField(max_length=250)
    degree = models.CharField(max_length=250, choices=DEGREE_CHOICES) 

    start_date = models.DateField()
    end_date = models.DateField()

    summary = models.TextField(blank=True)
    is_current = models.BooleanField(default=False)

    gpa = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)

    class Meta:
        ordering = ['-end_date','-start_date']
        verbose_name_plural = "Education"

    def edu_date_range(self):
        return ''.join(['(', self.formatted_start_date(), 
            '-', self.formatted_end_date(), ')'])

    def full_start_date(self):
        return self.start_date.strftime("%Y-%m-%d")

    def full_end_date(self):
        if (self.is_current == True):
            return time.strftime("%Y-%m-%d", time.localtime())
        else:
            return self.end_date.strftime("%Y-%m-%d")

    def formatted_start_date(self):
        return self.start_date.strftime("%b %Y")

    def formatted_end_date(self):
        if (self.is_current == True):
            return "Current"
        else:
            return self.end_date.strftime("%b %Y")

    def __unicode__(self):
        return ' '.join([self.name, self.edu_date_range()])

class Job(models.Model):
    resume = models.ForeignKey(Resume, related_name='jobs')

    company = models.CharField(max_length=250)
    company_url = models.URLField('Company URL')

    location = models.CharField(max_length=250)
    title = models.CharField(max_length=250)

    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()

    is_current = models.BooleanField(default=False)
    is_public = models.BooleanField(default=True)

    class Meta:
        ordering = ['-end_date','-start_date']
        
    def job_date_range(self):
        return ''.join(['(', self.formatted_start_date(),'-', 
            self.formatted_end_date(), ')'])
    
    def full_start_date(self):
        return self.start_date.strftime("%Y-%m-%d")

    def full_end_date(self):
        if (self.is_current == True):
            return time.strftime("%Y-%m-%d", time.localtime())
        else:
            return self.end_date.strftime("%Y-%m-%d")

    def formatted_start_date(self):
        return self.start_date.strftime("%b %Y")
        
    def formatted_end_date(self):
        if (self.is_current == True):
            return "Current"
        else:
            return self.end_date.strftime("%b %Y")

    def __unicode__(self):
        return ' '.join([self.company, self.job_date_range()])

class Accomplishment(models.Model):
    job = models.ForeignKey(Job, related_name='accomplishments')
    description = models.TextField()

    order = models.IntegerField()

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return ''.join([self.job.company, '-', self.description[0:50], '...'])

class SkillUsed(models.Model):
    job = models.ForeignKey(Job, related_name='skills_used')
    name =  models.CharField(max_length=250) # C++, Python, Java
    
    class Meta:
        verbose_name_plural = "skills used"
        ordering = ['id']

    def __unicode__(self):
        return self.name

