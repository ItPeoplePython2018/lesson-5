from django.contrib import admin
from django.urls import path, import

urlpatterns = [
    path('', include('blog.articles.urls'),
    path('admin/', admin.site.urls),
]
