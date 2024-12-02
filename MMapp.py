import MMcalc as mm
from dash import dash, dcc, html, Output, Input, State
import pandas as pd
import numpy as np
import base64
import io
import plotly.graph_objects as go

#Intialize data storage variable
uploaded = None

#Initialize Dash
app = dash.Dash(__name__)

#Dash Layout
app.layout = html.Div([html.H1(children='MMsuit: Michaelis-Menten Suit', style={"textAlign": "center", "marginBottom": "20px"}),
                       ## Upload button
                       html.H3(children='Upload your data as Substrate in one column and Velocity in the other column\nMMsuit fits your data to Michaelis-Menten and LineWeaver-Burk equations'),
                       dcc.Upload(id = 'upload-input',
                                  children= html.Button('Upload'), multiple=False),
                       html.Div(id='upload-output', style={"marginTop": "10px", "color": "#D4AF37"}),
                       html.Div([
                           ## Michaelis-Menten plot
                           html.Div([dcc.Markdown('''
                           ***Michaelis-Menten equation***\n
                           $V = Vmax*[S]/(Km + [S])$\n
                           $V$: velocity, $Vmax$: Maximum velocity, $S$: substrate concentration, $Km$: Michaelis-Menten constant
                           ''',mathjax=True, style={"color": "#D4AF37"}),
                                     dcc.Graph(id='MM-plot')],style={"width": "48%", "display": "inline-block"}),
                           ## Linweaver-Burk plot
                           html.Div([dcc.Markdown('''
                                                      ***Lineweaver-Burk equation***\n
                                                      $1/V = (Km/Vmax)*(1/S)+(1/Vmax)$\n
                                                      $V$: velocity, $Vmax$: Maximum velocity, $S$: substrate concentration, $Km$: Michaelis-Menten constant
                                                      ''',mathjax=True ,style={"color": "#D4AF37"}),
                                     dcc.Graph(id='LB-plot')],style={"width": "48%", "display": "inline-block"})],
                                  style={"display": "flex", "justify-content": "space-between"}),

                       ## Display Km and Vmax
                       html.Div([html.Div([html.Label("Vmax:"),
                                       dcc.Input(id="vmax-box",type="text",value="N/A",readOnly=True,
                                           style={"width": "100px", "backgroundColor": "white", "color": "black"})],
                                   style={"display": "inline-block", "marginRight": "20px"}),
                                        html.Div([html.Label("Km:"),
                                       dcc.Input(id="km-box",type="text",value="N/A",readOnly=True,
                                           style={"width": "100px", "backgroundColor": "white", "color": "black"})],
                                   style={"display": "inline-block"}),
                                        ],
                           style={"marginBottom": "20px", "color": "#D4AF37", "textAlign": "center"},
                       ),

                       ## Michaelis-Menten Simulator
                       html.Div([html.H3(children='Simulate Michaelis-Menten plot by inserting Km and Vmax'),
                           ## Km
                               html.Label("Enter Km:"),
                               dcc.Input(id="input-km", type="number", placeholder="Enter a positive number", min=0, step=0.01),
                           ## Vmax
                               html.Label("Enter Vmax:", style={"marginLeft": "12px"}),
                               dcc.Input(id="input-vmax", type="number", placeholder="Enter a positive number", min=0, step=0.01),
                               html.Button("Michaelis-Menten Simulator", id="button-michaelis-menten",n_clicks=0,
                                   style={"marginLeft": "12px"}
                                   ),
                           ## Michaelis-Menten simulated plot
                               dcc.Graph(
                                   id="simulatedMM-plot",
                                   style={"width": "48%","marginTop": "20px", "backgroundColor": "white", "padding": "10px", "borderRadius": "5px", },
                               ),
                           ],
                           style={"color": "#D4AF37", "marginTop": "20px"},
                       ),

                     ],
                      style={"border": "5px solid purple",  # Purple border
                             "padding": "20px",
                             "backgroundColor": "#4B2E83",  # UW Huskies Purple background
                             "color": "#D4AF37",  # Gold text color
                             "fontFamily": "Arial, sans-serif"})


#Dash Callbacks
@app.callback([Output('upload-output', 'children'),
              Output('MM-plot', 'figure'),
                Output('LB-plot', 'figure'),
               Output('vmax-box','value'),
               Output('km-box','value')],
              Input('upload-input', 'contents'),
              State('upload-input', 'filename'))
def update_output(contents,filename):
    global uploaded
    if contents is not None:
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        try:
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
            uploaded = np.transpose(df.to_numpy())
            uploaded = (uploaded[0],uploaded[1])
            if df.shape[1] >= 2:
                MMfig = mm.MMplot(uploaded)
                LBfig = mm.LBplot(uploaded)
                fittedMMparams = mm.MMfitter(uploaded)
                Vmax = fittedMMparams[1][1]
                Km = fittedMMparams[1][0]
            else:
                fig = go.Figure()
                fig.add_annotation(text="Insufficient Data for Plotting",
                                   xref="paper", yref="paper",
                                   showarrow=False,
                                   font=dict(size=16, color="red"))
            return f'Yay! {filename} uploaded successfully!', MMfig, LBfig, f'{Vmax:.2f}', f'{Km:.2f}'
        except:
            return 'Error reading file',go.Figure(),go.Figure(),'N/A','N/A'
    return 'Please upload a file', go.Figure(),go.Figure(),'N/A','N/A'

@app.callback(
    Output("simulatedMM-plot", "figure"),
    Input("button-michaelis-menten", "n_clicks"),
    [State("input-km", "value"), State("input-vmax", "value")],
)
def update_simulated(n_clicks, km, vmax):
    if n_clicks > 0 and km is not None and vmax is not None:
        simulatedfig = mm.MMsimulator(km, vmax)
        return simulatedfig
    return go.Figure()
#Run Dash
def MMsuit(debug=True, host="127.0.0.1", port=8050):
    app.run_server(debug=debug, host=host, port=port)
    if __name__ == "__main__":
        MMsuit()
MMsuit()

