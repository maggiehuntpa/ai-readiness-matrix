#todo: pull questions from db

class DatabasePull():
    def pull_questions():
        #pull questions, 0 and 10 from db
        questions_and_info = {
            "q1" : {
                "Questiontext": "text",
                "0" : "0text",
                "10": "10text",
                "theme" : "Culture"

        } #etc
        }
        return questions_and_info
    

    def pull_experts():
        
        experts ={"Fullname": {
            "email" : "x@PA.com",
            "role" : "Partner, FS",
            "specialist themes" : ["culture", "budget"],
            "bio" : "xyz" #etc
        }}

        return experts