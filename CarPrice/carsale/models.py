from django.db import models

# Create your models here.
class create_acc_details(models.Model):
	aname=models.CharField(max_length=200)
	aemail=models.CharField(max_length=200)
	aphoneno=models.CharField(max_length=20)
	apassword=models.CharField(max_length=200)
	acpassword=models.CharField(max_length=200)
#	atype=models.CharField(max_length=200)
	class Meta:
		db_table="create_acc_details"
class sale_car_details(models.Model):
	user_name=models.CharField(max_length=200)#5
	car_state=models.CharField(max_length=200)#7
	user_phoneno=models.CharField(max_length=50)#6
	car_model_name=models.CharField(max_length=200) #1
	car_brand=models.CharField(max_length=200)#7
	car_image=models.CharField(max_length=500)#8
	car_price=models.CharField(max_length=200) #2
	year=models.CharField(max_length=200)#3
	seller_type=models.CharField(max_length=200)#4
	km_driven=models.CharField(max_length=200)#9
	owner_type=models.CharField(max_length=200)#10
	fuel_type=models.CharField(max_length=200)#11
	transmission_type=models.CharField(max_length=200)#12
	mileage=models.CharField(max_length=200)#13
	engine=models.CharField(max_length=200)#14
	max_power=models.CharField(max_length=200)#15
	seats=models.CharField(max_length=200)#16
	class Meta:
		db_table="sale_car_details"

class buyer_booking_details(models.Model):
	buyer_name=models.CharField(max_length=200)
	buyer_email=models.EmailField()
	buyer_phone=models.CharField(max_length=200)
	buyer_address=models.CharField(max_length=200)
	buyer_pincode=models.CharField(max_length=200)
	buyer_time=models.CharField(max_length=500)
	buser_name=models.CharField(max_length=200)#5
	bcar_state=models.CharField(max_length=200)#7
	buser_phoneno=models.CharField(max_length=50)#6
	bcar_model_name=models.CharField(max_length=200) #1
	bcar_brand=models.CharField(max_length=200)#7
	bcar_image=models.CharField(max_length=500)#8
	bcar_price=models.CharField(max_length=200) #2
	byear=models.CharField(max_length=200)#3
	bseller_type=models.CharField(max_length=200)#4
	bkm_driven=models.CharField(max_length=200)#9
	bowner_type=models.CharField(max_length=200)#10
	bfuel_type=models.CharField(max_length=200)#11
	btransmission_type=models.CharField(max_length=200)#12
	bmileage=models.CharField(max_length=200)#13
	bengine=models.CharField(max_length=200)#14
	bmax_power=models.CharField(max_length=200)#15
	bseats=models.CharField(max_length=200)#16
	class Meta:
		db_table="buyer_booking_details"