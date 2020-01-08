from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name = 'index'),
    path('login.html', views.login, name = 'login'),
    path('search.html', views.search, name = 'search'),
    path('books.html', views.book, name = 'book'),
    url(r'^submit', views.submit),
    url(r'^viewBook', views.viewBook),
]