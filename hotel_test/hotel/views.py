from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    if request.method == "POST":
        a = request.POST.get("startDate", "")
        b = request.POST.get("finishDate", "")
        print(a, b)
        return redirect("/booking",)
    return render(request, "hotel/index.html")


def restaurant(request):
    return render(request, "hotel/restaurant-page.html")
