from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('', include('home.urls', namespace='home')),
    path('posts/', include('posts.urls', namespace='posts')),
]