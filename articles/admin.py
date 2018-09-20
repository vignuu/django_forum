from django.contrib import admin
from articles.models import Articles, ArticleVotes, ArticleComments, ArticleCommentVotes

# Register your models here.

@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
	list_display  = ['title', 'article', 'user', 'created_at', 'updated_at']
	list_filter   = ['title', 'article']
	search_fields = ['title', 'article']

@admin.register(ArticleVotes)
class ArticleVotesAdmin(admin.ModelAdmin):
	list_display = ['user', 'vote_type', 'article', 'updated_at']
	list_filter   = ['vote_type', 'article']
	search_fields = ['article']

@admin.register(ArticleComments)
class ArticleCommentsAdmin(admin.ModelAdmin):
	list_display = ['user', 'article', 'comment', 'parent']
	list_filter   = ['article', 'parent']
	search_fields = ['article','parent']

@admin.register(ArticleCommentVotes)
class ArticleCommentVotes(admin.ModelAdmin):
	list_display = ['user', 'comment', 'vote_type']