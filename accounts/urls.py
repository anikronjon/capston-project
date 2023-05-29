from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('profile/', views.user_profile_view, name='profile'),
    path('registration/', views.user_registration_view, name='registration'),
    path('login/', views.user_login_view, name='login'),
    path('logout/', views.user_logout_view, name='logout'),
]
