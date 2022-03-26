from . import views
from django.urls import path

urlpatterns = [
    path('post/create/', views.post_create, name='post_create'),
    path('blog/', views.PostListView.as_view(), name='blog'),
    path('post/myposts/', views.MyPostListView.as_view(), name='myposts'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<slug:slug>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    #path('about/', views.PostDeleteView.as_view(), name=''),
]
# path('post/list/', views.PostListView.as_view(), name='post_list'),
