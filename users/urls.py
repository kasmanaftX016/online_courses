from django.urls import path
from . import views

app_name = 'register'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('verify/', views.verify_code, name='verify_code'),
]
