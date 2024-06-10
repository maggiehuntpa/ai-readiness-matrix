from statistics import mean

class Scoring():

    def average_score(scores):
        average_score = mean(scores)
        return average_score

    def average_score_organization(scores):
        organization_scores = scores[:len(scores)//2]
        average_score_organization = mean(organization_scores)
        return average_score_organization

    def average_score_solution(scores):
        solution_scores = scores[len(scores)//2:]
        average_score_solution = mean(solution_scores)
        return average_score_solution