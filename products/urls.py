from django.urls import path
from . import views
from .views import PostListView,PostDetailView, PostCreateView, PostUpdateView,PostDeleteView, UserPostListView


urlpatterns = [
    path('home', PostListView.as_view(), name='history'),
    path('', PostListView.as_view(), name='history'),
    path('history/', PostListView.as_view(), name='history'),
    path('history/<int:pk>/', PostDetailView.as_view(), name='event-detail'),
    path('history/<int:pk>/update/', PostUpdateView.as_view(), name='event-update'),
    path('history/new/', PostCreateView.as_view(), name='event-create'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-history'),
    path('history/<int:pk>/delete/', PostDeleteView.as_view(), name='event-delete')
]
