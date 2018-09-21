from django.contrib import admin
from topics.models import Topics, TopicContributors, Answers, AnswerVotes, AnswerComments, AnswerCommentVotes

# Register your models here.

# admin.site.register(TopicContributors)

@admin.register(Topics)
class TopicAdmin(admin.ModelAdmin):
	list_display = ['title', 'description', 'user', 'is_private', 'created_at', 'updated_at']
	list_filter = ['is_private']
	search_fields = ['title']

@admin.register(TopicContributors)
class TopicContributorsAdmin(admin.ModelAdmin):
	list_display = ['topic', 'user', 'created_at']

@admin.register(Answers)
class AnswersAdmin(admin.ModelAdmin):
	list_display = ['topic', 'answer', 'user', 'created_at']

@admin.register(AnswerVotes)
class AnswerVotesAdmin(admin.ModelAdmin):
	list_display = ['answer', 'user']

@admin.register(AnswerComments)
class AnswerCommentsAdmin(admin.ModelAdmin):
	list_display = ['comment', 'answer', 'user', 'parent', 'created_at']

@admin.register(AnswerCommentVotes)
class AnswerCommentVotes(admin.ModelAdmin):
	list_display = ['comment', 'vote_type', 'user']
	list_filter = ['vote_type']

