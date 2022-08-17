from django.shortcuts import render,redirect
from carsale.forms import sale_car_form ,create_acc_form,buyer_booking_form
from carsale.models import sale_car_details ,create_acc_details,buyer_booking_details
# Create your views here.

def create_acc(request):
	return render(request,"create_acc.html")
def startpage(request):
	return render(request,"startpage.html")
def account_created(request):
	if request.method=="POST":
		t=create_acc_form(request.POST)
		if t.is_valid():
			try:
				t.save()
				return render(request,"create_acc.html")
			except:
				pass
		return render(request,"create_acc.html")
def showaccountdb(request):
	t=create_acc_details.objects.all()
	return render(request,'showaccountdb.html',{'x':t})
	
def delete_acc(request,id):
	t=create_acc_details.objects.get(id=id)
	t.delete()
	return redirect("../showaccountdb")

def edit_create_acc(request,id):
	t=create_acc_details.objects.get(id=id)
	return render(request,'edit_create_acc.html',{'x':t})
def create_acc_edit(request,id):
	t=create_acc_details.objects.get(id=id)
	f=create_acc_form(request.POST,instance=t)
	if f.is_valid():
		f.save()
		return redirect("../showaccountdb")
	return render(request,"edit_create_acc.html",{'x':t})
def welcomeboss(request):
	return render(request,'welcomeboss.html')
def login_acc(request):
	return render(request,'login_acc.html')

def loginsuccess(request):
	if request.method=='POST':
		aemail=request.POST['aemail']
		apassword=request.POST['apassword']
		try: 
			p=create_acc_details.objects.get(aemail=aemail)
			t=create_acc_details.objects.get(apassword=apassword)
			if p and t is not None:
				return render(request,'welcomeboss.html')
			else:
				return render(request,'welcomeboss.html')
		except:
			return render(request,'login_acc.html')



def uploadcar(request):
	return render(request,'uploadcar.html')

def finalupload(request):
	return render(request,'finalupload.html')
def car_details_filled(request):
	if request.method=="POST":
		t=sale_car_form(request.POST)
		if t.is_valid():
			try:
				t.save()
				return render(request,"finalupload.html")
			except:
				pass
		return render(request,"uploadcar.html")

def showcardb(request):
	t=sale_car_details.objects.all()
	return render(request,'showcardb.html',{'x':t})
	
def deletecardb(request,id):
	t=sale_car_details.objects.get(id=id)
	t.delete()
	return redirect("../showcardb")

def editcardb(request,id):
	t=sale_car_details.objects.get(id=id)
	return render(request,'editcardb.html',{'x':t})
def caredited(request,id):
	t=sale_car_details.objects.get(id=id)
	f=sale_car_form(request.POST,instance=t)
	if f.is_valid():
		f.save()
		return redirect("../showcardb")
	return render(request,"editcardb.html",{'x':t})
def showcarmain(request):
	t=sale_car_details.objects.all()
	return render(request,'showcarmain.html',{'x':t})
def viewcarfeatures(request,id):
	t=sale_car_details.objects.get(id=id)
	return render(request,'viewcarfeatures.html',{'x':t})
 
def admin_login(request):
	return render(request,'admin_login.html')
def admin_login_success(request):
	if request.method=='POST':
		User_name=request.POST['User_name']
		Pwd=request.POST['Pwd']
		try:
			if User_name=='shamik06' and Pwd=='shamik@12345':
				return render(request,'welcome_admin.html')
			else:
				return render(request,'admin_login.html')
		except:
			return render(request,'admin_login.html')

def buyerbooking(request,id):
	t=sale_car_details.objects.get(id=id)
	return render(request,'buyerbooking.html',{'x':t})
def buyercar(request,id):
	t=sale_car_details.objects.get(id=id)
	f=sale_car_form(request.POST,instance=t)
	if f.is_valid():
		f.save()
		return redirect("../buyerbooking")
	return render(request,"buyerbooking.html",{'x':t})	
def buyerordered(request):
	if request.method=="POST":
		t=buyer_booking_form(request.POST)
		if t.is_valid():
			try:
				t.save()
				return render(request,"buyerbooking.html")
			except:
				pass
		return render(request,"buyerbooking.html")
"""
def finalbooking(request):
	t=buyer_booking_details.objects.all()
	return render(request,'finalbooking.html',{'x':t})
"""
def finalbooking(request):
	t=buyer_booking_details.objects.all()
	return render(request,'finalbooking.html',{'x':t})
def printbill(request,id):
	t=buyer_booking_details.objects.get(id=id)
	return render(request,'printbill.html',{'x':t})
def showbuyerdb(request):
	t=buyer_booking_details.objects.all()
	return render(request,'showbuyerdb.html',{'x':t})
