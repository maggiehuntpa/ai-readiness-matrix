import plotly.graph_objects as go
from ..datafunctions.database_pull import DatabasePull as db

class DataVisualisaton():

    def plot_chart(scores):
        fig = go.Figure()
        categories = db.pull_topics()
        blanks = [0,0,0,0,0]


        organization_scores = scores[:len(scores)//2]
        solution_scores = scores[len(scores)//2:]


        fig.add_trace(go.Scatterpolar(
            r=scores,
            theta=categories,
            fill='tonext',
            name='Score',
            hoverinfo='none'
        ))

        
        fig.update_layout(
        polar=dict(
            radialaxis=dict(
            visible=True,
            range=[0, 10]
            )),
        showlegend=False
        )

        graph = fig.to_html(full_html=False)

        return graph