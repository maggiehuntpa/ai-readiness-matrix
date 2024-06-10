import plotly.graph_objects as go

class DataVisualisaton():

    def plot_chart(scores):
        fig = go.Figure()
        categories = ['1','2', '3', '4', '5', '6', '7', '8', '9', '10']


        organization_scores = scores[:len(scores)//2]
        solution_scores = scores[len(scores)//2:]


        fig.add_trace(go.Scatterpolar(
            r=organization_scores,
            theta=categories,
            fill='toself',
            name='Organizational Readiness'
        ))

       
        fig.add_trace(go.Scatterpolar(
        r=solution_scores,
        theta=categories,
        fill='toself',
        name='Solution Readiness'
    ))
        
        fig.update_layout(
        polar=dict(
            radialaxis=dict(
            visible=True,
            range=[0, 10]
            )),
        showlegend=False
        )

        graph = fig.to_html()

        return graph