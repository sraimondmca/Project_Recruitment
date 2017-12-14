from django.conf.urls import  url 

import views

urlpatterns = (
    url(
        regex=r'^apply_jobs/$',
        view=views.JobApplyView.as_view(),
        name='apply_jobs'
    ),
    url(
        regex=r'^success$',
        view=views.Success.as_view(),
        name='success'
    ),
    url(
        regex=r'^error$',
        view=views.ErrorView.as_view(),
        name='error'
    ),
)