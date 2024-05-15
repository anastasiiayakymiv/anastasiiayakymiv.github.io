from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get("customer-firstname", "")
        last_name = request.POST.get("customer-lastname", "")
        #зробили перевірку(Select зайнятих номерів, якщо є вільний номер - повертаємо повідомлення
        #бронювання успішне", якщо нема - "Нажаль всі номери обраного класу зайняті")
        #якщо успіх - записуємо в БД,якщо ні - повертаємо користувача на сторінку бронювання
    return render(request, "hotel/index.html")

def restaurant(request):
    return render(request, "hotel/restaurant-page.html")

def conferencehall(request):
    return render(request, "hotel/conferencehall-page.html")

def rooms(request):
    return render(request, "hotel/rooms.html")

def booking(request):
    return render(request, "hotel/booking.html")

def superiortwin(request):
    return render(request, "hotel/rooms-page1.html")

def standartdeluxe(request):
    return render(request, "hotel/rooms-page2.html")

def presidentialsuite(request):
    return render(request, "hotel/rooms-page3.html")

def premiersuite(request):
    return render(request, "hotel/rooms-page4.html")
