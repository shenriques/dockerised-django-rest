from django.urls import path
from . import views
urlpatterns = [
    path('', views.ProjectListCreateAPIView.as_view()),
    path('<int:pk>/', views.ProjectDetailAPIView.as_view(), name='project-detail'),
    path('<int:pk>/update', views.ProjectUpdateAPIView.as_view()),
    path('<int:pk>/delete', views.ProjectDestroyAPIView.as_view()),
]