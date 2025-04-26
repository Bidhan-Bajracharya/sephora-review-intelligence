import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/", name="Home")

layout = html.Div([
    # Top-right Sign Out button
    dbc.Row([
        dbc.Col([
            html.Div([
                dbc.Button(
                    "Sign Out",
                    id="home-login-button",
                    color="light",
                    href="/login",
                    className="float-end home-login-button",
                    style={
                        "backgroundColor": "transparent",
                        "border": "1px solid #f7a62c",
                        "color": "#f7a62c",
                        "fontWeight": "bold",
                        "transition": "all 0.3s ease"
                    }
                ),
            ], className="p-3")
        ])
    ]),

    # Center Content (Card)
    dbc.Row([
        dbc.Col([
            html.Div([
                html.H1(
                    "Welcome to Sephora Insights",
                    className="text-center mb-4 sephora-heading",
                    style={"fontWeight": "bold", "fontSize": "3rem", "color": "#f8f9fa"}
                ),
                html.P(
                    "Unlock beauty trends and product performances with data-driven insights.",
                    className="text-center mb-5",
                    style={"fontSize": "1.2rem", "color": "#ced4da"}
                ),
                html.Div([
                    dbc.Button(
                        "Explore Dashboard",
                        id="dashboard-button",
                        color="warning",
                        size="lg",
                        href="/dashboard",
                        className="dashboard-button",
                        style={
                            "fontSize": "1.2rem",
                            "fontWeight": "bold",
                            "padding": "12px 30px",
                            "backgroundColor": "#f7a62c",
                            "border": "none",
                            "transition": "all 0.3s ease"
                        }
                    )
                ], className="text-center"),
            ], className="p-5", style={
                "backgroundColor": "rgba(30, 30, 30, 0.2)",
                "border": "1px solid rgba(247, 166, 44, 0.5)",
                "borderRadius": "8px",
                "boxShadow": "0 0 8px rgba(247, 166, 44, 0.2)"
            })
        ], width=8, className="mx-auto")  # Narrower width, centered
    ], className="d-flex align-items-center justify-content-center", style={"height": "85vh"})
], style={
    # Subtle radial glow from bottom
    "background": "radial-gradient(circle at bottom center, rgba(247, 166, 44, 0.3) 0%, #000000 70%)",
    "backgroundSize": "cover",
    "backgroundPosition": "center",
    "height": "100vh",
    "color": "white",
    "overflow": "hidden"
})