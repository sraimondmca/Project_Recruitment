# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.edit import CreateView
from .models import Candidate, Job
from .forms import JobApplyForm
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http import JsonResponse

class JobApplyView(CreateView):
    model = Candidate
    template_name = "apply_jobs.html"
    form_class = JobApplyForm
    
    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        print request.session.get('job_id')
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        valid = form.is_valid()
        if valid:
            full_name = form.cleaned_data['full_name']
            location   = form.cleaned_data['location'] 
            work_status = form.cleaned_data['work_status']
            work_experince   = form.cleaned_data['work_experince'] 
            mobile_number = form.cleaned_data['mobile_number']
            email_address   = form.cleaned_data['email_address']
            resume = form.cleaned_data['resume']
            job_id   = Job.objects.get(id = request.session.get('job_id') ) 
            itemObj = Candidate(full_name=full_name,location=location,work_status=work_status,work_experince=work_experince,
                                mobile_number=mobile_number,email_address=email_address,resume=resume,job_id=job_id)
            itemObj.save()
            
            return HttpResponseRedirect(reverse("recruitment:success"))
        else:
            return HttpResponseRedirect(reverse("recruitment:error"))
        
    def get(self, request, **kwargs):
        print " in get "*10
        
        res = dict()
        if request.is_ajax():
            try:
                job_id = request.GET['JobId']
                print "job_id",job_id
                request.session['job_id'] = job_id
                res['status'] = 0
            except Exception as e:
                res['status'] = 2
        
            return JsonResponse(res)
        else:
            return super(JobApplyView, self).get(request, **kwargs)
    
class JobList(TemplateView):
    template_name = "job_list.html"
    
    def get_context_data(self, **kwargs):
        res = super(JobList, self).get_context_data(**kwargs)
        all_jobs = Job.objects.all()
        res["all_jobs"] = all_jobs

        return res

class Success(TemplateView):
    template_name = "success.html"

class ErrorView(TemplateView):
    template_name = "error.htm"
    
