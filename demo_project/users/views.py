from django.shortcuts import render, redirect
from .forms import Signupform, Loginform
from django.http import HttpResponse

# Create your views here.
def Signupview(request):
    if request.method == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            print(form.cleaned_data.get('username'))
            form.save()
            return redirect('login')
    else:
        form = Signupform
    return render(request, 'users/signup.html', {'form': form})


def Loginview(request):
    if request.method == 'POST':
        form = Loginform(request.POST)
        if form.is_valid():
            return HttpResponse("Login Successful")
    else:
        form = Loginform
    return render(request, 'users/login.html', {'form': form})