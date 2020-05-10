from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm
from django.http import JsonResponse
from .models import Post, Comment, Subweddit

User = get_user_model()


def log_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(reverse('red1:user_list'))
        else:
            print(form.errors)
    return render(request, 'red1/login.html', {'form': form})


@login_required(login_url='/login/')
def log_out(request):
    logout(request)
    return redirect(reverse('red1:login'))

def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('red1:login'))
        else:
            print(form.errors)
    return render(request, 'red1/signup.html', {'form': form})


@login_required(login_url='/login/')
def user_list(request):
    
    users = User.objects.select_related('logged_in_user')

    for user in users:
        user.status = 'Online' if hasattr(user, 'logged_in_user') else 'Offline'

    posts = Post.objects.all().order_by('-created_on')
    response_data = {}

    if request.POST.get('action') == 'post':
        body = request.POST.get('body')
        author = request.user.username

        response_data['body'] = body
        response_data['author'] = author

        Post.objects.create(
            body = body,
            author = author,
            )
        return JsonResponse(response_data)

    context = {
        'posts':posts,
        'users':users,
    }

    return render(request, 'red1/user_list.html', context)

def create_post(request):
    posts = Post.objects.all()
    response_data = {}

    if request.POST.get('action') == 'post':
        body = request.POST.get('body')

        response_data['body'] = body
      
        Post.objects.create(
            body = body,
            )
        return JsonResponse(response_data)

    return render(request, 'red1/test.html', {'posts':posts})