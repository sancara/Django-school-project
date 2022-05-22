from typing import List
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView
from classroom.forms import ContactForm
from classroom.models import Teacher

# Create your views here.

class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThankYou(TemplateView):
    template_name = 'classroom/thank_you.html'


class TeacherCreateView(CreateView):
    model = Teacher
    fields = '__all__'
    success_url = reverse_lazy('classroom:thanks')


class TeacherListView(ListView):
    model = Teacher

class TeacherDetailView(DetailView):
    model = Teacher

    

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    success_url = '/classroom/thanks'

    def form_valid(self, form: ContactForm):
        print(form.cleaned_data)
        return super().form_valid(form)