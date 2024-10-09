from google.cloud import bigquery
client = bigquery.Client()

class DatabasePull():
    def pull_questions():
        question_query_SQL = "SELECT * FROM `ai-readiness-matrix.matrixdata.questions`"
        question_query_job = client.query(question_query_SQL)
        question_results = question_query_job.result()
        question_dict = {}
        for q in question_results:
            question_dict[q[0]] = [q[1], q[2], q[3], q[4], q[5]]

        return question_dict
    

    def pull_experts():

        expert_query_SQL = "SELECT * FROM `ai-readiness-matrix.matrixdata.experts`"
        expert_query_job = client.query(expert_query_SQL)
        expert_results=expert_query_job.result()
        experts_dict = {}
        for e in expert_results:
            experts_dict[e[0]] = [e[1], e[2], e[3], e[4], e[5]]

        return experts_dict
    
    def pull_topic_contacts(weakest_q):
        experts_dict = DatabasePull.pull_experts()
        topics_query_SQL = "SELECT * FROM `ai-readiness-matrix.matrixdata.topics`"
        topics_query_job = client.query(topics_query_SQL)
        topics_results = topics_query_job.result()
        topics_dict_unsorted = {}
        for t in topics_results:
            topics_dict_unsorted[str(t[0])] = [t[1], experts_dict[t[2]], experts_dict[t[3]]]
        topics_dict = dict(sorted(topics_dict_unsorted.items()))
        topic_contacts = topics_dict[weakest_q]
   
        return topic_contacts