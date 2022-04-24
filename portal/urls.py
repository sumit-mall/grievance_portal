from django.conf.urls import include
from django.urls import path
from django.views.generic import TemplateView
from portal import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',TemplateView.as_view(template_name='index.html'), name= 'index'),
    path('status/',TemplateView.as_view(template_name="status.html"),name='status'),
    path('about/',TemplateView.as_view(template_name='about.html'),name='about'),
    path('oauth/',include("social_django.urls")), 
    path('login/',TemplateView.as_view(template_name='registration/login.html'),name='login'),
    path('complaint/add',views.complaint_add, name="complaint_add"),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('contactus/',views.contactme, name="contact"),
    path('searchresult/',views.complaintstatus,name="result"),
    path('success/',TemplateView.as_view(template_name='success.html'), name="success"),
]