from django.http import HttpResponse
from django.shortcuts import render
from django.conf.urls import url
from .import views
from django.contrib.auth.decorators import login_required


@login_required(login_url='accounts:login')
def index(request):
	return render(request,'index.html')

@login_required(login_url='accounts:login')
def about(request):
	return render(request,'about.html')

@login_required(login_url='accounts:login')
def contact(request):
	return render(request,'contact.html')

@login_required(login_url='accounts:login')
def sample(request):
	return render(request,'sample.html')

@login_required(login_url='accounts:login')
def scroll(request):
	return render(request,'scroll.html')

@login_required(login_url='accounts:single')
def single(request):
	return render(request,'single.html')
