from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_page, name='news_page'),
    path('home_page/', views.home_page, name = 'home_page'),
    path('news_detail_page/', views.home_page, name = 'news_detail_page')
]