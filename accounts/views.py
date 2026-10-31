from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Profile


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            return redirect('register')

    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})

def dashboard(request):
    return render(request, 'accounts/dashboard.html')