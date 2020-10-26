import numpy as np
import matplotlib.pyplot as plt


def plot_log(logs):
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
    top = logs.Depth.min()
    bot = logs.Depth.max()

    length = int((12 / 5) * len(names))
    fig, ax = plt.subplots(nrows=1, ncols=len(names), figsize=(length, 8))

    colors = ['green', 'red', 'black', 'blue', 'c', 'orange', 'pink', 'purple']
    color = colors[0]
    for x in names:
        ax[names.index(x)].plot(logs[x], logs.Depth, color=color)
        if color == colors[-1]:
            color = colors[0]
        color = colors[colors.index(color) + 1]

    for i in range(len(ax)):
        ax[i].set_ylim(top, bot)
        ax[i].invert_yaxis()
        ax[i].grid()

    for x in names:
        ax[names.index(x)].set_xlim(logs[x].min(), logs[x].max())
        ax[names.index(x)].set_xlabel(x)
        if x == names[0]:
            ax[names.index(x)].set_ylabel("Depth")
        else:
            ax[names.index(x)].yaxis.set_ticklabels([])

    return fig
