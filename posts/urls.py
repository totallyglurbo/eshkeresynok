from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_user, name='register'),
    path('login/', views.TheLoginView.as_view(), name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('create/', views.PostCreate.as_view(), name='create'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
    path('post/<int:pk>/delete', views.PostDelete.as_view(), name='post-delete'),
    path('post/<int:pk>/update', views.PostUpdate.as_view(), name='post-update'),
    path('profile/delete/', views.user_delete_view, name='user-delete'),
    path('profile/change/', views.user_change_view, name='user-change'),
]