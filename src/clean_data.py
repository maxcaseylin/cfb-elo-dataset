import pandas
import csv

import pandas
import numpy
import csv
import copy
import datetime

#constants
K_FACTOR = 40 #k-factor, may change depending on how the data turns out

class Team:
    def __init__(self, name, elo):
        self.elo = elo
        self.name = name

class GameDay:
    def __init__(self, date, teams={}):
        #key: team name(str), team(class)
        self.teams = teams
        self.date = date
    
    def addTeam(self, team):
        self.teams[team.name] = team

    def getTeam(self, team_name):
        return self.teams[team_name]

#calculates the elo change between 2 teams. winteam is either 0(team1) or 1(team2).
def calc_elo(team1, team2, winteam):
    
    org_elo1 = team1.elo
    org_elo2 = team2.elo

    ex_score2 = 1 / (1 + (10 ** ((team1.elo - team2.elo) / 400)))
    ex_score1 = 1 / (1 + (10 ** ((team2.elo - team1.elo) / 400)))

    potelo1 = team1.elo + (K_FACTOR * (((1 if winteam == 0 else 0)) - ex_score1))
    potelo2 = team2.elo + (K_FACTOR * (((1 if winteam == 1 else 0)) - ex_score2))

    team1.elo = potelo1 if potelo1 > 100 else 100
    team2.elo = potelo2 if potelo2 > 100 else 100

team1 = Team("Wisconsin", 2400)
team2 = Team("Indiana", 1500)
calc_elo(team1, team2, 1)
print(team1.elo)