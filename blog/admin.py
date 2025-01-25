from django.contrib import admin

# Register your models here.

from blog.models import Category, Comment, Post
from scanface.models import FaceLogin

class FaceLoginAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

admin.site.register(FaceLogin, FaceLoginAdmin)

