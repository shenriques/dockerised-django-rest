from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListCreateAPIView.as_view()),
    path('<int:pk>/', views.ArticleDetailAPIView.as_view(), name='article-detail'),
    path('<int:pk>/update', views.ArticleUpdateAPIView.as_view()),
    path('<int:pk>/delete', views.ArticleDestroyAPIView.as_view()),
]