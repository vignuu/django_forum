from django.http import HttpResponse
from django.shortcuts import render
from django.conf.urls import url
from .import views


def index(request):
	return render(request,'index.html')