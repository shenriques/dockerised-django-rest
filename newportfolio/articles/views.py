from rest_framework import generics
from . models import Article
from . serializers import ArticleSerializer

class ArticleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetailAPIView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'pk'

class ArticleUpdateAPIView(generics.UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'pk'

class ArticleDestroyAPIView(generics.DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)