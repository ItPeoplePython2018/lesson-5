from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('blog.articles.urls')),
    path('admin/', admin.site.urls),
]
