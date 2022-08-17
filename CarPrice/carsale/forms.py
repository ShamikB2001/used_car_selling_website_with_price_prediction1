from django import forms
from carsale.models import create_acc_details,sale_car_details,buyer_booking_details
class create_acc_form(forms.ModelForm):
	class Meta:
		model=create_acc_details
		fields="__all__"
class sale_car_form(forms.ModelForm):
	class Meta:
		model=sale_car_details
		fields="__all__"

class buyer_booking_form(forms.ModelForm):
	class Meta:
		model=buyer_booking_details
		fields="__all__"
