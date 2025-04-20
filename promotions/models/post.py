from django.db import models
from .category import Category
from .tag import Tag

class Post(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    content = models.TextField()
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField(Tag)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='posts/images/')

    def __str__(self):
        return self.title