from nba_api.stats.endpoints import leaguedashplayerstats
import pandas as pd
import matplotlib.pyplot as plt

# Query player stats for the 2023-24 regular season
stats = leaguedashplayerstats.LeagueDashPlayerStats(
    season='2023-24',
    season_type_all_star='Regular Season'
)

three_point_insider = {
    'Giannis Antetokounmpo': 'red',
    'Domantas Sabonis': 'red',
    'Anthony Davis': 'red',
    'Alpren Sengun': 'red'
}
three_point_shooters = {
    'Luke Kennard': 'green',
    'Malik Beasley': 'green',
    'CJ McCollum': 'green',
    'Jamal Murray': 'green',
    'Kyrie Irving': 'green',
    'D\'Angelo Russell': 'green',
    'Sam Hauser': 'green',
    'Stephen Curry': 'green',
    'Paul George': 'green',
    'Bojan Bogdanović' : 'green',
    'Grayson Allen' : 'green',
    'Simone Fontecchio' : 'green'
}


colors = [three_point_shooters.get(player, 'white') for player in three_pointers['Player']]
# Create figure and axes
fig, ax = plt.subplots(figsize=(6, 6), facecolor='lightblue')

# Set background color of the plot area
ax.set_facecolor('lightblue')  # This changes the background of the scatterplot

# Convert to DataFrame
df = stats.get_data_frames()[0]

print(df.)

player_inside_scoring = df['']
