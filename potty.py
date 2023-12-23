import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Generate some example data
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a subplot
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter'}]])

# Add initial traces
trace1 = go.Scatter(x=x, y=y1, mode='lines', name='Sin(x)')
trace2 = go.Scatter(x=x, y=y2, mode='lines', name='Cos(x)')
fig.add_trace(trace1)
fig.add_trace(trace2)

# Define animation frames
frames = [go.Frame(data=[go.Scatter(x=x, y=np.sin(x + i), mode='lines', name='Sin(x)'),
                          go.Scatter(x=x, y=np.cos(x + i), mode='lines', name='Cos(x)')],
                  name=str(i))
          for i in np.arange(0, 2 * np.pi, 0.1)]

# Add frames to the figure
fig.frames = frames

# Update layout
fig.update_layout(updatemenus=[{'type': 'buttons', 'showactive': False, 'buttons': [
    {'label': 'Play',
     'method': 'animate',
     'args': [None, {'fromcurrent': True, 'frame': {'duration': 50, 'redraw': True}, 'mode': 'immediate'}]},
    {'label': 'Pause', 'method': 'animate', 'args': [[None], {'frame': {'duration': 0, 'redraw': True}, 'mode': 'immediate'}]}
]}])

# Show the plot
fig.show()