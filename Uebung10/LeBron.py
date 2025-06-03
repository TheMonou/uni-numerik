import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pyplot import figure

three_pointers = pd.read_excel("3pt.xlsx")
three_point_insider = {
    'Giannis Antetokounmpo': 'red',
    'Domantas Sabonis': 'red',
    'Anthony Davis': 'red',
    'Alpren Sengun': 'red'
}
three_point_shooters = {
    'Giannis Antetokounmpo': 'red',
    'Domantas Sabonis': 'red',
    'Anthony Davis': 'red',
    'Zion Williamson': 'green',
    'Alpren Sengun': 'red',
    'Luke Kennard': 'green',
    'Malik Beasley': 'green',
    'CJ McCollum': 'green',
    'Jamal Murray': 'green',
    'Kyrie Irving': 'green',
    'D\'Angelo Russell': 'green',
    'Sam Hauser': 'green',
    'Stephen Curry': 'green',
    'Paul George': 'green',
    'Bojan Bogdanović': 'green',
    'Grayson Allen': 'green',
    'Simone Fontecchio': 'green'
}

colors = [three_point_shooters.get(player, 'white') for player in three_pointers['Player']]
# Create figure and axes
fig, ax = plt.subplots(figsize=(6, 6), facecolor='lightblue')

# Set background color of the plot area
ax.set_facecolor('lightblue')  # This changes the background of the scatterplot

# Create scatter plot
ax.scatter(x=three_pointers["3PA"], y=three_pointers["3P%"], color=colors)
ax.set_xlabel("3-Point Attempts")
ax.set_ylabel("3-Point Percentage")
# Show plot
plt.show()
