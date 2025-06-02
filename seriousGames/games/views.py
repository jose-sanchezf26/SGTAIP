from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# Create your views here.

@login_required
def game_selection(request):
    games = ["SurvivalRules", "WildAI"]  # Puedes obtener esto de la base de datos
    return render(request, 'game_selection.html', {'games': games})

def play_game(request, game_name):
     return render(request, "game_template.html", {"game_name": game_name, "username": request.user.username})
