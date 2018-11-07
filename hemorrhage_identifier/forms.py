from django import forms
from .models import Hemorrhage

class HemorrhageForm(forms.ModelForm):
	class Meta:
		model = Hemorrhage
		fields = ['ct_scan_image',]