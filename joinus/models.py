from django.db import models
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
    special_features = models.TextField(blank=True)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.CharField(max_length=255, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    io_pin_number = models.IntegerField(default=0)
    status = models.IntegerField(choices=STATUS, default=0)
    avg_rating = models.ManyToManyField(
        User, related_name='feature_rating', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.board_name

    def number_of_ratings(self):
        return self.avg_rating.count()


class Review(models.Model):

    board = models.ForeignKey(
        Board_feature, on_delete=models.CASCADE, related_name='board')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Review {self.body} by {self.name}"
