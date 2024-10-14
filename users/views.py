from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from . import forms

def register_view(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crm_university:dashboard')

    ctx = {'form': forms.RegisterForm}
    return render(request, 'register.html', ctx)


def login_view(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('crm_university:dashboard')

            else:
                return HttpResponse("""<h1 style="text-align: center">There is no such user in the database</h1>""")

    ctx = {'form': forms.LoginForm}
    return render(request, 'login.html', ctx)


def logout_view(request):
    logout(request)
    return redirect('users:login')