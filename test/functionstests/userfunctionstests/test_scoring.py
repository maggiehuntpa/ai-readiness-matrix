from unittest import TestCase
from functions.userinterfacefunctions.scoring import average_score, average_score_organization, average_score_solution


class TestScoring(TestCase):

    def test_score_averages(self):
        scores = test_score()

        self.assertEqual(average_score(scores), 4.2)
        self.assertEqual(average_score_organization(scores), 5.2)
        self.assertEqual(average_score_solution(scores), 3.2)

def test_score():
    test_score = [2,6,7,3,8,2,0,1,4,9]
    return test_score
