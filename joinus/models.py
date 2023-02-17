from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# User = settings.AUTH_USER_MODEL


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class BoardFeature(models.Model):
    board_name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, related_name='feature', on_delete=models.CASCADE)
    update_on = models.DateTimeField(auto_now=True)
    manufacturer = models.CharField(max_length=255, blank=True)
    special_features = models.TextField(blank=True)
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

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def number_of_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('post_edit', kwargs={'pk': self.pk})


class Review(models.Model):
    board = models.ForeignKey(
        BoardFeature, on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Review {self.body} by {self.name}"

    def get_absolute_url(self):
        return reverse('post_edit', kwargs={'pk': self.pk})
