from rest_framework import generics
from . models import Project
from . serializers import ProjectSerializer

class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    # method for overriding object save / deletion behaviour
    def perform_create(self, serializer):

        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description') or None
        # if user doesnt provide description for new project, set it to be the title
        if description is None:
            description = title

        serializer.save(description=description)

class ProjectDetailAPIView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectUpdateAPIView(generics.UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'pk'

class ProjectDestroyAPIView(generics.DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)