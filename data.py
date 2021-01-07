## This file manages, reads, updates, and transforms game data.

import pandas as pd

players_df = pd.read_csv('players.csv')
scores_df = pd.read_csv('scores.csv')

def df_to_dict(df):
	return df.to_dict('records')

