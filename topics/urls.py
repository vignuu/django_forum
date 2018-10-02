from django.urls import path, include
from topics import views

app_name = 'topics'

urlpatterns = [
	path('', views.TopicsView.as_view(), name="new"),
	path('new/', views.newTopic, name="new"),
]