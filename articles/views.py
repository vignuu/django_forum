from django.http import HttpResponse
from django.shortcuts import render
from django.conf.urls import url
from .import views


def index(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')

def contact(request):
	return render(request,'contact.html')

def sample(request):
	return render(request,'sample.html')

def scroll(request):
	return render(request,'scroll.html')
