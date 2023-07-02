from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def admin(request):
    return render(request, "users/admin.html")


def user(request):
    return render(request, "users/user.html")
