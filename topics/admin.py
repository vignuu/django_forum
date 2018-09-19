from django.contrib import admin
from topics.models import Topics, TopicContributors, Answers, AnswerVotes

# Register your models here.

# admin.site.register(TopicContributors)

admin.site.register(Topics)
admin.site.register(TopicContributors)
admin.site.register(Answers)
admin.site.register(AnswerVotes)


