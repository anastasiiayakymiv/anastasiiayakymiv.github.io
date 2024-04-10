from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "hotel/index.html")


def restaurant(request):
    return render(request, "hotel/restaurant-page.html")
