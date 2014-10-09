from django.conf.urls import patterns, url

from resume_autofill import views

urlpatterns = patterns('',
    url(r'^$',             views.index,       name='index'),
    url(r'^resume/$',      views.view_resume, name='view_resume'),
    url(r'^resume/edit/$', views.edit_resume, name='edit_resume'),
)
