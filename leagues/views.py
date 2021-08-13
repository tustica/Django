from django.shortcuts import render, redirect
from .models import League, Team, Player
from . import team_maker
import leagues
from django.db.models import Count

def index(request):
	context = {
		"leagues": League.objects.all(),
		"baseball_leagues": League.objects.filter(sport="Baseball"),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"dallas_teams": Team.objects.filter(location = "Dallas"),
		"penguins" : Team.objects.get(team_name = "Penguins"),
		"football_leagues": League.objects.filter(sport = "Football"),
		"count_of_players": Team.objects.annotate(Count('all_players')),
		"count_of_teams": Player.objects.annotate(countnum = Count('all_teams'))
		
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")