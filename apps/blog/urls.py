from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list_view, name='list'),
    path('post/create/', views.post_create_view, name='create'),
    path('post/<slug:slug>/edit/', views.post_edit_view, name='edit'),
    path('post/<slug:slug>/', views.post_detail_view, name='detail'),
]
