from statistics import mean
from functions.datafunctions.database_pull import DatabasePull as db

class Scoring():

    def average_score(scores):
        average_score = round(mean(scores)*10)
        if average_score >= 75:
            overall_message = "You are ready to build your AI solution! Get in touch and we can support you to develop and deploy!"
        else: 
            overall_message = "You are not ready to build your AI solution! Get in touch and we can support you to develop and deploy!"
       
        return average_score, overall_message

    def average_score_organization(scores):
        organization_scores = scores[:len(scores)//2]
        average_score_organization = round(mean(organization_scores)*10)
        if average_score_organization >= 75:
            overall_message_organization = "Your organization is ready for AI! Get in touch and we can support you to develop and deploy!"
        else: 
            overall_message_organization = "Your organization is not quite ready for AI! Get in touch and we can support you to train skills and manage change!"
        
        return average_score_organization, overall_message_organization

    def average_score_solution(scores):
        solution_scores = scores[len(scores)//2:]
        average_score_solution = round(mean(solution_scores)*10)
        if average_score_solution >= 75:
            overall_message_solution = "Your solution is a great fit for AI! Get in touch and we can support you to develop and deploy!"
        else: 
            overall_message_solution = "Your solution is not a good fit for AI yet. Get in touch and we can help you develop your idea and bring it to life!"
        
        return average_score_solution, overall_message_solution
    
    def get_in_touch():
        #todo - top 2 experts for lowest scores, add to content
       
        experts = db.pull_experts()

        get_in_touch = f'contact us! maggie.hunt@paconsulting.com and {experts}'

        return get_in_touch