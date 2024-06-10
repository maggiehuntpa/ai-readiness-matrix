from unittest import TestCase, assertEqual

from flask.functions.userfunctions.scoring import average_score, average_score_organization, average_score_solution


class TestScoring(TestCase):

    def test_score_averages():
        scores = test_score()
        print(scores)
        assertEqual(average_score(scores), 4.2)
        assertEqual(average_score_organization(scores), 5.2)
        assertEqual( average_score_solution(scores), 3.2)


def test_score():
    scores = [2,6,7,3,8,2,0,1,4,9]
    return scores
