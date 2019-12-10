from django.shortcuts import render, redirect
from .models import Blogpost, Books, Contact, DeliveryDetails
from django.contrib import messages


def index(request):
    books = Books.objects.all()
    return render(request, "home.html", {'books': books})


def newarrivals(request):
    return render(request, 'newarrivals.html')


def contactus(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        messages.info(request, 'Thanks for your feedback')
        return redirect('contactus')
    else:
        return render(request, 'contactus.html')


def blog(request):
    blogs = Blogpost.objects.all()

    return render(request, "blog.html", {'blogs': blogs})


def quickview(request, myid):
    # fetch the product using id
    product = Books.objects.filter(id=myid)
    return render(request, "quickview.html", {'product': product[0]})


def search(request):
    if request.method == 'POST':
        searched_book = request.POST['searched_book']
        results = Books.objects.filter(Title=searched_book)
        return render(request, 'search.html', {'results': results})
    else:
        results = Books.objects.filter()
        return render(request, 'search.html', {'results': results})


def deliverydetails(request):
    if request.method == "POST":
        name = request.user.first_name
        phone = request.POST['phone']
        email = request.user.email
        pincode = request.POST['pincode']
        house_no = request.POST['house_no']
        area = request.POST['area']
        landmark = request.POST['landmark']
        city = request.POST['city']
        state = request.POST['state']
        details = DeliveryDetails(name=name, phone=phone, email=email, pincode=pincode, house_no=house_no, area=area, landmark=landmark, city=city, state=state)
        details.save()
        return redirect('thankyou')
    else:
        return render(request, 'deliverydetails.html')


def thankyou(request):
    return render(request, 'thankyou.html')


