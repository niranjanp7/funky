from django.contrib import messages
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        firstName = request.POST["firstName"].title()
        lastName = request.POST["lastName"].title()
        password = request.POST["password"]
        newUser = User.objects.create_user(username, None, password)
        newUser.first_name = firstName
        newUser.last_name = lastName
        newUser.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("userprofile")
        return redirect("/")

    else:
        return redirect("/")


def userlogin(request):
    if request.method == "POST":
        user = authenticate(username=request.POST["lusername"], password=request.POST["lpassword"])
        if user is not None:
            login(request, user)
            return redirect("userprofile")
        return redirect("/")


def userlogout(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "You have LogOut Successfully")
        return redirect("userprofile")
    return redirect("/")


def userprofile(request):
    return render(request, "userprofile/userprofile.html")
