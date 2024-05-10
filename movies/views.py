from rest_framework import generics
from movies.models import Movie
from movies.serializers import MovieSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from movies.permissions import IsAdminUser

class MovieView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
