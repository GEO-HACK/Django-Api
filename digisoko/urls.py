from django.contrib import admin
from django.urls import path, include  # include is used to link app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Include the app's urls.py
  
]
