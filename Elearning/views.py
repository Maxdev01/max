from django.shortcuts import render

def confidentialite(request):
	return render(request, "confidentialite.html", {})

def dashboard(request):
    return render(request, "dashboard.html")

def donate(request):
    	return render(request, "donate.html")


def cours(request):
    	return render(request, "nos-cours.html")

""" voici le views des cours de developement personel """ 
def courss(request):
    	return render(request, "dev-personel.html")

""" voici le view du cours de gestion de conflit """
def cours2(request):
	return render(request, "cours-gestion-de-conflit.html")