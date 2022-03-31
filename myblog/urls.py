from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls), # Django admin route
    path('', include('post.urls')),
    path('', include("post.authentication.urls")), # Auth routes - login / register
    path('', include("post.home.urls")) # UI Kits Html files

#Add Django site authentication urls (for login, logout, password management)
    #path('accounts/', include('django.contrib.auth.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
