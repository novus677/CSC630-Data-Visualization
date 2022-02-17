import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import pandas as pd
from vega_datasets import data

movies = data.movies()
movies.dropna(subset = ["Worldwide_Gross", "Production_Budget", "IMDB_Rating"], inplace=True)

fig = plt.figure(figsize=(10,9))
ax = fig.add_subplot(projection='3d')

x = np.array([movies["Production_Budget"]])
y = np.array([movies["IMDB_Rating"]])
z = np.array([movies["Worldwide_Gross"]])

norm_x, norm_y, norm_z = colors.Normalize(0,np.amax(x)), colors.Normalize(0,np.amax(y)), colors.Normalize(0,np.amax(z))
x, y, z = norm_x(x), norm_y(y), norm_z(z)
ax.scatter3D(x,y,z)

plt.suptitle("Worldwide Grossing of Movies", fontweight='bold', fontsize=20)
plt.title("(Data has been normalized)")
ax.set_xlabel('Production Budget', fontweight='bold')
ax.set_ylabel('IMDB Rating', fontweight='bold')
ax.set_zlabel('Worldwide Gross', fontweight='bold')

plt.show()