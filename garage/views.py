# Build18 Garage Protoype VIEWS

from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from models import Builder,Team,Part
from forms import BuildersForm, TeamForm, PartForm, UserForm

def home(request):
	loggedin = request.user.is_authenticated()
	context = {
		"request":request,
		"loggedin":loggedin
	}
	return render(request,"home.html",context)

def signup(request):
	form = UserForm()
	context = {
		'form': form
	}
	return render(request,"signup.html",context)

def signin(request):
	context = {
		'request':request
	}
	return render(request,"login.html")

def signout(request):
	logout(request)
	return HttpResponseRedirect(reverse('home'))

def profile(request):
	context = {
		'request':request
	}
	return;

def create_user(request):
	form = UserForm(request.POST)
	if form.is_valid():
	# if form is valid, save user acct and link profile
		user = form.save()
		builder = Builder(user=user)
		builder.save()
		return HttpResponseRedirect(reverse('home'))
	else:
		form = UserForm()
		print "form invalid srry try again"
		return render(request, 'signup.html', {'form':form})

def authenticator(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return HttpResponseRedirect(reverse('home'))
		else:
			print "USER INACTIVE"
			return HttpResponseRedirect(reverse('login'))
	else:
		print "INVALID CREDENTIALS"
		return HttpResponseRedirect(reverse('login'))