import matplotlib.pyplot as plt
import matplotlib.patches as patches
from rrg_db import DatabaseManager


def setup_plot(ax):
    ax.set_xlim([50, 150])
    ax.set_ylim([50, 150])
    ax.axhline(y=100, color="gray", linewidth=0.5)
    ax.axvline(x=100, color="gray", linewidth=0.5)
    rect = patches.Rectangle((0, 0), 100, 100, facecolor="red", alpha=0.2)
    ax.add_patch(rect)
    rect = patches.Rectangle((0, 100), 100, 100, facecolor="blue", alpha=0.2)
    ax.add_patch(rect)
    rect = patches.Rectangle((100, 100), 100, 100, facecolor="green", alpha=0.2)
    ax.add_patch(rect)
    rect = patches.Rectangle((100, 0), 100, 100, facecolor="yellow", alpha=0.2)
    ax.add_patch(rect)


db = DatabaseManager()
symbol = "xlk"
dataEft = db.get_data(symbol)

fig, ax = plt.subplots()
setup_plot(ax)


ax.scatter([98, 101, 102, 103], [98, 104, 105, 106])
ax.plot([101, 102], [104, 105])


plt.show()
