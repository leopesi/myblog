from django.views import generic
from .models import Post
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import PostForm
from django.shortcuts import render


def index(request):
    return render(request, 'about.html')

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

class MyPostListView(generic.ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    template_name = 'my_posts.html'

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostUpdateView(generic.UpdateView):
    fields = '__all__'
    model = Post
    context_object_name = 'post_update'
    template_name = 'post_update.html'

    def get_success_url(self):
        if 'slug' in self.kwargs:
            slug = self.kwargs['slug']
        else:
            slug = 'demo'
        return reverse_lazy('post_detail', kwargs={'slug': slug})

class PostDeleteView(generic.DeleteView):
    model = Post
    fields = '__all__'
    context_object_name = 'delete_post'
    template_name = 'post_confirm_delete.html'

    def get_success_url(self):   # Permite personalizar a visualização
        return reverse_lazy('myposts')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)
