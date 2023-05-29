from django.urls import path
from . import views

app_name = 'mainapp'
urlpatterns = [
    path('', views.home_view, name='home_page'),
    path('about/', views.about_view, name='about_page'),
    path('service/', views.service_view, name='service_page'),
    path('project/', views.project_view, name='project_page'),
    path('contact/', views.contact_view, name='contact_page'),
    path('volunteer/', views.volunteer_view, name='volunteer'),
    path('donate/', views.donate, name='paymentPage'),
    path('donate/success/', views.donation_success, name='donation_success'),
    path('donate/cancel/', views.donation_cancel, name='donation_cancel'),
    path('checkout/', views.payment_checkout, name='payment'),

]