from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from .forms import UserDashboardForm, UserRegistrationForm


# Create your views here.
def user_profile_view(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = UserDashboardForm(data=request.POST, instance=request.user)
            if form.is_valid():
                form.save()
        else:
            form = UserDashboardForm(instance=request.user)

        if request.method == "POST":
            p_form = PasswordChangeForm(data=request.POST, user=request.user)
            if p_form.is_valid():
                p_form.save()
                update_session_auth_hash(request, p_form.user)
                return redirect('accounts:profile')
        else:
            p_form = PasswordChangeForm(user=request.user)
        return render(request, 'accounts/profile.html', {'form': form, 'p_form': p_form})
    else:
        return redirect('accounts:login')


def user_registration_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])
            login(request, new_user)
            messages.add_message(request, messages.SUCCESS, f'Hurray! now {request.user} is registered user.')
            return redirect('accounts:profile')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/registration.html', {'form': form})



def user_login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.add_message(request, messages.SUCCESS, f'{request.user} login successfully')
            return redirect('accounts:profile')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})



def user_logout_view(request):
    if request.user.is_authenticated:
        messages.add_message(request, messages.SUCCESS, f'{request.user} logout successfully. Continue with login.')
        logout(request)
        return redirect('accounts:login')
    else:
        return redirect('accounts:login')
    