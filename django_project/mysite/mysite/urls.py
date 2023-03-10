from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('about/', views.about),
    path('app/', include('myapp.urls')),
    path('admin/', admin.site.urls),
    # path('', views.home),  # Catch-all URL pattern
]
