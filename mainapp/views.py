from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect
import requests


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


def initiate_payment(request):
    amount = 1000  # Example amount in BDT

    # Construct the request payload
    payload = {
        'amount': amount,
        # Add other required parameters
    }

    # Send a request to the Bikash API for initiating the payment
    response = requests.post(
        'https://api.bikash.io/checkout/token/grant',  # Example endpoint URL
        json=payload,
        headers={
            'MerchantId': 'YOUR_MERCHANT_ID',
            'APIKey': 'YOUR_API_KEY',
        }
    )

    # Process the response and extract the payment URL or other relevant data
    if response.status_code == 200:
        payment_url = response.json().get('payment_url')
        # Redirect the user to the payment URL or render a template with the payment URL
        return render(request, 'mainapp/donate.html', {'payment_url': payment_url})
    else:
        # Handle the error case appropriately
        return render(request, 'mainapp/error.html')


def payment_status(request):
    # Example implementation:
    if request.method == 'POST':
        # Process the payment status notification
        # Extract the relevant data from the request and update your models accordingly
        return HttpResponse(status=200)
    else:
        return HttpResponseNotAllowed(['POST'])