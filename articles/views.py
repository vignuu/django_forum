from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf.urls import url
from .import views
from django.contrib.auth.decorators import login_required
from articles.models import Articles, Categories
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


@login_required(login_url='accounts:login')
def index(request):
	if request.method == 'POST':
		form = Categories(category_title = request.POST['categories'])
		form.save()
		form = Articles(title = request.POST['title'], article = request.POST.get('article'), user = request.user,categorie_id = Categories.objects.latest('id') )
		form.save()
		return redirect('articles:index')
	article = Articles.objects.all().order_by('updated_at')
	paginator = Paginator(article, 1) # Show 25 contacts per page
	page = request.GET.get('page')
	article = paginator.get_page(page)
	return render(request,'index.html',{'article' : article})

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
