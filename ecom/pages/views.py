from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request,*args, **kwargs):
    return render(request, "home.html", {})
    print(request.user)
def contact_view(request,*args, **kwargs):
    return render(request, "contact.html", {})
def about_view(request,*args, **kwargs):
    return render(request, "about.html", {})
def cart_view(request,*args, **kwargs):
    my_context = {
        "my_name" : "Aman",
        "my_class": 12,
        "my_friends": ["Ankit","Tushar","Sudhir","Kautilya","Abhishek","Suraj"]
    }
    return render(request, "cart.html", my_context)
