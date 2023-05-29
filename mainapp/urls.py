from django.urls import path
from . import views

app_name = 'mainapp'
urlpatterns = [
    path('', views.home_view, name='home_page'),
    path('service/', views.service_view, name='service_page'),
    path('project/', views.project_view, name='project_page'),
    path('contact/', views.contact_view, name='contact_page'),
    path('volunteer/', views.volunteer_view, name='volunteer'),
    path('initiate-payment/', views.initiate_payment, name='initiate_payment'),
    path('payment-status/', views.payment_status, name='payment_status'),

]