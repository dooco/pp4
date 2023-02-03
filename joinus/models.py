from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Board_feature(models.Model):
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='board_feature')
    update_on = models.DateTimeField(auto_now=True)
    board_name = models.CharField(max_length=255, unique=True)
    manufacturer = models.CharField(max_length=255, blank=True)
    microprocessor = models.CharField(max_length=255, blank=True)
    memory = models.CharField(max_length=80, blank=True)
    power = models.CharField(max_length=255, blank=True)
    clock_frequency = models.CharField(max_length=255, blank=True)
    conectivity = models.CharField(max_length=255, blank=True)
    special_features = models.CharField(max_length=500, blank=True)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.CharField(max_length=255, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    io_pin_number = models.IntegerField(default=0)
    status = models.IntegerField(choices=STATUS, default=0)
    avg_rating = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created_on']

    def average_rating(self):
        return Review.objects.filter(board=self).aggregate(
            Avg("score"))["score__avg"] or 0

    def __str__(self):
        return f"{self.board_name}: {self.average_rating()}"


class Review(models.Model):
    board = models.ForeignKey(
        Board_feature, on_delete=models.CASCADE, related_name='board')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Review {self.board.board_name} score {self.score}"
