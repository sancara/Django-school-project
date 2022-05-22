from django.urls import path
from .views import ContactFormView, HomeView, TeacherDetailView, ThankYou, TeacherCreateView, TeacherListView, TeacherUpdateView, TeacherDeleteView

app_name = 'classroom'

urlpatterns = [
    path('', HomeView.as_view() , name='home'),
    path('thanks/', ThankYou.as_view(), name='thanks'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('teacher/', TeacherCreateView.as_view(), name='teacher'),
    path('teacher_list/', TeacherListView.as_view(), name='teacher_list'),
    path('teacher_detail/<int:pk>', TeacherDetailView.as_view(), name='detail_teacher'),
    path('update_teacher/<int:pk>', TeacherUpdateView.as_view(), name='update_teacher'),
    path('delete_teacher/<int:pk>', TeacherDeleteView.as_view(), name='delete_teacher')
]