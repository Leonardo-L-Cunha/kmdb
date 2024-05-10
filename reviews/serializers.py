from rest_framework import serializers
from reviews.models import Review
from users.serializers import CriticSerializer
from django.shortcuts import get_object_or_404
from movies.models import Movie
import uuid
import ipdb
class ReviewSerializer(serializers.ModelSerializer):
    movie_id = serializers.UUIDField(read_only=True)
    critic = CriticSerializer(required=False)

    def create(self, validated_data):
        movie_id = self.context['view'].kwargs['movie_id']
        movie = get_object_or_404(Movie, id=movie_id)
        
        return Review.objects.create(**validated_data, movie_id=str(movie.id))

    class Meta:
        model = Review
        fields = ['id','stars','review','spoilers','movie_id','critic']
        read_only_fields = ['id', 'movie_id', 'critic']