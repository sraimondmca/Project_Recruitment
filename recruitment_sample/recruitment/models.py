# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

def photo_directory_path_candidate(instance, filename):
    # file will be uploaded to MEDIA_ROOT/api_abhyasi/id_photoseq.jpg
    return 'candidate/{0}.jpg'.format(instance.id)

class Job(models.Model):

    name                      = models.CharField(max_length=128,)
    description               = models.TextField(null=True, blank=True)

class Candidate(models.Model):
    
    WORK_STATUS_CHOICES = (  
            ('fresher','Fresher'),
            ('experienced','Experienced'),
            )
    
    full_name       = models.CharField(max_length=128,)
    location        = models.CharField(max_length=128,)
    work_status     = models.CharField(max_length=128,choices=WORK_STATUS_CHOICES,)
    work_experince  = models.FloatField()
    mobile_number   = models.CharField(max_length=128,)
    email_address   = models.CharField(max_length=128,)
    resume          = models.FileField(upload_to=photo_directory_path_candidate)
    job_id          = models.ForeignKey('recruitment.job', null=True, blank=True)
