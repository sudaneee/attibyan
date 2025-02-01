from django.urls import path
from . import views

urlpatterns = [
    path('apply/', views.apply, name='application_form'),
    # path('success/', views.success, name='success'),
]