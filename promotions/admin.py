from django.contrib import admin
from .models.post import Post
from .models.tag import Tag
from .models.category import Category


class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
  
admin.site.register(Post, PostAdmin)

admin.site.register(Tag)
admin.site.register(Category)