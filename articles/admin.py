from django.contrib import admin
from articles.models import Articles, ArticleVotes, ArticleComments, ArticleCommentVotes, Categories

# Register your models here.

@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
	list_display  = ['title', 'article', 'user', 'created_at', 'updated_at']
	list_filter   = ['title', 'article']
	search_fields = ['title', 'article']
	list_per_page = 10

@admin.register(ArticleVotes)
class ArticleVotesAdmin(admin.ModelAdmin):
	list_display = ['user', 'vote_type', 'article', 'updated_at']
	list_filter   = ['vote_type', 'article']
	search_fields = ['article']
	list_per_page = 10

@admin.register(ArticleComments)
class ArticleCommentsAdmin(admin.ModelAdmin):
	list_display = ['user', 'article', 'comment', 'parent']
	list_filter   = ['article', 'parent']
	search_fields = ['article','parent']
	list_per_page = 10

@admin.register(ArticleCommentVotes)
class ArticleCommentVotes(admin.ModelAdmin):
	list_display = ['user', 'comment', 'vote_type']
	list_per_page = 10

@admin.register(Categories)
class Categories(admin.ModelAdmin):
	list_display = ['category_title']
	list_filter = ['category_title']
	search_fields = ['category_title']
	list_per_page = 10
