from rest_framework import serializers
from .models import Post,Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        extra_kwargs = {
            "likes":{"read_only":True},
        }
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret["like_counts"] = len(ret["likes"])
        return ret

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

