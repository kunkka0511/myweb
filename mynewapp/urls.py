from django.urls import path
from django.urls import include, path

from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mynewapp.urls')),
      # Include your app's URLs
]
