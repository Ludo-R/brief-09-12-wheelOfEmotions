#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 12:04:54 2020

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

from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import SGDClassifier
import nltk

#-----------------------------------------
# - Layout -

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1(children='Machine learning'), className="mb-2")
        ]),
        dbc.Row([
            dbc.Col(html.H6(children='We will compare and analyse different model'), className="mb-4")
        ]),
        ])
    ])