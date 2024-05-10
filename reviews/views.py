from rest_framework import generics
from django.shortcuts import get_object_or_404
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from reviews.permissions import IsCriticOrAdmin

class ReviewView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCriticOrAdmin]

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
   
    def perform_create(self, serializer):
        serializer.save(critic=self.request.user)
