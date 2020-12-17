import dash  #(version 1.12.0)
from dash.dependencies import Input, Output
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

import dash_bootstrap_components as dbc

#PATH = pathlib.Path(__file__).parent
#DATA_PATH = PATH.joinpath("./datasets").resolve()
# ---------------------------------------------------------------

#df1 = pd.read_csv(DATA_PATH.joinpath("Data-Emotion-01.csv"))
#df2 = pd.read_csv(DATA_PATH.joinpath("Data-Emotion-02.csv"))


# Import the cleaned data (importing csv into pandas)
df1 = pd.read_csv("data/Data-Emotion-01.csv")
# # Import the cleaned data (importing csv into pandas)
df2 = pd.read_csv("data/Data-Emotion-02.csv")


def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Tab content 1')
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Tab content 2')
        ])

# Sorting operators (https://dash.plotly.com/datatable/filtering)
# app.layout = html.Div([
#     dash_table.DataTable(
#         id='datatable-interactivity',
#         columns=[
#             {"name": i, "id": i, "deletable": True, "selectable": True, "hideable": True}
#             for i in df.columns],
#         data=df.to_dict('records'),  # the contents of the table
#         editable=True,              # allow editing of data inside all cells
#         filter_action="native",     # allow filtering of data by user ('native') or not ('none')
#         sort_action="native",       # enables data to be sorted per-column by user or not ('none')
#         sort_mode="single",         # sort across 'multi' or 'single' columns
#         column_selectable="multi",  # allow users to select 'multi' or 'single' columns
#         row_selectable="multi",     # allow users to select 'multi' or 'single' rows
#         row_deletable=True,         # choose if user can delete a row (True) or not (False)
#         selected_columns=[],        # ids of columns that user selects
#         selected_rows=[],           # indices of rows that user selects
#         page_action="native",       # all data is passed to the table up-front or not ('none')
#         page_current=0,             # page number that user is on
#         page_size=6,                # number of rows visible per page
#         style_cell={                # ensure adequate header width when text is shorter than cell's text
#             'minWidth': 95, 'maxWidth': 95, 'width': 95
#         },
#         style_cell_conditional=[    # align text columns to left. By default they are aligned to right
#             {
#                 'if': {'column_id': c},
#                 'textAlign': 'left'
#             } for c in ['Text','Emotion']
#         ],
#         style_data={                # overflow cells' content into multiple lines
#             'whiteSpace': 'normal',
#             'height': 'auto'
#         }
#     ),

#     html.Br(),
#     html.Br(),
#     html.Div(id='bar-container'),
#     html.Div(id='choromap-container')

# ])
layoutHome = html.Div(children=[
html.Div([
dbc.Button("Page 1", color="primary",href="/apps/page1" ,id="loading-button"),
dbc.Spinner(html.Div(id="loading-output"))]),
html.Div([
dbc.Button("Page 2", color="primary",href="/apps/page2" ,id="loading-button"),
dbc.Spinner(html.Div(id="loading-output"))]),
])




layout1 = html.Div([
     html.H3(
         dbc.Alert("First page"),
         className="text-center"
     ),
    dcc.Tabs(
        id='tabs-example',
        value='tab-1',
        children=[
            dcc.Tab(
                label='Kaggle dataset',
                value='tab-1',
                children=[
                    html.H3(
                        'Dataset',
                        className="text-center"
                        ),
                            dash_table.DataTable(
        id='datatable-interactivity1',
        columns=[
            {"name": i, "id": i, "deletable": True, "selectable": True, "hideable": True}
            for i in df1.columns],
        data=df1.to_dict('records'),  # the contents of the table
        editable=True,              # allow editing of data inside all cells
        filter_action="native",     # allow filtering of data by user ('native') or not ('none')
        sort_action="native",       # enables data to be sorted per-column by user or not ('none')
        sort_mode="single",         # sort across 'multi' or 'single' columns
        column_selectable="multi",  # allow users to select 'multi' or 'single' columns
        row_selectable="multi",     # allow users to select 'multi' or 'single' rows
        row_deletable=True,         # choose if user can delete a row (True) or not (False)
        selected_columns=[],        # ids of columns that user selects
        selected_rows=[],           # indices of rows that user selects
        page_action="native",       # all data is passed to the table up-front or not ('none')
        page_current=0,             # page number that user is on
        page_size=6,                # number of rows visible per page
        style_cell={                # ensure adequate header width when text is shorter than cell's text
            'minWidth': 95, 'maxWidth': 95, 'width': 95
        },
        style_cell_conditional=[    # align text columns to left. By default they are aligned to right
            {
                'if': {'column_id': c},
                'textAlign': 'left'
            } for c in ['Text','Emotion']
        ],
        style_data={                # overflow cells' content into multiple lines
            'whiteSpace': 'normal',
            'height': 'auto'
        }
    ),
 html.Br(),
    html.Br(),
    html.Div(id='bar-container1')]),
            dcc.Tab(
                label='Data World dataset',
                value='tab-2',
                children=[
                    html.H3(
                        'World Dataset',
                        className="text-center"
                    ),
                    dash_table.DataTable(
        id='datatable-interactivity2',
        columns=[
            {"name": i, "id": i, "deletable": True, "selectable": True, "hideable": True}
            for i in df2.columns],
        data=df2.to_dict('records'),  # the contents of the table
        editable=True,              # allow editing of data inside all cells
        filter_action="native",     # allow filtering of data by user ('native') or not ('none')
        sort_action="native",       # enables data to be sorted per-column by user or not ('none')
        sort_mode="single",         # sort across 'multi' or 'single' columns
        column_selectable="multi",  # allow users to select 'multi' or 'single' columns
        row_selectable="multi",     # allow users to select 'multi' or 'single' rows
        row_deletable=True,         # choose if user can delete a row (True) or not (False)
        selected_columns=[],        # ids of columns that user selects
        selected_rows=[],           # indices of rows that user selects
        page_action="native",       # all data is passed to the table up-front or not ('none')
        page_current=0,             # page number that user is on
        page_size=6,                # number of rows visible per page
        style_cell={                # ensure adequate header width when text is shorter than cell's text
            'minWidth': 95, 'maxWidth': 95, 'width': 95
        },
        style_cell_conditional=[    # align text columns to left. By default they are aligned to right
            {
                'if': {'column_id': c},
                'textAlign': 'left'
            } for c in ['content','sentiment']
        ],
        style_data={                # overflow cells' content into multiple lines
            'whiteSpace': 'normal',
            'height': 'auto'
        }
    ),
    html.Br(),
    html.Br(),
    html.Div(id='bar-container2'),
    # html.Div(id='choromap-container'),
]
)
            ]
)
])