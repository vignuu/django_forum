from django.contrib import admin
from articles.models import Articles, ArticleVotes, ArticleComments, ArticleCommentVotes

# Register your models here.

@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
	list_display = ['title', 'article', 'user', 'created_at', 'updated_at']

@admin.register(ArticleVotes)
class ArticleVotesAdmin(admin.ModelAdmin):
	list_display = ['user', 'vote_type', 'article', 'updated_at']

@admin.register(ArticleComments)
class ArticleCommentsAdmin(admin.ModelAdmin):
	list_display = ['user', 'article', 'comment', 'parent']

@admin.register(ArticleCommentVotes)
class ArticleCommentVotes(admin.ModelAdmin):
	list_display = ['user', 'comment', 'vote_type']