from flask import Flask, render_template
from yfpy.query import YahooFantasySportsQuery


from configurations import CLIENT_ID, CLIENT_SECRET, PATH
from declarations import Team, RAVINE_RUMBLE, GAME_CODE
from prediction import predict_winner

# documentation: https://github.com/uberfastman/yfpy
QUERY_ENGINE = YahooFantasySportsQuery(
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
    nan = QUERY_ENGINE.get_team_stats_by_week(Team.NAN.value, 15)
    paul = QUERY_ENGINE.get_team_stats_by_week(Team.PAUL.value, 15)
    tim = QUERY_ENGINE.get_team_stats_by_week(Team.TIM.value, 15)
    tyler = QUERY_ENGINE.get_team_stats_by_week(Team.TYLER.value, 15)

    nan_prob, paul_prob = predict_winner(nan, paul)
    tim_prob, tyler_prob = predict_winner(tim, tyler)

    return render_template(
        'losers.html',
        nan=nan, paul=paul, tim=tim, tyler=tyler,
        nan_prob=nan_prob, paul_prob=paul_prob, tim_prob=tim_prob, tyler_prob=tyler_prob
    )
