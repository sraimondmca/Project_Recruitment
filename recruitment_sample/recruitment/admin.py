# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Job , Candidate

class JobsAdmin(admin.ModelAdmin):
    list_display = ('id','name','description',)
    search_fields = ('name',)
    fields = ('name','description')
    readonly_fields = ('id',)

class CandidateAdmin(admin.ModelAdmin):
    list_display    = ('full_name','location','work_status','work_experince','mobile_number','job_id')
    search_fields   = ('full_name',)
    fields          = ('full_name','location','work_status','work_experince','mobile_number','email_address','resume','job_id')
    readonly_fields = ('id',)
    

admin.site.register(Job, JobsAdmin)
admin.site.register(Candidate,CandidateAdmin)
