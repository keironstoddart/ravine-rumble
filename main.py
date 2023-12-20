from flask import Flask, render_template
from yfpy.query import YahooFantasySportsQuery


from configurations import CLIENT_ID, CLIENT_SECRET, PATH
from declarations import Team, RAVINE_RUMBLE, GAME_CODE


app = Flask(__name__)


@app.route('/')
def home():
    # documentation: https://github.com/uberfastman/yfpy
    query_engine = YahooFantasySportsQuery(
        PATH,
        RAVINE_RUMBLE,
        GAME_CODE,
        game_id=423,
        offline=False,
        all_output_as_json_str=False,
        consumer_key=CLIENT_ID,
        consumer_secret=CLIENT_SECRET,
    )

    brett = query_engine.get_team_stats_by_week(Team.BRETT.value, 16)
    paul = query_engine.get_team_stats_by_week(Team.PAUL.value, 16)
    wonjoon = query_engine.get_team_stats_by_week(Team.WONJOON.value, 16)
    tyler = query_engine.get_team_stats_by_week(Team.TYLER.value, 16)

    return render_template(
        'losers.html',
        brett=brett, paul=paul, wonjoon=wonjoon, tyler=tyler,
    )
