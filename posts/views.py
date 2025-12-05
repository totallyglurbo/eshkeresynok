from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

from posts.forms import RegistrationForm
from posts.models import Post


def index(request):
    return render(request, 'index.html')


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
            return render(request, 'register.html', {'form': form})
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


class TheLoginView(LoginView):
    template_name = 'login.html'


def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def profile_view(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'profile.html', context)