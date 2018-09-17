from django.db import models
from django.conf import settings

# Create your models here.

class Topics(models.Model):
	title = models.CharField(max_length=500)
	description = models.TextField(null=True)
	is_private = models.BooleanField(default=False)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete="CASCADE")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'topics'

class TopicContributors(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete="CASCADE")
	topic = models.ForeignKey('Topics', on_delete="CASCADE");
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'topic_contributors'

class Answers(models.Model):
	topic = models.ForeignKey('Topics', on_delete="CASCADE");
	answer = models.CharField(max_length=500)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete="CASCADE")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'answers'

class AnswerVotes(models.Model):
	VOTE_TYPES = (
		(1, 'upvote'),
		(2, 'downvote'),
		)
	vote_type = models.IntegerField(choices=VOTE_TYPES, null=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete="CASCADE")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)