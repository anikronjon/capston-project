from django.urls import path
from . import views

app_name = 'mainapp'
urlpatterns = [
    path('', views.home_view, name='home_page'),
    path('about/', views.about_view, name='about_page'),
    path('service/', views.service_view, name='service_page'),
    path('project/', views.project_view, name='project_page'),
    path('contact/', views.contact_view, name='contact_page'),
    path('payment/', views.payment_view, name='paymentPage'),
    path('success/', views.success, name='success'),
]