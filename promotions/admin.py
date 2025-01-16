from django.contrib import admin
from .models.post import Post
from .models.tag import Tag
from .models.category import Category

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)