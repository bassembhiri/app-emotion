from dash.dependencies import Input, Output
import time
from app import app
from layouts import layoutHome, layout1
import pandas as pd
import dash  #(version 1.12.0)
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import dash_bootstrap_components as dbc
import pathlib

# from my_import.my_var import table0_brut , table0_pre

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))

def display_page(pathname):
    if pathname == '/':
        return layoutHome
    elif pathname == '/apps/page1':
        return layout1
    else:
        return '404'

@app.callback(
    Output("loading-output", "children"), [Input("loading-button", "n_clicks")])
def load_output(n):
    if n:
        time.sleep(1)
        return
    return

@app.callback(
    Output(component_id='bar-container1', component_property='children'),
    [Input(component_id='datatable-interactivity1', component_property="derived_virtual_data"),
     Input(component_id='datatable-interactivity1', component_property='derived_virtual_selected_rows'),
     Input(component_id='datatable-interactivity1', component_property='derived_virtual_selected_row_ids'),
     Input(component_id='datatable-interactivity1', component_property='selected_rows'),
     Input(component_id='datatable-interactivity1', component_property='derived_virtual_indices'),
     Input(component_id='datatable-interactivity1', component_property='derived_virtual_row_ids'),
     Input(component_id='datatable-interactivity1', component_property='active_cell'),
     Input(component_id='datatable-interactivity1', component_property='selected_cells')]
)
def update_bar1(all_rows_data, slctd_row_indices, slct_rows_names, slctd_rows,
               order_of_rows_indices, order_of_rows_names, actv_cell, slctd_cell):
    print('***************************************************************************')
    print('Data across all pages pre or post filtering: {}'.format(all_rows_data))
    print('---------------------------------------------')
    print("Indices of selected rows if part of table after filtering:{}".format(slctd_row_indices))
    print("Names of selected rows if part of table after filtering: {}".format(slct_rows_names))
    print("Indices of selected rows regardless of filtering results: {}".format(slctd_rows))
    print('---------------------------------------------')
    print("Indices of all rows pre or post filtering: {}".format(order_of_rows_indices))
    print("Names of all rows pre or post filtering: {}".format(order_of_rows_names))
    print("---------------------------------------------")
    print("Complete data of active cell: {}".format(actv_cell))
    print("Complete data of all selected cells: {}".format(slctd_cell))

    dff1 = pd.DataFrame(all_rows_data)
    #plt.figure(figsize=(20,20))
    counts01=dff1['Emotion'].value_counts()
    # solution here
    counts11 = pd.DataFrame(counts01)
    counts11 = counts11.reset_index()
    counts11.columns = ['Emotion', 'counts'] # change column names
    counts11['percent'] = (counts11['counts'] / counts11['counts'] .sum()) * 100

    # used to highlight selected countries on bar chart
    colors = ['#7FDBFF' if i in slctd_row_indices else '#0074D9'
              for i in range(len(dff1))]

    if "Text" in dff1 and "Emotion" in dff1:
        return [
            dcc.Graph(id='bar-chart',
                      figure=px.bar(
                          data_frame=counts11,
                          x="Emotion",
                          y='counts',
                          labels={"Text": "of each Emotion"}
                      ).update_layout(showlegend=False, xaxis={'categoryorder': 'total descending'})
                      .update_traces(marker_color=colors, hovertemplate="<b>%{y}</b><extra></extra>")
                      )
        ]


@app.callback(
    Output(component_id='bar-container2', component_property='children'),
    [Input(component_id='datatable-interactivity2', component_property="derived_virtual_data"),
     Input(component_id='datatable-interactivity2', component_property='derived_virtual_selected_rows'),
     Input(component_id='datatable-interactivity2', component_property='derived_virtual_selected_row_ids'),
     Input(component_id='datatable-interactivity2', component_property='selected_rows'),
     Input(component_id='datatable-interactivity2', component_property='derived_virtual_indices'),
     Input(component_id='datatable-interactivity2', component_property='derived_virtual_row_ids'),
     Input(component_id='datatable-interactivity2', component_property='active_cell'),
     Input(component_id='datatable-interactivity2', component_property='selected_cells')]
)
def update_bar2(all_rows_data, slctd_row_indices, slct_rows_names, slctd_rows,
               order_of_rows_indices, order_of_rows_names, actv_cell, slctd_cell):
    print('***************************************************************************')
    print('Data across all pages pre or post filtering: {}'.format(all_rows_data))
    print('---------------------------------------------')
    print("Indices of selected rows if part of table after filtering:{}".format(slctd_row_indices))
    print("Names of selected rows if part of table after filtering: {}".format(slct_rows_names))
    print("Indices of selected rows regardless of filtering results: {}".format(slctd_rows))
    print('---------------------------------------------')
    print("Indices of all rows pre or post filtering: {}".format(order_of_rows_indices))
    print("Names of all rows pre or post filtering: {}".format(order_of_rows_names))
    print("---------------------------------------------")
    print("Complete data of active cell: {}".format(actv_cell))
    print("Complete data of all selected cells: {}".format(slctd_cell))

    dff2 = pd.DataFrame(all_rows_data)
    #plt.figure(figsize=(20,20))
    counts02=dff2['sentiment'].value_counts()
    # solution here
    counts21 = pd.DataFrame(counts02)
    counts21 = counts21.reset_index()
    counts21.columns = ['sentiment', 'counts'] # change column names
    counts21['percent'] = (counts21['counts'] / counts21['counts'] .sum()) * 100

    # used to highlight selected countries on bar chart
    colors = ['#7FDBFF' if i in slctd_row_indices else '#0074D9'
              for i in range(len(dff2))]

    if "content" in dff2 and "sentiment" in dff2:
        return [
            dcc.Graph(id='bar-chart',
                      figure=px.bar(
                          data_frame=counts21,
                          x="sentiment",
                          y='counts',
                          labels={"Text": "of each sentiment"}
                      ).update_layout(showlegend=False, xaxis={'categoryorder': 'total descending'})
                      .update_traces(marker_color=colors, hovertemplate="<b>%{y}</b><extra></extra>")
                      )
        ]
# -------------------------------------------------------------------------------------
# Highlight selected column
@app.callback(
    Output('datatable-interactivity1', 'style_data_conditional'),
    [Input('datatable-interactivity1', 'selected_columns')])
def update_styles1(selected_columns):
    return [{
        'if': {'column_id': i},
        'background_color': '#D2F3FF'
    } for i in selected_columns]


# @app.callback(
#     Output('datatable-interactivity2', 'style_data_conditional'),
#     [Input('datatable-interactivity2', 'selected_columns')]
# )
# def update_styles2(selected_columns):
#     return [{
#         'if': {'column_id': i},
#         'background_color': '#D2F3FF'
#     } for i in selected_columns]
# # -------------------------------------------------------------------------------------

