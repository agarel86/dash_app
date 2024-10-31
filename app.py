import pandas as pd
data_to_show=pd.read_csv("answers.csv", delimiter=";")
from dash import Dash, html, dash_table, dcc, Input, Output,callback
app = Dash()
server = app.server
app.title = "CSRD Information Retrieval App"

app.layout = [
              html.Div(html.H2("CSRD Information Retrieval App")),
              html.Div(children='Disclosure Requirement S1-9 – Diversity indicators. #63: The undertaking shall disclose the gender distribution at top management'),
              html.Hr(),
              html.Div(children='Select the company or interest:'),
              dcc.Dropdown(data_to_show["Firm"].drop_duplicates(), data_to_show["Firm"].drop_duplicates()[0], id='demo-dropdown'),
              html.Hr(),
              #dash_table.DataTable(data=data_to_show.to_dict('records'))
              html.Div(children='Below we report what our AI assistant has answered to the following diversity-related questions:'),
              html.Div(id='Q0'),
              html.Div(id='Q1'),
              html.Div(id='Q2'),
              html.Div(id='Q3'),
              html.Div(id='Q4'),
              html.Div(id='Q5'),
              html.Div(id='Q6'),
              ]

@callback(
    [Output('Q0', 'children'),Output('Q1', 'children'),Output('Q2', 'children'),Output('Q3', 'children'),Output('Q4', 'children'),Output('Q5', 'children'),Output('Q6', 'children')],
    Input('demo-dropdown', 'value'),
    prevent_initial_call=True
)

def update_output(value):
    if value==None:
        raise PreventUpdate
    else:
        data_sub = data_to_show[data_to_show["Firm"]==value]
        data_sub = data_sub[["Question", "Answer"]].reset_index()
        mylist=[]
        for x in range(0,len(data_sub)):
            text = html.P([html.B("Question:"), data_sub["Question"][x], html.Br(), html.B("Answer:"), data_sub["Answer"][x], html.Br()])
            mylist.append(text)
        return mylist

if __name__ == '__main__':
    app.run(debug=True)
