from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import stripe
from .forms import DonationForm
from .models import Donation

stripe.api_key = settings.STRIPE_SECRET_KEY


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


def volunteer_view(request):
    return render(request, 'mainapp/volunteer.html', {})


def donation_success(request):
    return render(request, 'mainapp/success.html')


def donation_cancel(request):
    return render(request, 'mainapp/cancle.html')


def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            amount_in_cents = int(amount * 100)

            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': 'Donation',
                        },
                        'unit_amount': amount_in_cents,
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url='http://127.0.0.1:8000/donate/success/',
                cancel_url='http://127.0.0.1:8000/donate/cancel/',
            )

            return render(request, 'mainapp/donate_checkout.html', {'session_id': session.id})

    else:
        form = DonationForm()

    return render(request, 'mainapp/donate_form.html', {'form': form})


# payment/views.py


def payment_checkout(request):
    if request.method == 'POST':
        cart_items = request.POST.getlist('cart-item')
        amount = 0
        line_items = []

        for item in cart_items:
            # Calculate the total amount and construct the line items
            # based on your application's logic
            # Example: Get the product and price from the database
            # and create the line item for Stripe

            product_name = 'Product Name'  # Replace with actual product name
            product_price = 1000  # Replace with actual product price in cents

            amount += product_price

            line_items.append({
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': product_price,
                    'product_data': {
                        'name': product_name,
                    },
                },
                'quantity': 1,
            })

        try:
            intent = stripe.PaymentIntent.create(
                amount=amount,
                currency='usd',
                payment_method_types=['card'],
                line_items=line_items,
            )
            return render(request, 'mainapp/donate_checkout.html', {'client_secret': intent.client_secret})

        except stripe.error.StripeError as e:
            # Handle Stripe errors
            return render(request, 'mainapp/error.html', {'error': str(e)})

    return render(request, 'mainapp/donate_checkout.html')
