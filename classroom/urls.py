from django.urls import path
from .views import ContactFormView, HomeView, ThankYou, TeacherCreateView, TeacherListView

app_name = 'classroom'

urlpatterns = [
    path('', HomeView.as_view() , name='home'),
    path('thanks/', ThankYou.as_view(), name='thanks'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('teacher/', TeacherCreateView.as_view(), name='teacher'),
    path('teacher_list/', TeacherListView.as_view(), name='teacher_list')
]