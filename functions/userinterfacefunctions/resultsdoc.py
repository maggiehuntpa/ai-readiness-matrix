from distutils import log
#from wkhtmltopdf import wkhtmltopdf

class ResultsDoc():

    
    def create_results_pdf(url, uid):

        results_pdf = "hi" #wkhtmltopdf(url=url, output_file=f'PA_Consulting_AI_Readiness_Matrix_Results_{uid}.pdf')
        log(uid, " PDF generated")
        return results_pdf
    
    def download_report(results_pdf):
        print(results_pdf)
        return "ok" #todo
    

    #todo: add email functionality