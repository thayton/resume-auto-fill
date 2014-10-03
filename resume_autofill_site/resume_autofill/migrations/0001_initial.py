# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Accomplishment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField()),
                ('order', models.IntegerField()),
            ],
            options={
                'ordering': ['order'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('school_url', models.URLField(verbose_name=b'School URL')),
                ('degree', models.CharField(max_length=250)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('summary', models.TextField()),
                ('is_current', models.BooleanField(default=False)),
                ('gpa', models.DecimalField(max_digits=3, decimal_places=2)),
            ],
            options={
                'ordering': ['-end_date', '-start_date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.CharField(max_length=250)),
                ('company_url', models.URLField(verbose_name=b'Company URL')),
                ('location', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('is_current', models.BooleanField(default=False)),
                ('is_public', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-end_date', '-start_date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('professional_summary', models.TextField()),
                ('location', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ['id'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skillset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SkillUsed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('job', models.ForeignKey(to='resume_autofill.Job')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': 'skills used',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='skill',
            name='skillset',
            field=models.ForeignKey(to='resume_autofill.Skillset'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resume',
            name='skillset',
            field=models.ForeignKey(to='resume_autofill.Skillset'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resume',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='education',
            name='resume',
            field=models.ForeignKey(to='resume_autofill.Resume'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accomplishment',
            name='job',
            field=models.ForeignKey(to='resume_autofill.Job'),
            preserve_default=True,
        ),
    ]
