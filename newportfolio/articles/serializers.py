from rest_framework import serializers
from . models import Article

class ArticleSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='article-detail', lookup_field='pk')
    
    class Meta:
        model = Article
        fields = '__all__'