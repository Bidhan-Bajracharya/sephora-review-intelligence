import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate

# Register the login page
dash.register_page(__name__, path="/login", name="Login")

# Login Page Layout
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col([
                    html.Div(
                        html.Img(
                            src="/assets/logo.png",  # Make sure your logo is inside assets folder
                            style={
                                "width": "150px",
                                "marginBottom": "20px",
                                "display": "block",
                                "marginLeft": "auto",
                                "marginRight": "auto",
                                "marginTop": "100px",
                            }
                        )
                    ),
                html.Div([
                    html.H2(
                        "Login",
                        className="mb-4 text-center",
                        style={"color": "#f8f9fa", "fontWeight": "bold"}
                    ),
                    dbc.Input(
                        id="login-username",
                        placeholder="Username",
                        type="text",
                        className="mb-3",
                        style={
                            "backgroundColor": "#2c2c2c",
                            "color": "#f8f9fa",
                            "border": "1px solid #ced4da"
                        }
                    ),
                    dbc.Input(
                        id="login-password",
                        placeholder="Password",
                        type="password",
                        className="mb-3",
                        style={
                            "backgroundColor": "#2c2c2c",
                            "color": "#f8f9fa",
                            "border": "1px solid #ced4da"
                        }
                    ),
                    html.Div(
                        id="login-error",
                        style={"color": "red", "textAlign": "center", "marginBottom": "10px"}
                    ),
                    dbc.Button(
                        "Login",
                        id="login-button",
                        color="warning",
                        className="w-100 mb-3 login-button",
                        style={
                            "backgroundColor": "#f7a62c",
                            "border": "none",
                            "fontWeight": "bold",
                            "transition": "all 0.3s ease"
                        }
                    ),
                ], className="p-4", style={
                    "backgroundColor": "rgba(30, 30, 30, 0.2)",
                    "border": "1px solid rgba(247, 166, 44, 0.5)",
                    "borderRadius": "8px",
                    "boxShadow": "0 0 8px rgba(247, 166, 44, 0.2)",
                    "maxWidth": "400px",
                    "margin": "auto",
                    # "marginTop": "100px"
                })
            ], width=8, className="mx-auto")
        ], className="d-flex justify-content-center", style={"minHeight": "100vh"})
    ], fluid=True)
], style={
    # Subtle radial glow from bottom
    "background": "radial-gradient(circle at bottom center, rgba(247, 166, 44, 0.3) 0%, #000000 70%)",
    # "background": "radial-gradient(circle at bottom center, rgba(247, 166, 44, 0.3) 0%, rgba(0, 0, 0, 0.2) 50%, #000000 70%)",
    "backgroundSize": "cover",
    "backgroundPosition": "center",
    "height": "100vh",
    "overflow": "hidden"
})

# Callback for Login Logic
@dash.callback(
    Output("session-store", "data"),  # Store login session
    Output("url", "href"),  # Redirect to home page
    Output("login-error", "children"),
    Input("login-button", "n_clicks"),
    State("login-username", "value"),
    State("login-password", "value"),
    prevent_initial_call=True
)
def perform_login(n_clicks, username, password):
    if n_clicks is None:
        raise PreventUpdate

    # Check credentials
    if username == "admin" and password == "sephora123":
        # Successfully logged in, redirect to home
        return {"logged_in": True}, "/", ""
    else:
        # Invalid login, do nothing
        return dash.no_update, dash.no_update, "Invalid username or password. Please try again."