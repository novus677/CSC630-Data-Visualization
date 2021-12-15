import numpy as np
import matplotlib.pyplot as plt

total = 35480
# deckname: matches, winrate
meta = {
    "Weenie White": (12630, 57.06),
    "Mono Black Control": (5100, 56.79),
    "Mono Green Aggro": (5420, 53.09),
    "Grixis Aggro": (3370, 56.34),
    "Bant Control": (3200, 49.25),
    "Orzhov Control": (2740, 54.82),
    "Red Deck Wins": (2730, 49.63),
    "Orzhov Aggro": (2190, 54.52),
    "Jeskai Control": (2160, 51.80),
    "Sultai Control": (2160, 44.65)
}

x = [val[0] for val in meta.values()]
y = [val[1] for val in meta.values()]
plt.scatter(x, y)
plt.title("Magic the Gathering Meta Snapshot 11/29 - 12/12")
plt.xlabel("Matches played")
plt.ylabel("Winrate %")

for key, val in meta.items():
    plt.annotate(key, xy=(val[0], val[1]), textcoords="offset points", xytext=(0,7), ha='center')

plt.show()