from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category (models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class Recipe (models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=164)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    prepartion_time_unit = models.CharField(max_length=64)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=64)
    prepartion_steps = models.TextField()
    prepartion_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(
        upload_to='recipes/cover/%Y/%m/%d', blank=True, default='')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True,
        default=None
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
