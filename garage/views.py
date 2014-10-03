# Build18 Garage Protoype VIEWS

from django.shortcuts import render, get_object_or_404

def home(request):
	context = {
		"request":request
	}
	return render(request,"home.html",context)

def signup(request):
	context = {
		'request':request
	}
	return render(request,"signup.html",context)

def login(request):
	context = {
		'request':request
	}
	return render(request,"login.html")