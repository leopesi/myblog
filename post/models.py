from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0,"rascunho"),
    (1,"publicado")
)
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.IntegerField(choices=STATUS, default='0')
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'posts'
        ordering = ['-date']

    def __str__(self):
        return self.title