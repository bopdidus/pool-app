from flask import Flask
import dash
import dash_bootstrap_components as dbc

server = Flask(__name__)

server.config['DEBUG'] = True

app = dash.Dash(__name__, server=server, url_base_pathname='/dashApp/',
                             external_stylesheets=[dbc.themes.BOOTSTRAP, 'dashboard.css'])
app.config['suppress_callback_exceptions'] = True

from dash_package import routes