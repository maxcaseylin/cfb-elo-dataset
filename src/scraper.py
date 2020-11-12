import CFBScrapy as cfb
import pandas
import csv
import numpy

t = pandas.DataFrame()
for i in range(1980, 2019):
    t = t.append(cfb.get_game_info(year=i, conference="B1G", seasonType="regular"))

t.drop(columns=["start_time_tbd", "neutral_site", "conference_game", "attendance", "venue_id", "venue", "home_post_win_prob", "away_post_win_prob", "home_id", "id", "week", "season_type", "excitement_index", "home_line_scores", "away_line_scores"], inplace=True)
t.to_csv("src/raw_data.csv")

print(t.head(10).iloc[-1]["home_team"])