from django.shortcuts import render, redirect
from django.db.models import Count
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
		"playersLopez": Player.objects.filter(last_name__contains="Lopez").filter(curr_team__in=Team.objects.filter(league=League.objects.get(name="American Conference of Amateur Football"))),
		"playersSoccer": Player.objects.filter(curr_team__league__sport__contains="soccer"),
		"playerSof": Team.objects.filter(curr_players__first_name__contains="sofia"),
		#"leagSof": League.objects.filter(teams__curr_players__first_name_contains="sofia"),
		"playerFlor": Player.objects.filter(last_name__contains="Flores").exclude(curr_team__team_name="Roughriders",curr_team__location="Washington"),
		"playerSam": Team.objects.filter(all_players__first_name = "Samuel", all_players__last_name = "Evans"),
		"playerMan": Player.objects.filter(all_teams__team_name = "Tiger-Cats", all_teams__location = "Manitoba"),
		"playerW": Player.objects.filter(all_teams__team_name = "Vikings", all_teams__location = "Wichita").exclude(curr_team__team_name = "Vikings", curr_team__location = "Wichita"),
		"playerJ": Team.objects.filter(all_players__first_name = "Jacob", all_players__last_name = "Gray").exclude(team_name = "Colts", location = "Oregon"),
		"playerJos": Player.objects.filter(first_name = "Joshua", all_teams__league__name = "Atlantic Federation of Amateur Baseball Players"),
		"teams12": Team.objects.annotate(x = Count('all_players')).filter(x__gt=11),
		"players12": Player.objects.annotate(x = Count('all_teams')).order_by('-x')
	}
	#print(context["playersCollBase"])
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")