from django.views import generic
from .models import Post
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from .forms import PostForm

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.text = post.text.upper()
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'post_create.html', {'form': form})

class PostListView(generic.ListView):
    queryset = Post.objects.filter(status=1)
    context_object_name = 'posts'
    template_name = 'index.html'

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = 'post_update.html'

class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'post_delete.html'

