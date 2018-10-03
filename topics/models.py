from django.db import models
from django.conf import settings
from shortcodes.shortcodes import ShortCodes
from feed.models import CategoriesMaster
# Create your models here.

class Topics(models.Model):
	title = models.CharField(max_length=500)
	description = models.TextField(null=True)
	is_private = models.BooleanField(default=0)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'topics'
		verbose_name_plural = 'Topics'
		ordering = ['-created_at']

	def __str__(self):
		return self.title

class TopicContributors(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	topic = models.ForeignKey('Topics', on_delete="CASCADE");
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'topic_contributors'
		verbose_name_plural = 'Topic Contributors'
		ordering = ['-created_at']

class Answers(models.Model):
	topic = models.ForeignKey('Topics', on_delete=models.CASCADE);
	answer = models.CharField(max_length=500)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'answers'
		verbose_name_plural = 'Answers'

	def __str__(self):
		return self.answer

class AnswerVotes(models.Model):
	vote_type = models.IntegerField(choices=ShortCodes.VOTE_TYPES, null=True)
	answer = models.ForeignKey('Answers', on_delete=models.CASCADE, default=None)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'answer_votes'
		verbose_name_plural = 'Answer Votes'

	def __str__(self):
		return self.get_vote_type_display()

class AnswerComments(models.Model):
	answer = models.ForeignKey('Answers', on_delete=models.CASCADE)
	comment = models.CharField(max_length=500)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	parent = models.ForeignKey('AnswerComments', on_delete=models.CASCADE, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'answer_comments'
		verbose_name_plural = 'Answer Comments'

	def __str__(self):
		return self.comment

class AnswerCommentVotes(models.Model):
	comment = models.ForeignKey('AnswerComments', on_delete=models.CASCADE)
	vote_type = models.IntegerField(choices=ShortCodes.VOTE_TYPES, null=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'answer_comment_votes'
		verbose_name_plural = 'Answer Comment Votes'

	def __str__(self):
		return self.vote_type

class TopicCategories(models.Model):
	topic = models.ForeignKey('Topics', on_delete=models.CASCADE)
	category = models.ForeignKey('feed.CategoriesMaster', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'topic_categories'
		verbose_name_plural = 'Topic Categories'