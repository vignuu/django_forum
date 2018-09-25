from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def loginUser(request):
	if request.method == 'POST':
		user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			login(request, user)
			return HttpResponseRedirect('/admin/')
		else:
			data = {
			'errors' : ['invalid username/password']
			}
			return render(request, 'accounts/login.html', data)
	else:
		return render(request, 'accounts/login.html');

def logoutUser(request):
	logout(request)
	return HttpResponseRedirect('/accounts/login/')
