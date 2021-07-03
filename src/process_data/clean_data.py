import pandas
import numpy
import csv
import copy
import datetime

#constants
K_FACTOR = 15 #k-factor, may change depending on how the data turns out

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



#days array
days = []

raw_data = pandas.read_csv("src/old_processed_data/raw_data.csv")
labels = raw_data.columns

#sort by date
raw_data["date"] = pandas.to_datetime(raw_data.date)
raw_data.sort_values(by='date', inplace=True)



possible_teams = numpy.union1d(raw_data["team"].unique(), raw_data["opponent"].unique())

part_cleaned_df = raw_data.drop(columns=["game_number","year", "day"])
#part_cleaned_df = part_cleaned_df.drop(part_cleaned_df[(part_cleaned_df["team"] == part_cleaned_df["opponent"])].index)

#for testing purposes only
#part_cleaned_df = part_cleaned_df.head(1500)


#create first day, 1980-08-31, and initialize every team's elo to 0
days.append(GameDay(datetime.date(1980, 8, 31)))
for team_name in possible_teams:
    tempTeam = Team(team_name, 1500)
    days[0].addTeam(tempTeam)

#we now iterate over the dataframe.(probably faster to do this another way but we only need to do this once)
for row in part_cleaned_df.itertuples():
    #create new date if doesn't exist
    if days[-1].date != row.date:
        days.append(GameDay(row.date, copy.deepcopy(days[-1].teams)))
    
    #now use new row, and calculate new elo values for the game
    
    #get team_elo from dict, then mutate
    team1 = days[-1].getTeam(row.team)
    team2 = days[-1].getTeam(row.opponent)
    print("Game: " + row.team + " vs " + row.opponent + " " + row.WL)
    print("Team1: " + team1.name + " " + str(team1.elo))
    print("Team2: " + team2.name + " " + str(team2.elo))

    #i don't know why this is switched but
    calc_elo(team1, team2, (0 if row.WL == "W" else 1))
    print("Team1: " + team1.name + " " + str(team1.elo))
    print("Team2: " + team2.name + " " + str(team2.elo))
    
    

#print to csv

with open("src/old_processed_data/cleaned_data.csv", 'w', newline='') as file:
    columns = possible_teams
    file.write("\"date\",")
    for team in possible_teams:
        file.write("\"" + team + "\"\n") if team == possible_teams[-1] else file.write("\"" + team + "\"" + ",")
    
    for day in days:
        file.write( "\"" + day.date.strftime("%m/%d/%Y") + "\",")
        for team in possible_teams:
            file.write("\"" + str(day.getTeam(team).elo) + "\"\n") if team == possible_teams[-1] else file.write("\"" + str(day.getTeam(team).elo) + "\",")


