from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
import uuid

class Review(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False) 
    stars = models.PositiveSmallIntegerField(
        'Stars', 
        validators=[
            MinValueValidator(1, 'Rating must be at least 1 star.'), 
            MaxValueValidator(5, 'Rating cannot be more than 5 stars.')
        ]
    )
    review = models.TextField()
    spoilers = models.BooleanField(null=True, default=False)

    movie = models.ForeignKey(
        'movies.Movie',
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    critic = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='reviews'
    )


