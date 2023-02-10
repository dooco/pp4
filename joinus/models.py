from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class BoardFeature(models.Model):
    board_name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    update_on = models.DateTimeField(auto_now=True)
    manufacturer = models.CharField(max_length=255, blank=True)
    special_features = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.CharField(max_length=255, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.board_name

    def number_of_likes(self):
        return self.likes.count()


class Review(models.Model):
    board = models.ForeignKey(
        BoardFeature, on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Review {self.body} by {self.name}"
