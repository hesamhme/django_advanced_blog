from rest_framework import serializers
from ...models import Post

# class PostSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['id', 'author','title','content', 'status', 'category', 'created_date', 'publish_date']