from django.shortcuts import render, get_object_or_404, redirect
from .models import Hemorrhage
from .forms import HemorrhageForm
from .identifier import identify_image

# Create your views here.

def index(request):
	return render(request, 'hemorrhage_identifier/index.html',{})

def identify_hemorrhage(request):
	if request.method == 'POST':
		form = HemorrhageForm(request.POST,request.FILES)
		if form.is_valid():
			new_hemorrhage = Hemorrhage.objects.create()
			new_hemorrhage.ct_scan_image = form.cleaned_data['ct_scan_image']
			new_hemorrhage.output = identify_image(new_hemorrhage.ct_scan_image)
			new_hemorrhage.save()
			return redirect('hemorrhage:output', pk=new_hemorrhage.pk)
	else:
		form = HemorrhageForm()
	return render(request, 'hemorrhage_identifier/identify_hemorrhage.html',{'form':form})

def output(request,pk):
	hemorrhage = get_object_or_404(Hemorrhage, pk=pk)
	return render(request, 'hemorrhage_identifier/output.html', {'hemorrhage':hemorrhage})