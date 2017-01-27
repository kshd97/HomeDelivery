from django.http import HttpResponse
from django.contrib.auth.models import User,UserManager
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from .models import Customer
#import googlemaps
from django.contrib.gis.measure import Distance, D
from datetime import datetime
#from geographiclib.geodesic import Geodesic
#from geopy.geocoders import Nominatim
from math import *
import json
import sys



def index(request):
	if request.user.is_authenticated() == True:
		user = request.user
		u = Customer.objects.filter(user = user)
		if len(u)>0:
			print("helllooooo")
			return render(request, 'Login/index.html', {'u':u})
	else:
		print("hello")
		return render(request, 'Login/Signin.html', None)

def Signin(request):
	if request.method=='POST':
		username = request.POST['Username']
		password = request.POST['Password']
		user = authenticate(username=username,password=password)
		if user is None:
			return render(request,'Login/Signin.html',{'error':'Invalid username or password'})
		else:
			login(request,user)
			user = request.user
			u = Customer.objects.filter(user = user)
			if len(u)>0:
				for i in u:
					print(i.user)
					# gmaps = googlemaps.Client(key='AIzaSyDeqb53ojQt7qbvDr2SVFSIG9RaRBqj7Q0')
					# geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
					# #print(geocode_result)
					# json_str = json.dumps(geocode_result)
					# resp = json.loads(json_str)
					# #print (resp)
					# print(resp[0])
				return render(request, 'Login/index.html', {'u':u})	
	else:
		return render(request,'Login/Signin.html',None)

def Signup(request):
	if request.method == 'POST':
		username = request.POST['Username']
		password = request.POST['Password']
		address =  request.POST['Address']
		try:
			u = User._default_manager.get(username__iexact=username) #fix for case sensitive username
			return render(request,'Login/Signup.html',{'error':'username already already exists!'})
		except User.DoesNotExist:
			user = User.objects.create_user(username=username)
			user.set_password(password)
			user.is_active = True
			user.save()

			#gmaps = googlemaps.Client(key='AIzaSyDeqb53ojQt7qbvDr2SVFSIG9RaRBqj7Q0')
			#geocode_result = gmaps.geocode(address)
			#geolocator = Nominatim()
			#print("HELKHGK")
			#location = geolocator.geocode(address, timeout=None)
			#print(location.latitude)
			profileobject = Customer(user=user,address=address)
			profileobject.save()
			user.backend = 'django.contrib.auth.backends.ModelBackend' #user backend error fix
			authenticate(username=username,password=password)
			login(request,user)
			return render(request, 'Login/index.html', {'user':user})
	else:
		return render(request,'Login/Signup.html',None) 

	
