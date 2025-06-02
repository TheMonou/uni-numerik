import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pyplot import figure

three_pointers  = pd.read_excel("3pt.xlsx")
three_point_insider = {
    'Giannis Antetokounmpo' : 'red',
    'Domantas Sabonis' : 'red',
    'Anthony Davis' : 'red',
    'Alpren Sengun' : 'red'
}

colors = [three_point_insider.get(player, 'gray') for player in three_pointers['Player']]
plt.figure()
plt.scatter(x = three_pointers["3PA"], y = three_pointers["3P%"])
plt.show()




