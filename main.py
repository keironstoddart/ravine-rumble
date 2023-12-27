from random import choice

from flask import Flask, render_template
from yfpy.query import YahooFantasySportsQuery


from configurations import CLIENT_ID, CLIENT_SECRET, PATH
from declarations import Team, RAVINE_RUMBLE, GAME_CODE


app = Flask(__name__)
GIFS = [
    'https://giphy.com/embed/vFhdC60CFCwgAUTQ6i',
    'https://giphy.com/embed/nEuNUZP8rX9YyDMVud',
    'https://giphy.com/embed/3ohc0Y2TA2KJRO66m4',
    'https://giphy.com/embed/l57gbvjm8xU5uVSDnx',
    'https://giphy.com/embed/3orieZBr6Oh8YmeR56',
    'https://giphy.com/embed/0Q2Idjtt38WLwrLGnO',
    'https://giphy.com/embed/jO1ZyDgmy9IBqFzPPm',
]


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

    paul = query_engine.get_team_stats_by_week(Team.PAUL.value, 17)
    tyler = query_engine.get_team_stats_by_week(Team.TYLER.value, 17)

    return render_template(
        'losers.html',
        paul=paul, tyler=tyler, gif=choice(GIFS)
    )
