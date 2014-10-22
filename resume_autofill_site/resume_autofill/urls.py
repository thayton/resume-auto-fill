from django.conf.urls import patterns, url

from resume_autofill import views

urlpatterns = patterns('',
    url(r'^$',             views.index,       name='index'),
    url(r'^resume/view/$', views.view_resume, name='view_resume'),

    url(r'^resume/skillset/$', views.view_skillsets, name='view_skillsets'),
    url(r'^resume/skillset/(?P<skillset_id>\d+)/$', views.edit_skillset, name='edit_skillset'),
    url(r'^resume/skillset/add/$', views.add_skillset, name='add_skillset'),

    url(r'^resume/education/$', views.view_education, name='view_education'),
    url(r'^resume/education/(?P<education_id>\d+)/$', views.edit_education, name='edit_education'),
    url(r'^resume/education/add/$', views.add_education, name='add_education'),

    url(r'^resume/job/$', views.view_jobs, name='view_job'),
    url(r'^resume/job/(?P<job_id>\d+)/$', views.edit_job, name='edit_job'),
    url(r'^resume/job/add/$', views.add_job, name='add_job'),
)
