import dash
from dash import html, dcc, Input, Output, State
from transformers import BertForSequenceClassification, BertTokenizer
import torch
import os
import torch.nn.functional as F
import plotly.graph_objs as go
from transformers import pipeline

classifier = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-sentiment-latest", return_all_scores=True)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

label_map = {0: "Negative", 1: "Positive"}

dash.register_page(__name__, path='/sentiment')

layout = html.Div([
    html.H1('Sentiment Analysis', className="mb-4"),

    html.Div([
        html.Label("Enter text to analyze sentiment:", className="form-label"),
        
        dcc.Textarea(
            id='sentiment-input',
            placeholder='Type your sentence here...',
            style={'width': '100%', 'height': 150},
            className="form-control mb-3"
        ),

        html.Div([
            html.Button('Analyze', id='submit-button', n_clicks=0, className="btn btn-warning me-2"),
            html.Button('Clear', id='clear-button', n_clicks=0, className="btn btn-secondary")
        ], className="mb-4"),

        html.Div(id='sentiment-result', className="mt-3 fw-bold"),
        dcc.Graph(id='probability-bar', className="mt-4", style={'display': 'none'})
    ], className="bg-dark p-4 rounded", style={"maxWidth": "700px", "margin": "0 auto"})
])


@dash.callback(
    Output('sentiment-input', 'value'),
    Output('sentiment-result', 'children'),
    Output('probability-bar', 'figure'),
    Output('probability-bar', 'style'),
    Input('submit-button', 'n_clicks'),
    Input('clear-button', 'n_clicks'),
    State('sentiment-input', 'value'),
    prevent_initial_call=True
)
def handle_sentiment(submit_clicks, clear_clicks, text):
    ctx = dash.callback_context

    if not ctx.triggered:
        raise dash.exceptions.PreventUpdate

    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if trigger_id == 'clear-button':
        return "", "", go.Figure(), {'display': 'none'}

    if not text:
        return text, "", go.Figure(), {'display': 'none'}

    # Analyze text
    outputs = classifier(text)[0]
    scores = {output['label']: output['score'] for output in outputs}
    # print(scores)

    neg = scores.get('negative', 0)
    neu = scores.get('neutral', 0)
    pos = scores.get('positive', 0)

    # Normalize for only negative and positive
    total = neg + pos
    if total == 0:
        neg_norm = pos_norm = 0.5  # Avoid division by zero
    else:
        neg_norm = neg / total
        pos_norm = pos / total

    # Determine final label based on normalized scores
    if pos_norm >= neg_norm:
        final_label = "Positive"
        confidence = pos_norm
    else:
        final_label = "Negative"
        confidence = neg_norm

    result_text = f"Predicted Sentiment: {final_label}"

    fig = go.Figure(data=[
        go.Bar(
            x=["Negative", "Positive"],
            y=[neg_norm, pos_norm],
            marker_color=["crimson", "green"]
        )
    ])
    fig.update_layout(
        title="Sentiment Probabilities",
        yaxis=dict(title="Probability", range=[0, 1]),
        xaxis=dict(title="Sentiment"),
        plot_bgcolor="#1e1e1e",
        paper_bgcolor="#1e1e1e",
        font=dict(color="white")
    )

    return text, result_text, fig, {'display': 'block'}



