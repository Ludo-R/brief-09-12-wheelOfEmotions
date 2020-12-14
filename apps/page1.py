#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 12:04:40 2020

@author: randon
"""

import plotly.graph_objects as go
import pandas as pd
import dash_table
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app

# ---------------------------------------------------
# - Import -

df = pd.read_csv('data/emotion_final.csv')
df2 = pd.read_csv("data/text_emotion.csv")

# ---------------------------------------------------
# - Figure 1 -
trace = go.Histogram(x=df["Emotion"], xbins=dict(),
                   marker=dict(color='#810303'))
layout = go.Layout(
    title="Frequency Emotions Counts From First Table"
)
fig = go.Figure(data=go.Data([trace]), layout=layout)

# - Figure 2 -
trace = go.Histogram(x=df2["sentiment"], xbins=dict(),
                   marker=dict(color='#11337E'))
layout = go.Layout(
    title="Frequency Emotions Counts From Second Table"
)
fig2 = go.Figure(data=go.Data([trace]), layout=layout)

# - Tabs -
tab1_content = dash_table.DataTable(id='container-button-timestamp',
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            export_format='csv',
            style_header={'backgroundColor': 'rgb(30, 30, 30)'},
            style_table={'overflowX': 'auto',
                         'width' : '1200px',
                         'height': '400px'},
            style_cell={
                'backgroundColor': 'rgb(50, 50, 50)',
                'color': 'white',
                'textAlign':'left'
                }
            )

tab2_content = dash_table.DataTable(id='container-button-timestamp',
            data=df2.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df2.columns],
            export_format='csv',
            style_header={'backgroundColor': 'rgb(30, 30, 30)'},
            style_table={'overflowX': 'auto',
                         'width' : '1200px',
                         'height': '400px'},
            style_cell={
                'backgroundColor': 'rgb(50, 50, 50)',
                'color': 'white',
                'textAlign':'left'
                }
            )

# ---------------------------------------------------
# - Layout -
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1(children='Data table'), className="mb-2")
        ]),
        dbc.Row([
            dbc.Col(html.H6(children='Visualising the data table from the two file'), className="mb-4")
        ]),
        dbc.Row([dbc.Tabs(
    [
        dbc.Tab(tab1_content, label="Data Kaggle",label_style={"color":"#810303"}),
        dbc.Tab(tab2_content, label="Data World", label_style={"color":"#11337E"}),
    ]
),
    ]),
        dbc.Row([
            dbc.Col(html.H1(children='Visualisation'), className="mb-2")
        ]),
        dbc.Row([
            dbc.Col(html.H6(children='In first lets see the count of emotion'), className="mb-4")
        ]), 
        dbc.Row([
                dbc.Col(dcc.Graph(id='graph-1',figure=fig),),
                dbc.Col(dcc.Graph(id='graph-2',figure=fig2),)
        ]), 
        ])
    ])