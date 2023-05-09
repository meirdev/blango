from django.contrib import admin
from blog.models import AuthorProfile, Comment, Tag, Post


admin.site.register(Tag)


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)

admin.site.register(Comment)

admin.site.register(AuthorProfile)
