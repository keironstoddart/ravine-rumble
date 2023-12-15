"""
Example public Yahoo league URL: "https://archive.fantasysports.yahoo.com/nfl/2014/729259"

Example vars using public Yahoo leagues still require auth through a personal Yahoo account: see README.md

yfpy Resource: https://github.com/uberfastman/yfpy/blob/main/quickstart/quickstart.pyL
"""

from flask import Flask, render_template
from yfpy.query import YahooFantasySportsQuery


from configurations import CLIENT_ID, CLIENT_SECRET, PATH
from declarations import Team, RAVINE_RUMBLE, GAME_CODE


yahoo_query = YahooFantasySportsQuery(
    PATH,
    RAVINE_RUMBLE,
    GAME_CODE,
    game_id=423,
    offline=False,
    all_output_as_json_str=False,
    consumer_key=CLIENT_ID,
    consumer_secret=CLIENT_SECRET,
)


app = Flask(__name__)


@app.route('/')
def home():
    nan = yahoo_query.get_team_stats_by_week(Team.NAN.value, 15)
    paul = yahoo_query.get_team_stats_by_week(Team.PAUL.value, 15)
    tim = yahoo_query.get_team_stats_by_week(Team.TIM.value, 15)
    tyler = yahoo_query.get_team_stats_by_week(Team.TYLER.value, 15)

    return render_template('losers.html', nan=nan, paul=paul, tim=tim, tyler=tyler)
