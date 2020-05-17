import dash_core_components as dcc
import dash_html_components as html
import dash
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
            children=[
                        dcc.Input(id="cell-1", type="number", value=0, placeholder="cell-1"),
                                dcc.Input(id="cell-2", type="number", value=0, placeholder="cell-2"),
                                        html.H1(id="output-cell"),
                                            ]
            )

@app.callback(
            output=Output("output-cell", "children"),
                inputs=[Input("cell-1", "value"), Input("cell-2", "value")],
                )
def sum_of_cell1_and_cell2(value_of_cell1, value_of_cell2):
    return int(value_of_cell1) + int(value_of_cell2)

if __name__ == "__main__":
    app.run_server(host="localhost", debug=True)
