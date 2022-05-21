from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from classroom.forms import ContactForm

# Create your views here.

class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThankYou(TemplateView):
    template_name = 'classroom/thank_you.html'

class ContactFormView(FormView):
    form_class = ContactForm
    