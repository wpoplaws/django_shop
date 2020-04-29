from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('authentication was successful')
            else:
                return HttpResponse('Account is locked')
        else:
            return HttpResponse('Incorrect username or password')

    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})
