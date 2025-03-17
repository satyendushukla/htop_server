from django.contrib import admin
from django.urls import path
from myapp.views import htop_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('htop/', htop_view),
    path('', htop_view),  # Add this to map '/' to '/htop/'
]
