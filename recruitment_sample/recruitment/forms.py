from django import forms
from .models import Candidate
from crispy_forms.helper import FormHelper

class JobApplyForm(forms.ModelForm):

    class Meta:
        model = Candidate
        fields =  ("full_name", "location", "work_status", "work_experince", "mobile_number", "email_address",
            "resume")
        
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-2'  
    helper.field_class = 'col-lg-8'
    
    def __init__(self, *args, **kwargs):
        super(JobApplyForm, self).__init__(*args, **kwargs)
        
