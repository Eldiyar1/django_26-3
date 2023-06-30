from django.contrib import admin
from blog.models import Post, CommentPost

admin.site.register(Post)
admin.site.register(CommentPost)

