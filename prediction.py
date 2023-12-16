from random import normalvariate
from typing import List, Tuple

from yfpy import TeamPoints, TeamProjectedPoints

Total = float
Projection = float
Points = Tuple[Total, Projection]


def _simulate_final_result(points: Points, iterations: int) -> List[float]:
    total, projection = points

    standard_deviate = (projection - total) / 2
    return [normalvariate(projection, standard_deviate) for _ in range(iterations)]


AProbability = float
BProbability = float


def _predict(points_a: Points, points_b: Points, iterations: int) -> Tuple[AProbability, BProbability]:
    pred_result_a = _simulate_final_result(points_a, iterations)
    pred_result_b = _simulate_final_result(points_b, iterations)

    a_wins = sum(1 for a, b in zip(pred_result_a, pred_result_b) if a > b)
    return a_wins / iterations, 1 - a_wins / iterations


def predict_winner(
        team_a:  dict[str, TeamPoints | TeamProjectedPoints],
        team_b: dict[str, TeamPoints | TeamProjectedPoints]
) -> Tuple[AProbability, BProbability]:
    team_a_points = team_a['team_points'].total, team_a['team_projected_points'].total
    team_b_points = team_b['team_points'].total, team_b['team_projected_points'].total

    return _predict(team_a_points, team_b_points, 10_000)


def main():
    a = 50, 121.64
    b = 50, 108.71
    print(predict_winner(a, b, 10_000))


if __name__ == '__main__':
    main()
