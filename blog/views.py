from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class PostList(ListView):
    model = Post
    template_name = 'home.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

class PostCreate(CreateView):
    model = Post
    fields = ('title', 'author', 'body')
    template_name = 'post_new.html'

class PostUpdate(UpdateView):
    model = Post
    fields = ('title', 'body')
    template_name = 'post_edit.html'
class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

# def post_detail(request,pk): .............................FBV post_detail
#     post = get_object_or_404(Post,pk=pk)
#     return render(request,'post_detail.html',{'post':post})


# def post_list(request):...................................FBV post_list
#     posts = Post.objects.all()
#     return render(request,'home.html',{'posts':posts})

