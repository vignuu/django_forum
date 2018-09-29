from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def loginUser(request):
	if request.method == 'POST':
		user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			request.session.set_expiry(86400)
			login(request, user)
			if 'next' in request.POST:
				return redirect(request.POST.get('next'))
			else:
				return HttpResponseRedirect('/articles/')
		else:
			data = {
			'errors' : ['invalid username/password']
			}
			return render(request, 'accounts/login.html', data)
	else:
		if request.user.is_authenticated:
			return HttpResponseRedirect('/articles/')
		return render(request, 'accounts/login.html');

def logoutUser(request):
	logout(request)
	return HttpResponseRedirect('/accounts/login/')

