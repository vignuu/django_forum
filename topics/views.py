from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from topics.models import Topics
from django.http import JsonResponse, HttpResponseRedirect
from django.views.generic import ListView

# Create your views here.

class TopicsView(ListView):
	template_name = 'topics/topics.html'
	model = Topics
	context_object_name = 'topics'   # your own name for the list as a template variable
	queryset = Topics.objects.all() # Get 5 books containing the title war
	paginate_by = 10

@login_required
def newTopic(request):
	if request.method == 'GET':
		return render(request, 'topics/new_topic.html')

	else:
		form = {}
		errors = []
		if(request.POST['title']):
			topic = Topics()
			topic.title = request.POST['title']
			topic.description = request.POST['description']
			topic.user = request.user

			if 'is_private' in request.POST:
				topic.is_private = 1
			topic.save()
		else:
			errors.append('Title is Mandatory')
			form['errors'] = errors
			return render(request, 'topics/new_topic.html', form)
		return HttpResponseRedirect('/topics/new')