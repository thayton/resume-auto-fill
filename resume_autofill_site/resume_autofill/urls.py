from django.conf.urls import patterns, url

from resume_autofill import views

urlpatterns = patterns('',
    url(r'^$',             views.index,       name='index'),
    url(r'^resume/view/$', views.view_resume, name='view_resume'),

    url(r'^resume/skillset/$', views.view_resume_skillset, name='view_resume_skillset'),
    url(r'^resume/skillset/(?P<skillset_id>\d+)/$', views.edit_resume_skillset, name='edit_resume_skillset'),
    url(r'^resume/skillset/add/$', views.add_resume_skillset, name='add_resume_skillset'),

    url(r'^resume/education/$', views.view_resume_education, name='view_resume_education'),
    url(r'^resume/education/(?P<education_id>\d+)/$', views.edit_resume_education, name='edit_resume_education'),
    url(r'^resume/education/add/$', views.add_resume_education, name='add_resume_education'),

    url(r'^resume/job/$', views.view_resume_job, name='view_resume_job'),
    url(r'^resume/job/(?P<job_id>\d+)/$', views.edit_resume_job, name='edit_resume_job'),
    url(r'^resume/job/add/$', views.add_resume_job, name='add_resume_job'),
)
