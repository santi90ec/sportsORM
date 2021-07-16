from django.shortcuts import render, redirect
from .models import League, Team, Player
from . import team_maker
import leagues

def index(request):
	obj=League.objects.get(name="American Conference of Amateur Football")
	teamsL=Team.objects.filter(league=obj)
	Lop=Player.objects.filter(curr_team__in=teamsL)
	#Player.objects.filter(first_name__contains="Lopez").filter(curr_team=Team.objects.filter(league=))
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
		"playersAL": Player.objects.filter(first_name__contains="alexander"),
		"teamSoc": Team.objects.filter(league=League.objects.get(name__contains="atlantic soccer")),
		"playersBoston": Player.objects.filter(curr_team=Team.objects.get(team_name__contains="Penguins")),
		"playersCollBase": Player.objects.filter(curr_team=Team.objects.filter(league=2)),
		"playersLopez": Player.objects.filter(last_name__contains="Lopez").filter(curr_team__in=Team.objects.filter(league=League.objects.get(name="American Conference of Amateur Football")))


	}
	#print(context["playersCollBase"])
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")