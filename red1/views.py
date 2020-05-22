from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import DetailView, TemplateView
from django.contrib.auth import get_user_model, login, logout
from .models import Post, Comment, Subweddit, LoggedInUser, Follow
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.core import serializers
from .forms import PostForm, CommentForm, FollowForm
from django.http import JsonResponse

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
    
    form =  PostForm

    context = {
        'users':users,
        'form':form,
        'posts':posts,
    }

    return render(request, 'red1/user_list.html', context)


def user_post(request):
    
    if request.is_ajax and request.method == 'POST':
        
        form = PostForm(request.POST)
        
        if form.is_valid():

            instance = form.save(commit=False)

            instance.author = LoggedInUser.objects.get(user=request.user)

            instance.save()

            form.save_m2m()

            ser_instance = serializers.serialize('json', [ instance, ])

            print(ser_instance)

            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, status=400)

    return JsonResponse({"error": ""}, status=400)

class DiscoverView(TemplateView):

    template_name = 'red1/weddit.html'

    def get_context_data(self, pk, *args, **kwargs):
        
        context = super(DiscoverView, self).get_context_data()

        weddits = Subweddit.objects.filter(pk=pk)

        self.kwargs['pk']

        following = []
        for i in weddits:
            if len(i.followers.filter(user=self.request.user.id)) == 0:
                following.append((i, False))
            else:
                following.append((i, True))

        context['subweddits'] = Subweddit.objects.filter(pk = pk)
        context['post_detail'] = Post.objects.filter(weddits = pk).order_by('-created_on')
        context['form'] = FollowForm()
        context['login_user'] = self.request.user
        context['following'] = following

        return context

class FollowView(CreateView):
    form_class = FollowForm
    model = Follow
    success_url = reverse_lazy('red1:user_list')
    def form_valid(self, form):
        form.user = self.request.user
        return super(FollowView, self).form_valid(form)

class UnfollowView(DeleteView):
    model = Follow
    success_url = reverse_lazy('red1:user_list')
    def get_object(self):
        target_id = self.kwargs['target_id']
        return self.get_queryset().get(target__id=target_id)