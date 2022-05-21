from django.urls import path
from .views import HomeView, ThankYou

app_name = 'classroom'

urlpatterns = [
    path('', HomeView.as_view() , name='home'),
    path('thanks/', ThankYou.as_view(), name='thanks')
]