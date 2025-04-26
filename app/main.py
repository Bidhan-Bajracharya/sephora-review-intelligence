import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

# Initialize app
app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True  # Allow dynamic loading of components
)
app.title = "Sephora Application"
server = app.server

# App Layout
app.layout = html.Div([
    dcc.Location(id="url"),  # Keeps track of the URL
    dcc.Store(id="session-store", storage_type="session"),  # Session storage to manage login state
    html.Div(id="page-layout")  # This will display different pages depending on the URL
])

# Callback to change layout based on URL
@app.callback(
    Output("page-layout", "children"),
    Input("url", "pathname"),
    State("session-store", "data")  # Getting the session data
)
def display_layout(pathname, session_data):
    # Login Page: No navigation links, just the login form
    if pathname == "/login":
        return dash.page_container  # login page without navigation

    # Check if the user is logged in
    if session_data and session_data.get("logged_in"):
        # If logged in, display navigation and content (Dashboard, Sentiment, etc)
        if pathname == "/":
            return dash.page_container  # Home Page with no nav

        else:
            # Protected pages with NavLinks (Dashboard, Sentiment, etc)
            return dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Div([
                # Make the logo clickable by wrapping it in a NavLink
                    dbc.NavLink(
                        html.Img(
                            src="/assets/logo.png",  # Assumes the logo is in 'public/assets/'
                            # width="auto",  # Auto width to maintain aspect ratio
                            height="40px",  # Adjust height as needed
                            className="mb-4",
                            style={"maxWidth": "100%", "height": "40px", "objectFit": "contain", "padding": "5px"},
                        ),
                        href="/",  # Redirects to homepage
                        className="d-block mb-4"  # Ensures it's aligned as a block element
                    ),
                
                dbc.Nav([
                    dbc.NavLink("Dashboard", href="/dashboard", active="exact", className="nav-link-custom"),
                    dbc.NavLink("Sentiment", href="/sentiment", active="exact", className="nav-link-custom"),
                ], vertical=True, pills=True, className="nav-pills-custom")
            ], className="bg-dark vh-100 p-3 sticky-top", style={"borderRight": "1px solid orange"})
        ], width=2, className="p-0"),

        dbc.Col([
            dash.page_container  # Protected content page (Dashboard, Sentiment)
        ], width=10, className="text-white p-4", style={"backgroundColor": "#111"})
    ])
], fluid=True)

    else:
        # If not logged in, redirect to login page
        if pathname not in ["/login"]:
            return dcc.Location(pathname="/login", id="redirect")  # Redirect to login
        return dash.page_container  # If we're on the login page, show it

if __name__ == "__main__":
    app.run(debug=True)
