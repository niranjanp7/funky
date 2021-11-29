from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Game


def game_list(request):
    return render(request, "games/index.html", {"game_play": False, "game": Game.objects.all()})


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
        },
    )
