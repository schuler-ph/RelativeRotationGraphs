import matplotlib.pyplot as plt
import matplotlib.patches as patches
from rrg_db import DatabaseManager


def setup_plot(fig, ax):
    ax.set_title("Relative Rotation Graph")
    ax.set_xlabel("RS-Ratio")
    ax.set_ylabel("RS-Momentum")
    plt.figtext(0.14, 0.14, "Lagging", color="red")
    plt.figtext(0.14, 0.84, "Improving", color="blue")
    plt.figtext(0.87, 0.84, "Leading", color="green", ha="right")
    plt.figtext(0.87, 0.14, "Weakening", color="gold", ha="right")
    windowZoom = 10
    lim = [100 - windowZoom, 100 + windowZoom]
    ax.set_xlim(lim)
    ax.set_ylim(lim)
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
    plt.gcf().set_size_inches(10, 10)


def gen_int(string, seed):
    int = hash(string + seed) % 256
    if int > 20:
        int -= 20
    return int


def gen_color(symbol):
    colRed = gen_int(symbol, "r")
    colGreen = gen_int(symbol, "g")
    colBlue = gen_int(symbol, "b")

    return "#%02X%02X%02X" % (colRed, colGreen, colBlue)


db = DatabaseManager()
config = db.get_config()

#    0        1            2
# (date, rsRatioAvg, rsMomentumAvg)

# how many plots should be created
for i in range(config["history_range"]):
    fig, ax = plt.subplots()

    setup_plot(fig, ax)

    # which etfs should be plotted
    for symbol in config["plot_symbols"]:
        dataEft = db.get_plot_data_avg(symbol)
        data = dataEft[i : i + db.get_config()["tail_length"]]
        range = "From " + data[-1][0] + " to " + data[0][0]
        plt.figtext(0.5, 0.025, range, ha="center")
        color = gen_color(symbol)

        for idx, d in enumerate(data):
            if idx == 0:
                ax.scatter(d[1], d[2], c=color, s=15)
                ax.text(d[1] + 0.1, d[2] + 0.1, symbol, color="black", fontsize=8)
            else:
                ax.scatter(d[1], d[2], c=color, s=5)
                ax.plot(
                    [data[idx - 1][1], d[1]],
                    [data[idx - 1][2], d[2]],
                    color=color,
                    linewidth=1,
                )

    number = str(config["history_range"] - i)

    if int(number) < 100 and config["history_range"] >= 100:
        number = "0" + number
    if int(number) < 10 and config["history_range"] >= 10:
        number = "0" + number

    plt.savefig("src/plots/" + config["filename"] + "_" + number + ".png")
    plt.close()
