from django.shortcuts import render
from .forms import FbForm
from .models import FbModel

def home(request):
	if request.method == "POST":
		na = request.POST.get("name")
		fb = request.POST.get("feedback")
		d = FbModel(name=na, feedback=fb)
		d.save()
		fm = FbForm()
		return render(request,"home.html",{"fm":fm,"msg":"thanks for the feedback"})
	else:
		fm = FbForm()
		return render(request,"home.html",{"fm":fm})