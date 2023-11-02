from django.urls import path
from mynewapp import views

urlpatterns = [
    path('', views.mynewapp, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    # Other URL patterns
]
