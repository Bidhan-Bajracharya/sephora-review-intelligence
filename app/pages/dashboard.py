import dash
from dash import html

dash.register_page(__name__, path='/dashboard')

layout = html.Div([
    html.Div([
        html.Iframe(
            title="sephora",
            src="https://app.powerbi.com/view?r=eyJrIjoiNGJhYjQ2ZWUtMjQ2ZC00ZTlkLTg2MjMtY2UwOWI1ZTZiNDRhIiwidCI6Ijk5ZWViMDA5LWU3YTItNDdiNi05ZGVkLTAyOGNkY2MzMDBlNiIsImMiOjEwfQ%3D%3D&pageName=0aea0f17ea6080e59100",
            style={
                "width": "100%",
                "height": "100%",
                "minHeight": "80vh",  # Adjust this as needed
                "border": "none"
            },
            # allowFullScreen=True
        )
    ], style={"width": "100%", "height": "100%"})
])

# <iframe title="sephora" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiNGJhYjQ2ZWUtMjQ2ZC00ZTlkLTg2MjMtY2UwOWI1ZTZiNDRhIiwidCI6Ijk5ZWViMDA5LWU3YTItNDdiNi05ZGVkLTAyOGNkY2MzMDBlNiIsImMiOjEwfQ%3D%3D&pageName=0aea0f17ea6080e59100" frameborder="0" allowFullScreen="true"></iframe>
