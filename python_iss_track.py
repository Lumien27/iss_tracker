

# --- Find and plot the ISS --- #
# Only plots one time, possible adaptation, plot an hour's worth of time
# 9/19/2021

# --- import modules for plotting and data science -- #
import plotly.express as px
import pandas as pd
import time

url = 'http://api.open-notify.org/iss-now.json'

# --- create dataframe with json information --- #
df = pd.read_json(url)
# --- create two new columns labeling the iss position as their respective coordinates --- #
df['latitude'] = df.loc['latitude', 'iss_position']
df['longitude'] = df.loc['longitude', 'iss_position']
df.reset_index(inplace=True)
df = df.drop(['index', 'message'], axis=1)

frames = [df]

# --- get more 1 frame per minute for 1 hour --- #
for i in range(0, 60):
    n_df = pd.read_json(url)
    # --- create two new columns labeling the iss position as their respective coordinates --- #
    n_df['latitude'] = n_df.loc['latitude', 'iss_position']
    n_df['longitude'] = n_df.loc['longitude', 'iss_position']
    n_df.reset_index(inplace=True)
    n_df = n_df.drop(['index', 'message'], axis=1)
    frames.append(n_df)
    time.sleep(60)

df = pd.concat(frames)
fig = px.scatter_geo(df, lat='latitude', lon='longitude')

fig.show()
