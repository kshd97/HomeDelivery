from django.http import HttpResponse
from django.contrib.auth.models import User,UserManager
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from Login.models import Customer
from Login_Store.models import Store 
from .models import ItemList, Transaction, Price, Cart
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(request):
	return HttpResponse("Hello")

def Category_Shop(request):
	top = ItemList.objects.filter(rating__gte=3)
	categories = ItemList.objects.order_by().values('category').distinct()
	return render(request, 'Buy/Categories.html', {'categories':categories, 'top':top})

def Category(request,cat):
	lists = ItemList.objects.filter(category=cat)
	return render(request,'Buy/List.html', {'lists':lists})

@csrf_exempt
def Item(request, cat, item):
	ids = ItemList.objects.filter(p_name=item)
	print(ids)
	for i in ids:
		details = Price.objects.filter(p_id=i.p_id)
		request.session['P_id'] = i.p_id

	return render(request, 'Buy/Details.html', {'details':details})

def Search(request):
	if request.method == 'GET': 
		sq = request.GET.get('search_box', None)
		lists = ItemList.objects.filter(p_name__icontains=sq)
		return render(request,'Buy/List.html', {'lists':lists})

@csrf_exempt
def AddToCart(request):
	if request.method=='POST':
	 	quantity = request.POST['quantity']
	 	preference = request.POST['Preference']
	 	rating = request.POST['Rating']
	 	p_id = request.POST['p_id']
	 	q = ItemList.objects.filter(p_id=p_id)
	 	if rating is not None:
	 		q.rating = (((q.rating*q.number)+rating)/(q.number+1))
	 		q.number = (q.number+1)
	 		q.save()
	 	u = request.user
	 	k = Customer.objects.filter(user=u)
	 	#n = Store.objects.filter(user=preference)

	 	for i in k:
	 		#for j in n:
	 		A = Cart(c_id=i, p_id=p_id, quantity=quantity, preference=preference)
	 		A.save()
	 	return render(request,'Buy/Categories.html')


	return HttpResponse("BLAH")

		