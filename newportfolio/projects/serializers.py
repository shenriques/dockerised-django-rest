from rest_framework import serializers
from . models import Project

class ProjectSerializer(serializers.ModelSerializer):

    # add clickable url for each product (only works on model serialiser)
    url = serializers.HyperlinkedIdentityField(view_name='project-detail', lookup_field='pk')
    
    class Meta:
        model = Project
        fields = '__all__'