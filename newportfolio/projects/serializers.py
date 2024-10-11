from rest_framework import serializers
from . models import Project
from topics.models import Topic

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'name']

class ProjectSerializer(serializers.ModelSerializer):
    topics = serializers.ListField(
        child=serializers.CharField(),  # accept topic names as strings in request
        write_only=True  # not returned in response
    )
    topic_list = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name',
        source='topics'  # topics = reverse relation in model
    )

    url = serializers.HyperlinkedIdentityField(view_name='project-detail', lookup_field='pk')

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'image', 'slug', 'topics', 'topic_list', 'url', 'updated', 'created']

    def create(self, validated_data):
        topics_data = validated_data.pop('topics', [])  # get topics from dict
        project = Project.objects.create(**validated_data)  # make a project

        # create / get topics and add to the project
        for topic_name in topics_data:
            topic, _ = Topic.objects.get_or_create(name=topic_name)
            project.topics.add(topic)

        return project

    def update(self, instance, validated_data):
        # use pop and none in case 'topics' isnt in data
        topics_data = validated_data.pop('topics', None)
        
        instance = super().update(instance, validated_data)

        # update topics if theres data
        if topics_data is not None:
            instance.topics.clear()  # clear existing topics
            for topic_name in topics_data:
                topic, _ = Topic.objects.get_or_create(name=topic_name)
                instance.topics.add(topic)

        return instance
