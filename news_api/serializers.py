from rest_framework import serializers
from news_api.models import Post


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=30)
    author = serializers.CharField(max_length=30)
    upvotes = serializers.IntegerField(required=False)
    creation_date = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        """
        Create and return a new `Post` instance, given the validated data.
        """
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return and existing `Post` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.upvotes = validated_data.get('upvotes', instance.upvotes)
        instance.save()
        return instance

