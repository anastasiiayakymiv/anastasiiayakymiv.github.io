from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get("nameinput", "")
        phone = request.POST.get("phoneinput", "")
        feedback = request.POST.get("feedbackinput", "")
        print(name, phone, feedback)
    return render(request, "hotel/index.html")

def restaurant(request):
    if request.method == "POST":
        name = request.POST.get("rest-reserv-name", "")
        phone = request.POST.get("rest-reserv-phone", "")
        time = request.POST.get("rest-reserve-time", "")
        date = request.POST.get("rest-reserv-date", "")
        guests = request.POST.get("rest-reserv-guest", "")
        additionally = request.POST.get("rest-reserv-additionally", "")
        print(name, phone, time, date, guests, additionally)
    return render(request, "hotel/restaurant-page.html")    

def conferencehall(request):
    if request.method == "POST":
        name = request.POST.get("reservation-name", "")
        phone = request.POST.get("reservation-number", "")
        time = request.POST.get("reserv-time", "")
        date = request.POST.get("reserv-date", "")
        guests = request.POST.get("reserv-guest", "")
        additionally = request.POST.get("reserv-additionally", "")
        print(name, phone, time, date, guests, additionally)
    return render(request, "hotel/conferencehall-page.html")

def rooms(request):
    return render(request, "hotel/rooms.html")

def booking(request):
    if request.method == "POST":
        first_name = request.POST.get("customer-firstname", "")
        last_name = request.POST.get("customer-lastname", "")
        phone = request.POST.get("customer-phone", "")
        email = request.POST.get("customer-email", "")
        check_in = request.POST.get("checkin-date", "")
        check_out = request.POST.get("checkout-date", "")
        adults_amount = request.POST.get("adult-amount", "")
        children_amount = request.POST.get("children-amount", "")
        room_type = request.POST.get("room-type", "")
        comment = request.POST.get("customer-comment", "")
        print(first_name, last_name, phone, email, check_in, check_out, adults_amount, children_amount, room_type, comment)
        #зробили перевірку(Select зайнятих номерів, якщо є вільний номер - повертаємо повідомлення
        #бронювання успішне", якщо нема - "Нажаль всі номери обраного класу зайняті")
        #якщо успіх - записуємо в БД,якщо ні - повертаємо користувача на сторінку бронювання
    return render(request, "hotel/booking.html")

def superiortwin(request):
    return render(request, "hotel/rooms-page1.html")

def standartdeluxe(request):
    return render(request, "hotel/rooms-page2.html")

def presidentialsuite(request):
    return render(request, "hotel/rooms-page3.html")

def premiersuite(request):
    return render(request, "hotel/rooms-page4.html")