from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import reverse, render
from .forms import LoginForm


def login_view(request):
    html = "login.html"
    form = None

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', '/'))

    else:
        form = LoginForm()
    return render(request, html, {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))