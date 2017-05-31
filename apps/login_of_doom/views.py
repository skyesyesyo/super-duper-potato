# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import User

# Create your views here.

# GET "/" ->
# POST "/register" -> register
# Post "/login" -> login

def index(request):
	return render(request, 'login_of_doom/index.html')

def register(request):
	if request.method == "POST":
		form = request.POST

		# IMAGINE YOU VALIDATED YOUR REGISTRATION HERE

		User.objects.create(first_name=form['first_name'], last_name=form['last_name'], email=form['email'], password=form['password'])

		# assume we show flash message that say, "login now!"

	return redirect("logins:index")

def login(request):
	if request.method == "POST":
		form = request.POST
		
		# user_check = User.objects.filter(email=request.POST['email'])
		if User.objects.filter(email=request.POST['email']):
			user = User.objects.filter(email=request.POST['email'])[0]
			print '*' *50
			print User.objects.filter(email=request.POST['email'])
			if user.password == request.POST['password']:
				# if we made it here we want to put their id in the seesions
				# to present them being loggedin.
				# and then redirect to secrets:dashboard
				request.session['user_id'] = user.id
				return redirect("secrets:dashboard")


	return redirect("logins:index")

def logout(request):
	pass