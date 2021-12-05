from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from .models import Level
from games.models import Game
from django.http import HttpResponse


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        firstName = request.POST["firstName"].title()
        lastName = request.POST["lastName"].title()
        password = request.POST["password"]
        try:
            newUser = User.objects.create_user(username, None, password)
            newUser.first_name = firstName
            newUser.last_name = lastName
            newUser.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                levelAssign(request, user)
                login(request, user)
                messages.success(request, "Welcome " + firstName)
                return redirect("userprofile")
        except:
            messages.error(
                request, 'SignUpERROR : Username "' + username + '" has allready been taken. Please enter another one'
            )
        return redirect("/")

    else:
        return redirect("/")


def userlogin(request):
    if request.method == "POST":
        user = authenticate(username=request.POST["lusername"], password=request.POST["lpassword"])
        if user is not None:
            login(request, user)
            return redirect("/")
        messages.error(request, "LogInERROR : Wrong Username or Password")
        return redirect("/")


def userlogout(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "You have LoggedOut Successfully")
        return redirect("home")
    else:
        messages.error(request, "LogOutERROR : Something went wrong")
        return redirect("home")


def userprofile(request):
    if request.user.is_authenticated:
        level, levels = getLevels(request)
        return render(
            request,
            "userprofile/userprofile.html",
            {"levels": levels[:level], "level": level, "next": True if len(levels) > level else False},
        )
    messages.error(request, "Please LogIn first")
    return redirect("home")


def levelAssign(request, user):
    if request.method == "POST":
        levels = Level(user=user)
        levels.save()


def getLevels(request):
    level = Level.objects.filter(user=request.user)[0].levels
    levels = Game.objects.all()
    return level, levels


def levelCleared(request):
    if request.method == "POST":
        game_id = request.POST["currentLevel"]
        level = Level.objects.filter(user=request.user)[0]
        if level.levels + 1 == int(game_id):
            level.levels = game_id
            level.save()
        return HttpResponse(status=204)
    messages.error(request, "CheatEROOR : You are cheating!")
    return redirect("home")
