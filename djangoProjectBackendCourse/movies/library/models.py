from django.contrib.auth.models import User
from django.db import models


class ChatSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_sessions')
    session_id = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat session for {self.user.username}"


class ChatMessage(models.Model):
    session = models.ForeignKey(ChatSession, on_delete=models.CASCADE, related_name='messages')
    message = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

class Movie(models.Model):
    poster = models.ImageField(upload_to='movie_images/')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    director = models.CharField(max_length=100)
    four_main_actors = models.CharField(max_length=100)
    year_of_release = models.PositiveIntegerField(
        help_text='Enter the year (e.g., 2025)'
    )

    @property
    def average_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            total_rating = sum(review.rating for review in reviews)
            return total_rating / reviews.count()
        return 0

    def __str__(self):
            return self.title


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    reviewer_name = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.PositiveIntegerField(help_text='Rate from 1 to 5')
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review_text

