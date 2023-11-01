from django.urls import path
from mynewapp import views

urlpatterns = [
    path('', views.mynewapp, name='index'),
    
    # Other URL patterns
]
