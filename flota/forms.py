import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import Action, Vehicle


class ActionCreateForm(forms.ModelForm):
	class Meta:
		model = Action
		fields = '__all__'
        #['', 	'name' , 'sex', 'year_of_birth', 'full_birth', 'weight', 'PESEL', 'start_kumite', 'start_kata']

class VehicleSubmitForm(forms.ModelForm):
	class Meta:
		model = Vehicle
		fields = '__all__'
