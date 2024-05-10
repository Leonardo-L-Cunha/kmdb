from rest_framework import serializers
from movies.models import Movie
from genres.models import Genre
from genres.serializers import GenreSerializer
import ipdb

class MovieSerializer(serializers.ModelSerializer):
    
    genres = GenreSerializer(many=True)
    def create(self, validated_data):
        genres_data = validated_data.pop('genres')
        
        movie = Movie.objects.create(**validated_data)
        
        for genre_name in genres_data:
            genre, created = Genre.objects.get_or_create(**genre_name)
            movie.genres.add(genre)
            
        return movie

    class Meta:
        model = Movie
        fields = ['id', 'title', 'duration', 'premiere', 'budget', 'overview','genres']  