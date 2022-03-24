from . import views
from django.urls import path

urlpatterns = [
    path('post/create/', views.post_create, name='post_create'),
    path('post/', views.PostListView.as_view(), name='posts'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('about/', views.PostDeleteView.as_view(), name='post_delete'),
]
# path('post/list/', views.PostListView.as_view(), name='post_list'),
