import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go


def plot_log(logs, title=None):
    """
    Function to plot well logs data using matplotlib.

    Arguments:
        logs (dataframe): each log is a column

    Keyword Arguments:
        title (str or None): text to add as title if required

    Returns:
        plotly figure: plot
    """

    logs.dropna(axis=0, how='any', inplace=True)

    logs.reset_index(inplace=True)
    logs = logs.replace({np.nan: None})

    names = list(logs.columns)
    if 'DEPT' in names:
        logs["Depth"] = logs["DEPT"]
        names.pop(names.index('DEPT'))
    else:
        logs["Depth"] = list(logs.index)
    logs = logs.sort_values(by='Depth')

    fig = make_subplots(rows=1, cols=len(names),
                        subplot_titles=names)
    col = 1
    for x in names:
        fig.add_trace(
            go.Scatter(x=logs[x], y=logs.Depth),
            row=1, col=col
        )
        col += 1

    fig.update_layout(height=600, width=800, showlegend=False)

    if title is not None:
        fig.update_layout(title_text=title)

    return fig
