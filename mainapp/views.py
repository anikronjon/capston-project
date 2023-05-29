from django.shortcuts import render, redirect
import stripe
from django.conf import settings
from django.http import HttpResponse
def home_view(request):
    context = {
        'user': request.user
    }
    return render(request, 'mainapp/index.html', {})


def about_view(request):
    return render(request, 'mainapp/about.html', {})


def service_view(request):
    return render(request, 'mainapp/service.html', {})


def project_view(request):
    return render(request, 'mainapp/project.html', {})


def contact_view(request):
    return render(request, 'mainapp/contact.html', {})


def success(request):
    return render(request, 'mainapp/success.html')
def payment_view(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    if request.method == 'POST':
        token = request.POST.get('stripeToken')
        change = stripe.checkout.Session.create(
            mode='payment',
            ammount=1000,
            currency='usd',
            description='Donate',
            source=token
        )
        return redirect('mainapp:success')
    return render(request, 'mainapp/payment.html', {'publishable_key': settings.STRIPE_PUBLISHABLE_KEY})