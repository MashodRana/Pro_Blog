from django.contrib import admin

from .models import ArticleModel, CommentModel
# Register your models here.

admin.site.register(ArticleModel)
admin.site.register(CommentModel)

