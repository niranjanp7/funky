from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404
from .models import Game
from django.contrib import messages
from userauth.views import getLevels


def game_list(request):
    if request.user.is_authenticated:
        level, levels = getLevels(request)
        return render(request, "games/index.html", {"game_play": False, "game": Game.objects.all(), "level": level})
    messages.error(request, "Please Login First")
    return redirect("home")


def game(request, game_id):
    try:
        Game.objects.get(id=game_id + 1)
        next_game = game_id + 1
    except Game.DoesNotExist:
        next_game = 0
    try:
        g = Game.objects.get(id=game_id)
    except Game.DoesNotExist:
        raise Http404(">>>Game Level not created!<<<")
    if request.user.is_authenticated:
        level, levels = getLevels(request)
        if game_id > level + 1:
            messages.error(
                request,
                "GameLevelERROR : You are not elligible for this level. Please clear level "
                + str(level + 1)
                + " first.",
            )
            return redirect("game_list")
        return render(
            request,
            "levels/" + str(g.html_file),
            {
                "game_play": True,
                "next_game": next_game,
                "game_id": g.id,
                "game_name": g.game_name,
                "html_file": g.html_file,
                "game": Game.objects.all(),
                "level": level,
            },
        )
    messages.error(request, "Please Login First")
    return redirect("home")
