from rest_framework import serializers
from .models import Post, Vote



class PostSerializer(serializers.ModelSerializer):
    poster=serializers.ReadOnlyField(source='poster.username')
    poster_id=serializers.ReadOnlyField(source='poster.id')
    votes = serializers.SerializerMethodField()
    class Meta:
        model = Post
        field=['id', 'title', 'url', 'poster', 'created','votes']
        fields = "__all__"
    
    def get_votes(self,post):
        return Vote.objects.filter(post=post).count()


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        field=['id']
        fields = "__all__"