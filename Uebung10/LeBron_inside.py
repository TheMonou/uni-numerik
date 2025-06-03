from nba_api.stats.endpoints import leaguedashplayershotlocations, leaguedashplayerstats
import pandas as pd
import matplotlib.pyplot as plt

# Get shooting stats by distance
shot_data = leaguedashplayershotlocations.LeagueDashPlayerShotLocations(
    season='2023-24',
    season_type_all_star='Regular Season'
)

# Convert to DataFrame
df_shot = shot_data.get_data_frames()[0]
# Flatten MultiIndex columns
df_shot.columns = [' '.join(col).strip() for col in df_shot.columns.values]


# Get games played from player stats
player_stats = leaguedashplayerstats.LeagueDashPlayerStats(
    season='2023-24',
    season_type_all_star='Regular Season'
).get_data_frames()[0]

# Filter only relevant columns (you can inspect them using df.columns)
cols_of_interest = [
    'PLAYER_NAME',
    'Restricted Area FGA',
    'Restricted Area FG_PCT'
]

# Merge on player name
merged = pd.merge(
    df_shot,
    player_stats[['PLAYER_NAME', 'GP']],
    on='PLAYER_NAME'
)

# Compute per-game FGA within 5 feet (Restricted Area)
merged['Restricted Area FGA per game'] = merged['Restricted Area FGA'] / merged['GP']

# Select desired columns
inside_scorers = merged[['PLAYER_NAME', 'Restricted Area FGA per game', 'Restricted Area FG_PCT']]



insider_insider = {
    'Giannis Antetokounmpo': 'green',
    'Domantas Sabonis': 'green',
    'Anthony Davis': 'green',
    'Alperen Sengun': 'green',
    'Zion Williamson' : 'green',
    'LeBron James' : 'green'
}

insider_shooters = {
'Giannis Antetokounmpo': 'green',
    'Domantas Sabonis': 'green',
    'Anthony Davis': 'green',
    'Zion Williamson' : 'green',
    'LeBron James' : 'green',
    'Luke Kennard': 'red',
    'Malik Beasley': 'red',
    'CJ McCollum': 'red',
    'Jamal Murray': 'red',
    'Kyrie Irving': 'red',
    'D\'Angelo Russell': 'red',
    'Sam Hauser': 'red',
    'Stephen Curry': 'red',
    'Paul George': 'red',
    'Bojan Bogdanović' : 'red',
    'Grayson Allen' : 'red',
    'Simone Fontecchio' : 'red'
}




colors = [insider_shooters.get(player, 'white') for player in inside_scorers['PLAYER_NAME']]
# Create figure and axes
fig, ax = plt.subplots(figsize=(6, 6), facecolor='lightblue')

# Set background color of the plot area
ax.set_facecolor('lightblue')  # This changes the background of the scatterplot

# Create scatter plot
ax.scatter(x=inside_scorers["Restricted Area FGA per game"], y=inside_scorers["Restricted Area FG_PCT"], color=colors)
ax.set_xlabel("Restricted Area FGA per game")
ax.set_ylabel("Restricted Area Field Goal Percentage")
# Show plot
plt.show()


