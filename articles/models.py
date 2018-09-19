from django.db import models
from django.conf import settings
# Create your models here.

class Articles(models.Model):
	title = models.CharField(max_length=200)
	article = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	class Meta():
		db_table = 'articles'
		verbose_name_plural = 'Articles'

	def __str__(self):
		return self.title

class ArticleVotes(models.Model):
	VOTE_TYPES = (
		(1, 'upvote'),
		(2, 'downvote'),
		)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	vote_type = models.IntegerField(choices=VOTE_TYPES, null=True)
	article = models.ForeignKey('Articles', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'article_votes'
		verbose_name_plural = 'Article Votes'

	def __str__(self):
		return self.user

class ArticleComments(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	article = models.ForeignKey('Articles', on_delete=models.CASCADE)
	comment = models.CharField(max_length=1300)
	parent = models.ForeignKey('ArticleComments', on_delete=models.SET_NULL, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'article_comments'
		verbose_name_plural = 'Article Comments'

	def __str__(self):
		return self.comment

class ArticleCommentVotes(models.Model):
	VOTE_TYPES = (
		(1, 'upvote'),
		(2, 'downvote'),
		)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	comment = models.ForeignKey('ArticleComments', on_delete=models.CASCADE)
	vote_type = models.IntegerField(choices=VOTE_TYPES, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'article_comment_votes'
		verbose_name_plural = 'Article Comment Votes'

	def __str__(self):
		return self.get_vote_type_display()