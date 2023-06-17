# payment_system/urls.py
from django.urls import path
from userwallet import views
from django.contrib import admin


urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('start_timer/', views.start_timer, name='start_timer'),
    path('stop_timer/', views.stop_timer, name='stop_timer'),
]
