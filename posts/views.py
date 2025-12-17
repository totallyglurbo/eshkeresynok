from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from posts.forms import RegistrationForm, PostForm
from posts.models import Post


def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'index.html', context)


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


class PostCreate(CreateView):
    model = Post
    template_name = 'post_form.html'
    form_class = PostForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PostDelete(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('profile')

class PostUpdate(UpdateView):
    model = Post
    fields = ['name', 'description', 'status']
    template_name = 'post_form.html'
    success_url = reverse_lazy('index')

@login_required
def user_delete_view(request):
    user_to_delete = request.user
    if request.method == 'POST':
        user_to_delete.delete()
        return redirect(reverse('index'))
    return render(request, 'delete_user.html', {'user_to_delete': user_to_delete})


@login_required
def user_change_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('profile'))
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = RegistrationForm(instance=request.user)

    return render(request, 'register.html', {'form': form})