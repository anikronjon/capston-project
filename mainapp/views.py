import stripe
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.conf import settings


stripe.api_key = settings.STRIPE_SECRET_KEY


def home_view(request):
    context = {
        'user': request.user
    }
    return render(request, 'mainapp/index.html', {})


def service_view(request):
    return render(request, 'mainapp/service.html', {})


def project_view(request):
    return render(request, 'mainapp/project.html', {})


def contact_view(request):
    return render(request, 'mainapp/contact.html', {})


def volunteer_view(request):
    return render(request, 'mainapp/volunteer.html', {})


def payment(request):
    public_key = settings.STRIPE_PUBLISHABLE_KEY
    return render(request, 'mainapp/donate.html', {'public_key': public_key})


def charge(request):

    return render(request, 'mainapp/success.html')