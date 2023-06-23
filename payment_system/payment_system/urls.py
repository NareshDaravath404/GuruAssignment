# payment_system/urls.py
from django.urls import path
from userwallet import views
from django.contrib import admin


urlpatterns = [
    path('user/', views.home, name='home'),
    path('', views.signin, name='signin'),
    path('admin/', admin.site.urls),
    path('start_timer/', views.start_timer, name='start_timer'),
    path('stop_timer/', views.stop_timer, name='stop_timer'),
    path('signup/',views.signup,name='signup'),
    path('signup/addcoins/',views.addcoins,name='addcoins'),
    path('signup/addcoins/user/',views.home,name='home1'),
]
