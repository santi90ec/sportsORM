from django.shortcuts import render, redirect
from .models import League, Team, Player
from . import team_maker
import leagues

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"leaguesB": League.objects.filter(sport__contains="baseball"),
		"leaguesW": League.objects.filter(name__contains="women"),
		"leaguesH": League.objects.filter(sport__contains="Hockey"),
		"leaguesNotF": League.objects.exclude(sport="football"),
		"leaguesConf": League.objects.filter(name__contains="conference"),
		"leagueAtl": League.objects.filter(name__contains="atlantic"),
		"teamD": Team.objects.filter(location__contains="dallas"),
		"teamR": Team.objects.filter(team_name__contains="raptors"),
		"teamC": Team.objects.filter(location__contains="city"),
		"teamT": Team.objects.filter(team_name__startswith="t"),
		"teamAl":Team.objects.order_by("team_name"),
		"teamRe": Team.objects.order_by("-team_name"),
		"playersC": Player.objects.filter(last_name__contains="cooper"),
		"playersJ": Player.objects.filter(first_name__contains="joshua"),
		"playersCop": Player.objects.filter(last_name__contains="cooper" ).exclude(first_name__contains="joshua"),
		"playersAW": Player.objects.filter(first_name__contains="wyatt"),
		"playersAL": Player.objects.filter(first_name__contains="alexander")
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")