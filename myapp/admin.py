from django.contrib import admin

from myapp.models import Article, Author, Comment, Like

# Register your models here.
admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Like)