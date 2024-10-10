from statistics import mean
from functions.datafunctions.database_pull import DatabasePull as db

class Scoring():

    def average_score(scores):
        average_score = float(mean(scores)*10)
        if average_score >= 75:
            overall_message = "You are ready to build your AI solution! Get in touch and we can support you to develop and deploy!"
        else: 
            overall_message = "You are not ready to build your AI solution! Get in touch and we can support you to develop and deploy!"
       
        return average_score, overall_message

    def average_score_organization(scores):
        organization_scores = scores[:len(scores)//2]
        average_score_organization = float(mean(organization_scores)*10)
        if average_score_organization >= 75:
            overall_message_organization = "Your organization is ready for AI! Get in touch and we can support you to develop and deploy!"
        else: 
            overall_message_organization = "Your organization is not quite ready for AI! Get in touch and we can support you to train skills and manage change!"
        
        return average_score_organization, overall_message_organization

    def average_score_solution(scores):
        solution_scores = scores[len(scores)//2:]
        average_score_solution = float(mean(solution_scores)*10)
        if average_score_solution >= 75:
            overall_message_solution = "Your solution is a great fit for AI! Get in touch and we can support you to develop and deploy!"
        else: 
            overall_message_solution = "Your solution is not a good fit for AI yet. Get in touch and we can help you develop your idea and bring it to life!"
        
        return average_score_solution, overall_message_solution
    
    def worst_question(scores):
        worst_score_q = scores.index(min(scores))+1
        worst_score_q_no_str = str(worst_score_q) 
        worst_score_q_desc_str = str(db.pull_questions()[worst_score_q][1])
        
        return worst_score_q_no_str, worst_score_q_desc_str
    
    def best_question(scores):
        best_score_q = scores.index(max(scores))+1
        best_score_q_no_str = str(best_score_q) 
        best_score_q_desc_str = str(db.pull_questions()[best_score_q][1])
        return best_score_q_no_str, best_score_q_desc_str
    
    def experts(scores):
        #todo - add - 'lead' is for soution and org; also append topics
        worst_question = Scoring.worst_question(scores)[0]
        experts = db.pull_topic_contacts(worst_question)
        experts[0] = experts[0].title()
        # topic = experts[0]
        # leader = experts[1]
        # supporter = experts[2]
        
        return experts